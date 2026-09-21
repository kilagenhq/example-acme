---
id: std-risk-framework
type: standard
title: Risk Framework Standard
description: 'The single scale on which Acme scores information security risk: likelihood, impact,
  the criticality matrix they produce, and the treatment and acceptance rules that follow from
  the result.

  '
status: active
owner: role-ciso
domains:
- grc
related:
- pol-information-security
approved_by:
- role-security-committee
requirements:
- ref: '8.1'
  text: Every information security risk is recorded in the register with an owner
  how_demonstrated: The risk register itself, from program/risks/.
  frameworks:
    nist_csf:
    - ID.RA
    soc2:
    - CC3.1
- ref: '8.2'
  text: Risks are scored on the common likelihood and impact scales
  how_demonstrated: Likelihood and impact on every risk, recorded in the document’s own frontmatter.
  frameworks:
    nist_csf:
    - ID.RA
    soc2:
    - CC3.2
- ref: '8.3'
  text: Treatment is decided and acceptance is made by the authorised role
  how_demonstrated: Treatment and owner on every risk, recorded in the document’s own frontmatter.
  frameworks:
    nist_csf:
    - GV.RM
    soc2:
    - CC3.4
    - CC9.1
- ref: '8.4'
  text: The register is reviewed quarterly by the security committee
  how_demonstrated: Minutes of the quarterly security committee, showing the register as reviewed and the decisions taken.
  evidence:
  - name: Security committee minutes — Q3 2026
    url: https://drive.acme.example/security/grc/2026-Q3-committee-minutes.pdf
    collected: '2026-08-20'
    freshness: quarterly
    collector: quarter-end
  frameworks:
    nist_csf:
    - GV.OV
    soc2:
    - CC4.1
- ref: '8.5'
  text: Severity is derived from the matrix and never set by hand
  how_demonstrated: CI validation of severity against the matrix, from the pipeline run on every pull request.
version: '1.2'
capabilities:
- grc.compliance-management
- grc.risk-management
last_reviewed: '2026-02-20'
next_review: '2027-02-20'
---

# Risk Framework Standard

## Purpose

One scale, used by everyone. Without it, "high risk" means whatever the person
saying it wants it to mean, and the register cannot be sorted, compared or
defended.

## Scope

All information security risks recorded as `rsk-*`. The same severity scale is
inherited by gaps, threats, vendor tiers and incidents, so that a `high` means
the same thing wherever it appears in this repository.

## Requirements

### Register

8.1 Every information security risk is recorded in `program/risks/` with a named
owner, a risk category from `risk-taxonomy.yml`, and at least one root cause.

8.2 Risks are scored on the likelihood and impact scales below. Both are
mandatory; an unscored risk is not a risk, it is a note.

### Treatment

8.3 Every risk carries a treatment decision — `mitigate`, `avoid`, `transfer`
or `accept`. Acceptance of a `high` or `critical` risk is made by the CTO;
`medium` and below by the CISO. The decision is recorded on the risk, not in a
meeting note.

8.4 The register is reviewed by the security committee quarterly, and any risk
whose score has changed is re-scored at that review.

8.5 Severity is the product of likelihood and impact read off the matrix below.
It is never set by hand, and CI rejects a risk whose severity does not match
its own scores.

## Likelihood scale

| Level | Name | Meaning |
|---|---|---|
| 5 | Critical | Expected within the year; already seen at peers |
| 4 | High | More likely than not within two years |
| 3 | Medium | Plausible within three years |
| 2 | Low | Possible but not expected |
| 1 | Negligible | Would require an unusual combination of failures |

## Impact scale

| Level | Name | Meaning for Acme |
|---|---|---|
| 5 | Critical | Loss of the payment licence, or a breach of cardholder data at scale |
| 4 | High | Regulatory notification, material merchant loss, or platform outage over 4 hours |
| 3 | Medium | Contained incident with merchant impact and a customer-visible degradation |
| 2 | Low | Internal disruption, no merchant impact |
| 1 | Negligible | Absorbed by normal operations |

## Criticality matrix

Severity is likelihood multiplied by impact, banded as follows:
negligible = 1, low = 2, medium = 3-7, high = 8-14, critical = 15-25.

| Likelihood / Impact | 1 Negligible | 2 Low | 3 Medium | 4 High | 5 Critical |
|---|---|---|---|---|---|
| **5 Critical (Highly likely)** | 5 Medium | 10 High | 15 Critical | 20 Critical | 25 Critical |
| **4 High (Likely)** | 4 Medium | 8 High | 12 High | 16 Critical | 20 Critical |
| **3 Medium (Possible)** | 3 Medium | 6 Medium | 9 High | 12 High | 15 Critical |
| **2 Low (Unlikely)** | 2 Low | 4 Medium | 6 Medium | 8 High | 10 High |
| **1 Negligible (Rare)** | 1 Negligible | 2 Low | 3 Medium | 4 Medium | 5 Medium |

## Control effectiveness

Recorded on each risk to explain the distance between inherent and residual
exposure: `fully`, `substantially`, `partially`, `largely-ineffective`, `none`,
`not-evaluated`. A control claimed as `fully` effective needs evidence; the
default for anything untested is `not-evaluated`.

## Revision History

| Version | Date | Approved by | Change |
|---|---|---|---|
| 1.0 | 2024-04-18 | Security Committee | Initial version |
| 1.1 | 2025-05-30 | Security Committee | Added control effectiveness vocabulary |
| 1.2 | 2026-02-20 | Security Committee | Severity derived from the matrix and enforced in CI |
