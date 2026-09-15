"""
cli.py — run the extracted logic from the command line.

    python -m forklift_defect_analysis "Brake pedal travel noticeably longer than normal"

Prints the exact prompt that would be sent to the LLM node, then (if
OPENAI_API_KEY is set) actually calls the LLM and prints its response.
"""

from __future__ import annotations

import sys

from .prompt_builder import build_prompt
from .llm_client import analyze_defect, LLMConfigError


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    remark = " ".join(argv) if argv else None
    record = {"inspection_remarks": remark} if remark else {}

    prompt = build_prompt(record)
    print("--- Prompt sent to LLM/Ask LLM ---")
    print(prompt)
    print()

    try:
        print("--- LLM response ---")
        print(analyze_defect(record))
    except LLMConfigError as exc:
        print(f"(skipped live call: {exc})")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
