---
id: rsk-vulnerable-dependency-in-production
type: risk
title: Vulnerable Dependency Reaching Production
description: 'A third-party component with a known vulnerability runs in production long enough
  to be exploited, because it was missed, unscannable or left unpatched past its deadline.

  '
status: active
owner: role-appsec-eng
domains:
- grc
- appsec
related:
- std-secure-development
- std-vulnerability-management
- thr-supply-chain-compromise
systems:
- dependabot
- trivy
impact: high
likelihood: medium
severity: high
tracker: https://acme.atlassian.net/browse/SEC-233
treatment: mitigate
root_causes:
- unpatched-component
- third-party-failure
risk_category:
  principle: operational-risk
  category1: technology
  category2: software-vulnerability
last_reviewed: '2026-07-15'
next_review: '2026-10-15'
---

# Vulnerable Dependency Reaching Production

## Risk statement

Acme's services carry several hundred transitive dependencies. If one with a
known, exploitable vulnerability runs in production past its remediation
deadline, an attacker with a public exploit reaches the same environment that
processes payments.

## Assessment

| Dimension | Rating | Reasoning |
|---|---|---|
| Likelihood | Medium | Advisories arrive weekly; the deadline is occasionally missed |
| Impact | High | Code execution inside the platform, though not directly in the CDE |
| Severity | High | 3 × 4 = 12, per the matrix in `std-risk-framework` |
| Control effectiveness | Substantially | Scanning is continuous, upgrades are raised automatically, and the time to patch is measured against a deadline |

## Treatment

**Mitigate.** Continuous scanning, automatic upgrade pull requests, and a
measured mean time to patch of 9 days for critical findings against a 7-day
deadline — close, and not yet met.

| Action | Owner | Status |
|---|---|---|
| Bring the vendored portal library under a manifest | role-appsec-eng | Gap `gap-unmanaged-vendored-library` |
| Close the gap between 9 days and the 7-day critical deadline | role-appsec-eng | Monitored monthly |
| Produce a software bill of materials per release | role-appsec-eng | Backlog |

## Acceptance

The residual risk is accepted at `high` by the CISO between quarterly reviews.
A critical advisory affecting a component in the cardholder data environment is
handled as an incident, not as a patch cycle.
