---
id: rsk-payment-fraud-at-checkout
type: risk
title: Automated Fraud Against Merchant Checkouts
description: 'Card testing and enumeration against Acme-hosted checkouts produce merchant chargebacks,
  scheme fines and a reputational cost Acme carries rather than the attacker.

  '
status: active
owner: role-security-eng
domains:
- grc
- appsec
related:
- bp-payment-processing
- thr-payment-fraud-automation
systems:
- cloudflare
impact: low
likelihood: medium
severity: medium
treatment: accept
root_causes:
- targeted-attack
- inadequate-monitoring
risk_category:
  principle: operational-risk
  category1: financial-crime
  category2: payment-fraud
last_reviewed: '2026-07-15'
next_review: '2026-10-15'
---

# Automated Fraud Against Merchant Checkouts

## Risk statement

Attackers use Acme's hosted checkout to validate stolen cards. The direct loss
sits with the issuer and the merchant, but the scheme monitoring, the merchant
complaints and the remediation work land on Acme.

## Assessment

| Dimension | Rating | Reasoning |
|---|---|---|
| Likelihood | Medium | Continuous background activity, occasionally organised |
| Impact | Low | Bounded by scheme rules; no Acme data is exposed |
| Severity | Medium | 3 × 2 = 6, per the matrix in `std-risk-framework` |
| Control effectiveness | Partially | Rate limits are per merchant; the cross-merchant pattern is not detected |

## Treatment

**Accept**, with monitoring. This is the one risk in the register that is
deliberately not being mitigated further, and it is worth showing as such: the
control that would reduce it — bot management in blocking mode — has twice
caused a merchant integration to fail, and the business has chosen the fraud
over the outage.

| Consideration | Position |
|---|---|
| Why not mitigate | Blocking mode broke a merchant integration twice |
| Why not transfer | Scheme rules already place the direct loss elsewhere |
| Compensating control | Velocity detections and per-merchant rate limits |
| Trigger to revisit | Any scheme monitoring notice, or a merchant escalation |

## Acceptance

Accepted at `medium` by the CISO under `std-risk-framework` 8.3, reviewed
quarterly. The acceptance is recorded here rather than in a meeting note
precisely because it will be questioned during the next audit.
