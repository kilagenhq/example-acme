---
id: gap-dlp-coverage-partial
type: gap
title: Data loss prevention covers outbound email only
description: Outbound email is inspected for cardholder data; file sharing, endpoints and the merchant portal are not, so three of the four ways data leaves Acme are unmonitored.
owner: role-it-manager
requirement: std-data-protection-controls#6.6
source: risk-assessment
found: '2026-02-20'
severity: medium
tracker: https://acme.atlassian.net/browse/SEC-377
domains:
- data-security
related:
- rsk-cardholder-data-exposure
systems:
- google-workspace
---

# Data loss prevention covers outbound email only

## What is missing

Data loss prevention runs on outbound email only. The three routes it does not
cover are the file-sharing tenant, removable media on endpoints, and the
merchant portal's own export feature — which is the route
`gap-portal-export-idor` already proved can return the wrong merchant's data.

## Why it is still open

The email rules were bought as part of the mail gateway and cost nothing extra
to turn on. Covering the other three means a separate product, an agent on
every endpoint, and a tuning period that the security engineer does not have
capacity for while the logging work in `gap-portal-logs-not-onboarded` is
unfinished. It has been deprioritised twice, both times deliberately.

## What closes it

Inspection on the file-sharing tenant and on endpoints, with the rule set
scoped to the cardholder data patterns in `da-cardholder-data`, and a documented
decision on the portal export — either inspect it or remove it. Until then the
residual exposure is carried in `rsk-cardholder-data-exposure`.
