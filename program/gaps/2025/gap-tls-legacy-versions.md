---
id: gap-tls-legacy-versions
type: gap
title: Legacy TLS versions accepted at the edge
description: The edge accepted TLS 1.0 and 1.1 alongside 1.2, so a downgrade was available to anyone who asked for it. Closed 2026-01-08.
owner: role-security-eng
requirement: std-data-protection-controls#6.2
source: audit
found: '2025-11-05'
severity: medium
tracker: https://acme.atlassian.net/browse/SEC-318
remediated: '2026-01-08'
domains:
- data-security
systems:
- cloudflare
---

# Legacy TLS versions accepted at the edge

TLS 1.0 and 1.1 disabled at the edge; minimum raised to 1.2 and monitored continuously.
