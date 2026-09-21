---
id: rsk-payments-platform-outage
type: risk
title: Prolonged Payments Platform Outage
description: 'Payment processing is unavailable for longer than the recovery objective, through
  a destructive attack, a failed change or a dependency failure.

  '
status: active
owner: role-cto
domains:
- grc
- infra
related:
- bp-payment-processing
- std-incident-response
- thr-ransomware
systems:
- aws
impact: medium
likelihood: medium
severity: high
treatment: transfer
root_causes:
- software-defect
- process-not-followed
- capacity-limit
risk_category:
  principle: operational-risk
  category1: technology
  category2: system-failure
last_reviewed: '2026-07-15'
next_review: '2026-10-15'
---

# Prolonged Payments Platform Outage

## Risk statement

Merchants lose revenue for every minute Acme cannot process payments, and the
largest of them hold contractual recovery commitments. The risk is not that an
outage occurs — that is routine and handled — but that recovery takes longer
than the four-hour objective in `bp-payment-processing`.

## Assessment

| Dimension | Rating | Reasoning |
|---|---|---|
| Likelihood | Medium | Two outages over 30 minutes in the last year, neither near the objective |
| Impact | Medium | Contained merchant impact; a multi-hour outage would raise this |
| Severity | High | 3 × 3 = 9, per the matrix in `std-risk-framework` |
| Control effectiveness | Partially | Backups exist and are encrypted; full recovery is unproven |

## Treatment

**Mitigate.** The backups are real and the restore procedure is written; what
is missing is that nobody has run it end to end against the four-hour
objective, so the objective is a plan rather than a measurement.

| Action | Owner | Status |
|---|---|---|
| Full disaster recovery exercise against the four-hour objective | role-security-eng | Scheduled annually, `schedule.yml` |
| Document recovery objectives per system, not only per process | role-it-manager | Gap `gap-recovery-objectives-incomplete` |
| Restore test covering the payment database and the object store | role-security-eng | Partially done: database only |

## Acceptance

Accepted at `high` by the CTO until the recovery exercise demonstrates the
objective. The exercise result will re-score this risk either way, and that is
the point of scheduling it.
