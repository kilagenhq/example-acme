---
id: gap-portal-export-idor
type: gap
title: Merchant portal export returned another merchant's transactions
description: The portal's export endpoint authorised the session but not the record, so a merchant could read another merchant's transactions by changing an id. Closed 2026-05-02.
owner: role-appsec-eng
requirement: std-secure-development#2.1
source: bug-bounty
found: '2026-04-14'
severity: high
source_url: https://hackerone.example.com/reports/2026-0414
tracker: https://acme.atlassian.net/browse/APPSEC-72
remediated: '2026-05-02'
domains:
- appsec
systems:
- semgrep
---

# Merchant portal export returned another merchant's transactions

Authorisation moved to the resource layer and covered by a regression test; a Semgrep rule now catches the pattern at review time.
