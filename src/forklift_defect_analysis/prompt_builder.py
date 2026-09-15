"""
prompt_builder.py

A faithful, 1:1 extraction of the **exact** source code that ships inside the
`Code/Python#1` node of the "Awaiting Review AI Defect Analysis" workflow
(V-ONE low-code platform, Forklift Daily Pre-Start Checklist App).

This is not a rewrite or a "fixed" version — it is the literal logic pulled
straight out of the app's exported `template.json`, translated from the
platform's `parameter[]` / `output[]` node convention into an ordinary,
importable Python function so it can actually run (and be tested) outside
the V-ONE canvas.

Original node source, verbatim (as stored in the exported workflow graph):

    data = parameter[1] if len(parameter) > 1 and isinstance(parameter[1], dict) else {}
    remarks = data.get('inspection_remarks', 'Minor defect observed during pre-start check')
    output[1] = f\"\"\"Analyze the following forklift defect remark from a pre-start
    inspection ticket under Awaiting Review status and provide clear, actionable
    advice for the Person-In-Charge (PIC):

    Remark: {remarks}

    Provide your response strictly starting with:
    AI Summary: [Suggested Actions]\"\"\"

Known limitation (present in the original, unchanged here): this node has no
status gate — on the live canvas it fires on *any* `Ticket/Record Updated`
event, not only the transition into "Awaiting Review". See README.md.
"""

from __future__ import annotations

DEFAULT_REMARK = "Minor defect observed during pre-start check"

# The exact system prompt configured on the paired LLM/Ask LLM#1 node.
SYSTEM_PROMPT = (
    "You are an expert industrial safety and forklift maintenance specialist. "
    "Evaluate pre-start inspection defects and provide concise, authoritative "
    "action advice."
)


def build_prompt(record: dict) -> str:
    """1:1 port of the node body.

    Original:
        data = parameter[1] if len(parameter) > 1 and isinstance(parameter[1], dict) else {}
        remarks = data.get('inspection_remarks', 'Minor defect observed during pre-start check')
        output[1] = f"..."

    Here, ``record`` stands in for ``parameter[1]`` (the triggering ticket
    record) and the return value stands in for ``output[1]``.
    """
    data = record if isinstance(record, dict) else {}
    remarks = data.get("inspection_remarks", DEFAULT_REMARK)

    return f"""Analyze the following forklift defect remark from a pre-start inspection ticket under Awaiting Review status and provide clear, actionable advice for the Person-In-Charge (PIC):

Remark: {remarks}

Provide your response strictly starting with:
AI Summary: [Suggested Actions]"""
