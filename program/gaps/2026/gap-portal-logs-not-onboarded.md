---
id: gap-portal-logs-not-onboarded
type: gap
title: Merchant portal application logs are not collected centrally
description: The merchant portal writes its logs to local disk and nothing forwards them, so the one system merchants touch directly is invisible to detection and lost on rebuild.
owner: role-secops-analyst
requirement: std-logging-monitoring#5.1
source: internal
found: '2026-01-24'
severity: medium
tracker: https://acme.atlassian.net/browse/SEC-355
domains:
- secops
related:
- pro-vulnerability-triage
systems:
- elastic-siem
---

# Merchant portal application logs are not collected centrally

## What is missing

Every other production system forwards to the SIEM. The merchant portal does
not: it writes to local disk on instances that are replaced on every deploy, so
its logs have a lifetime of about a day and exist in no place anybody looks.

That leaves the portal outside detection, outside the twelve-month retention
`std-logging-monitoring` 5.2 requires, and outside incident response. When
`gap-portal-export-idor` was found, the question of whether anyone had exploited
it before the fix could not be answered from the record — which is the concrete
cost of this gap and the reason it is filed against 5.1 rather than 5.2.

## Why it is still open

The portal predates the logging standard and writes an unstructured format the
collector cannot parse. Onboarding it means changing the application's log
output first, which is an engineering change on a system whose team is fully
committed to the PCI remediation work.

## What closes it

Structured output from the portal, the collector configured against it, and a
detection for repeated authorisation failures by one merchant — the signal that
would have made the export defect visible while it was happening.
