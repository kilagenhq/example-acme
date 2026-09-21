---
id: thr-supply-chain-compromise
type: threat
title: Software Supply Chain Compromise
description: 'A malicious or vulnerable third-party dependency, build action or supplier integration
  reaches Acme production and gives an attacker code execution or data access.

  '
status: active
owner: role-appsec-eng
domains:
- grc
related:
- rsk-cardholder-data-exposure
- rsk-vulnerable-dependency-in-production
- tm-payments-api
systems:
- dependabot
- github-advanced-security
- trivy
priority: 2
severity: high
last_reviewed: '2026-07-15'
next_review: '2027-01-15'
---

# Software Supply Chain Compromise

## Threat scenario

Three variants, in decreasing likelihood and increasing impact:

1. **A known vulnerable dependency reaches production** and is exploited before
   it is patched. This is the everyday case, and the reason dependency
   scanning is the most heavily invested AppSec control Acme runs.
2. **A package is taken over upstream** — through a maintainer account
   compromise or a typosquatted name — and ships malicious code that the
   pipeline installs and runs.
3. **A supplier with an integration into Acme** is compromised, and their
   access is used as a route in.

## Why Acme is exposed

- Several hundred transitive dependencies across the platform services.
- Build runners hold credentials to publish images and, in one pipeline, to
  deploy them.
- Third-party JavaScript on the merchant portal executes in the same page as
  the merchant's session.

## Existing controls

| Control | Where |
|---|---|
| Continuous dependency scanning with patch deadlines | dependabot, `std-vulnerability-management` 3.1 |
| Container and IaC scanning before publication | trivy, `std-secure-development` 2.5 |
| Pinned build actions and reviewed pipeline changes | `std-secure-development` 2.1 |
| Supplier tiering and review before access | `std-third-party-risk` |

## Residual exposure

One vendored JavaScript library in the merchant portal is outside every
manifest and therefore outside dependency scanning. Build runner permissions
have not been reduced to least privilege, and no software bill of materials is
produced for releases.
