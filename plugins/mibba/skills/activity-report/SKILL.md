---
name: activity-report
description: Produces complete monthly or annual Mibba dossier activity reports. Use when the user asks how many dossiers were active, modified, or currently closed over a year or bounded period.
---

# Mibba activity report

Use `get_legal_record_activity_report` instead of counting a page of search results.

## Method

1. Resolve the requested civil year or exact `from` and `toExclusive` period. Ask only if the period is genuinely ambiguous.
2. Request the complete report. Periods longer than the tool's supported maximum must be split into non-overlapping intervals.
3. Present the total and the monthly breakdown in Europe/Paris calendar time.
4. Include the report's synchronization and data-quality metadata, especially records missing a synchronized modification date.

## Interpretation

The report counts records by their synchronized Septeo modification timestamp. A record whose current status is `Clôturé` belongs to the closed-status subset, but that does not establish when the status changed. Never describe this as an exact closure-date report unless separate evidence supplies closure dates.
