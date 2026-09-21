---
id: rsk-cardholder-data-exposure
type: risk
title: Cardholder Data Exposure
description: 'Cardholder data is disclosed to an unauthorised party through a compromise of
  the cardholder data environment, a supplier, or a copy of production data outside it.

  '
status: active
owner: role-ciso
domains:
- grc
- data-security
related:
- bp-payment-processing
- da-cardholder-data
- std-data-protection-controls
- thr-supply-chain-compromise
systems:
- aws
- aws-kms
- cloudflare
impact: critical
likelihood: low
severity: high
tracker: https://acme.atlassian.net/browse/SEC-104
treatment: mitigate
root_causes:
- misconfiguration
- third-party-failure
- human-error
risk_category:
  principle: operational-risk
  category1: information-security
  category2: data-breach
last_reviewed: '2026-07-15'
next_review: '2026-10-15'
---

# Cardholder Data Exposure

## Risk statement

If cardholder data were disclosed, Acme would face scheme fines, mandatory
forensic investigation, merchant loss and, in the worst case, withdrawal of its
ability to process payments. It is the risk with the highest impact rating in
the register and, deliberately, one of the most heavily controlled.

## Assessment

| Dimension | Rating | Reasoning |
|---|---|---|
| Likelihood | Low | Segmented environment, tokenised storage, no human access path |
| Impact | Critical | Loss of the ability to process payments is an existential outcome |
| Severity | High | 2 × 5 = 10, per the matrix in `std-risk-framework` |
| Control effectiveness | Substantially | Strong at the boundary; weaker on copies leaving it |

## Treatment

**Mitigate.** The primary account number is tokenised, the environment is
segmented into its own account, and keys are held separately. The exposure that
remains is not the front door but the side: production data copied into
analytics or staging, which no tooling currently detects.

| Action | Owner | Status |
|---|---|---|
| Data security posture management to find copies outside the CDE | role-security-eng | Nothing does this today; funded for next year |
| Extend DLP beyond outbound email | role-it-manager | Gap `gap-dlp-coverage-partial` |
| Annual segmentation test by the penetration testing supplier | role-ciso | Scheduled, `schedule.yml` |

## Acceptance

Reviewed quarterly. Any change to what the platform stores, or to the
tokenisation design, triggers a re-score outside the cycle.
