---
id: rsk-cloud-misconfiguration-exposure
type: risk
title: Cloud Misconfiguration Exposing Data or Access
description: 'A storage bucket, security group or identity policy is misconfigured and exposes
  data or an access path that was never intended to exist.

  '
status: active
owner: role-security-eng
domains:
- grc
- infra
related:
- std-asset-management
- std-secure-development
systems:
- aws
- trivy
- wiz
impact: medium
likelihood: low
severity: medium
tracker: https://acme.atlassian.net/browse/SEC-301
treatment: mitigate
root_causes:
- misconfiguration
- human-error
risk_category:
  principle: operational-risk
  category1: information-security
  category2: data-breach
last_reviewed: '2026-07-15'
next_review: '2026-10-15'
---

# Cloud Misconfiguration Exposing Data or Access

## Risk statement

Misconfiguration is how cloud environments are usually breached, and it does
not require an attacker to do anything sophisticated — only to find the mistake
before the owner does.

## Assessment

| Dimension | Rating | Reasoning |
|---|---|---|
| Likelihood | Low | Infrastructure is code and reviewed; posture management is continuous |
| Impact | Medium | Non-CDE accounts hold internal and merchant data, not cardholder data |
| Severity | Medium | 2 × 3 = 6, per the matrix in `std-risk-framework` |
| Control effectiveness | Substantially | Detection is strong; prevention at merge time is advisory only |

## Treatment

**Mitigate.** The interesting part of this risk is the asymmetry between two
controls in the same chain: posture management runs continuously and blocks,
while the infrastructure-as-code scanning that would stop the misconfiguration
reaching production only advises — which is `gap-iac-findings-advisory`.

| Action | Owner | Status |
|---|---|---|
| Agree the IaC baseline so Trivy findings can block a merge | role-security-eng | Gap `gap-iac-findings-advisory` |
| Extend runtime protection to the remaining two clusters | role-security-eng | Backlog |
| Quarterly review of public-facing resources | role-security-eng | In place |

## Acceptance

Accepted at `medium` by the CISO. It would be re-scored upward immediately if
the cardholder data environment were in the same account as anything else,
which is why the account separation in `aws` is treated as a control rather
than an architectural convenience.
