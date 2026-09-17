---
name: document-audit
description: Audits a Mibba dossier's document inventory, cited pieces, evidence, and legal deadlines. Use when the user asks what is present or missing, whether an act's annexes are available, or which dossier deadlines need attention.
---

# Mibba document audit

Audit only the dossier the user selected or the single dossier you unambiguously resolve.

## Inventory and cited pieces

1. Resolve the dossier with `search_legal_records`, then load it with `get_legal_record`.
2. Enumerate relevant documents with `search_documents`. Use pagination and totals when present; never describe a truncated first page as a complete inventory.
3. When an act cites annexes or promised pieces, use `match_cited_documents`. Preserve its `present`, `uncertain`, and `absent` classifications.
4. For an `uncertain` match, inspect the suggested page or search the document text before concluding. A poorly named scan may still contain the cited piece.
5. Describe an absent piece as an observed inventory gap, not proof that the étude never received it.

## Deadlines

Use `compute_dossier_deadlines` for retraction periods, loan-offer acceptance, and diagnostic expiry. Supply only dates read from Mibba evidence, and cite the pages that establish those dates. Do not calculate legal deadlines mentally when the tool covers them.

## Output

Group results into present pieces, uncertain matches, observed gaps, and deadlines. Include Mibba-provided citations beside each material finding and state any unreadable or unsynchronized-document limitations.
