# AI Defect Analysis — Prompt Reference

This document records the exact prompts used by the `LLM/Ask LLM#1` node in the
**Awaiting Review AI Defect Analysis** workflow (V-ONE low-code platform,
Forklift Daily Pre-Start Checklist App). Both prompts are extracted 1:1 from
the app's exported `template.json`.

---

## 1. System Prompt

Configured on the `LLM/Ask LLM#1` node. Sets the model's role and response style.

```
You are an expert industrial safety and forklift maintenance specialist. Evaluate pre-start inspection defects and provide concise, authoritative action advice.
```

---

## 2. User Prompt Template

Built by the `Code/Python#1` node from the triggering ticket record, then passed
to the LLM alongside the system prompt above.

```
Analyze the following forklift defect remark from a pre-start inspection ticket under Awaiting Review status and provide clear, actionable advice for the Person-In-Charge (PIC):

Remark: {inspection_remarks}

Provide your response strictly starting with:
AI Summary: [Suggested Actions]
```

- `{inspection_remarks}` is read from the ticket record's `inspection_remarks` field.
- **Fallback:** if the field is missing, or the record is not a dict, the template falls back to the default remark: `"Minor defect observed during pre-start check"`.
