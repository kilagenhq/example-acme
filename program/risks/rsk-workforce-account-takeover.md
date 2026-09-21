---
id: rsk-workforce-account-takeover
type: risk
title: Workforce Account Takeover
description: 'An attacker obtains a valid workforce session and uses it to reach production
  systems, merchant data or the identity provider itself.

  '
status: active
owner: role-ciso
domains:
- grc
- iam
related:
- inc-finance-credential-phishing
- std-access-control
- thr-credential-phishing
systems:
- elastic-siem
- okta
impact: critical
likelihood: high
severity: critical
tracker: https://acme.atlassian.net/browse/SEC-198
treatment: mitigate
root_causes:
- human-error
- targeted-attack
risk_category:
  principle: operational-risk
  category1: information-security
  category2: unauthorised-access
last_reviewed: '2026-07-15'
next_review: '2026-10-15'
---

# Workforce Account Takeover

## Risk statement

If an attacker obtains a valid workforce session — through phishing, a reused
password or a stolen device — then they can reach whatever that identity can
reach, which for an engineering or support account includes merchant data and,
for an administrative account, the identity provider itself.

## Assessment

| Dimension | Rating | Reasoning |
|---|---|---|
| Likelihood | High | Attempted regularly; one incident already occurred in 2026 |
| Impact | Critical | An administrative account reaches every federated system |
| Severity | Critical | 4 × 5 = 20, per the matrix in `std-risk-framework` |
| Control effectiveness | Substantially | Phishing-resistant MFA is in place; two legacy exceptions remain |

## Treatment

**Mitigate.** The controls are in place and working; the residual exposure is
the two applications still on password authentication and the push factors that
remain enabled for them.

| Action | Owner | Status |
|---|---|---|
| Migrate the legacy billing application to SAML | role-it-manager | In progress, `exc-legacy-billing-sso` expires 2026-12-31 |
| Remove push factors once the exception closes | role-it-manager | Blocked on the above |
| Add session anomaly detection beyond impossible travel | role-secops-analyst | Backlog |

## Acceptance

Residual risk after treatment is expected to fall to `high`. As a `critical`
risk it is reviewed quarterly by the security committee, and its acceptance
sits with the CTO under `std-risk-framework` 8.3.
