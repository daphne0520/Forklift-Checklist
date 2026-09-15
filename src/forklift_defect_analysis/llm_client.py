"""
llm_client.py

Makes the extracted prompt actually *do* something end-to-end: sends it to a
real LLM and returns the response text — standing in for the platform's
built-in `LLM/Ask LLM` node, which this module's caller is not able to
reach directly since it only exists inside V-ONE.

Uses the OpenAI API by default (the most common drop-in choice). Swap
`_call_openai` for another provider's SDK if your workflow's LLM node is
actually wired to Anthropic, Azure OpenAI, etc. — the rest of this package
doesn't care which provider answers, only that something implementing
``ask(system_prompt, question) -> str`` does.

Requires the OPENAI_API_KEY environment variable to actually call out to the
network. Everything else in this package (prompt_builder, tests) has no
network dependency at all.
"""

from __future__ import annotations

import os
from .prompt_builder import SYSTEM_PROMPT, build_prompt


class LLMConfigError(RuntimeError):
    """Raised when no API key / client is configured."""


def _call_openai(system_prompt: str, question: str, model: str = "gpt-4o-mini") -> str:
    try:
        from openai import OpenAI
    except ImportError as exc:  # pragma: no cover
        raise LLMConfigError(
            "The 'openai' package is required to actually call the LLM. "
            "Install it with: pip install openai"
        ) from exc

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise LLMConfigError(
            "OPENAI_API_KEY is not set. Export it before running, e.g.:\n"
            "  export OPENAI_API_KEY=sk-...\n"
            "(or swap _call_openai in llm_client.py for your own provider)."
        )

    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question},
        ],
    )
    return completion.choices[0].message.content


def analyze_defect(record: dict, model: str = "gpt-4o-mini") -> str:
    """End-to-end: ticket record in -> AI-generated defect summary out.

    Rebuilds exactly what the V-ONE workflow does:
        Ticket/Record Updated -> Code/Python#1 (prompt_builder.build_prompt)
                               -> LLM/Ask LLM#1 (this function's LLM call)
    """
    question = build_prompt(record)
    return _call_openai(SYSTEM_PROMPT, question, model=model)
