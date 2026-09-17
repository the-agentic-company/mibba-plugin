---
name: dossier-research
description: Researches Mibba notarial dossiers and their documents with traceable evidence. Use when the user asks to find, inspect, compare, or summarize a dossier, client, participant, property, document, or fact stored in Mibba.
---

# Mibba dossier research

Use the Mibba MCP tools to answer from the user's authorized workspace.

## Method

1. Resolve the dossier before making detailed claims. Use `search_legal_records` when the user supplied a title, reference, type, status, date range, or Septeo identifier. Ask for clarification only when multiple plausible dossiers remain.
2. Use `get_legal_record` to establish the dossier's participants, properties, folders, document metadata, case items, and human decisions.
3. Find documents with `search_documents`. Prefer documents with active text when the task requires document contents.
4. Search contents with `search_document_text` for known document IDs or `search_document_evidence` for a semantic question across the relevant corpus. Follow the tool's `nextSteps` and search-budget metadata.
5. Read only the relevant pages with `get_document_page`, `get_document_evidence`, or `multi_get_document_evidence`. Do not load whole documents when page-level evidence is enough.
6. Cite the URLs returned by Mibba. Never construct a citation URL, page number, dossier identifier, or document identifier yourself.

## Reliability rules

- Separate facts stated in evidence from inference. Label uncertainty plainly.
- Never treat an empty or failed search as proof that a fact or document does not exist.
- Preserve the legal subject of a fact: a company's asset, debt, or obligation is not automatically a participant's personal fact.
- Respect `humanDecisions` returned by the dossier assessment. Do not recreate a dismissed, resolved, or obsolete case item unless newer dated evidence justifies it, and explain that evidence.
- Do not expose raw internal identifiers unless the user specifically needs one for a technical task.
- If a tool returns an error, follow its retry hint. Use `report_semantic_friction` when the tools are semantically inadequate, ambiguous, repeatedly empty, or scoped incorrectly.

End with a concise answer, the supporting citations, and any material coverage gaps.
