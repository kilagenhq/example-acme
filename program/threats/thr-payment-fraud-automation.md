---
id: thr-payment-fraud-automation
type: threat
title: Automated Payment Fraud at the Checkout
description: 'Attackers run card testing, enumeration or credential stuffing against the hosted
  checkout and the payments API, using Acme''s merchants as a validation service for stolen
  cards.

  '
status: active
owner: role-security-eng
domains:
- grc
related:
- bp-payment-processing
- rsk-payment-fraud-at-checkout
systems:
- cloudflare
priority: 4
severity: medium
last_reviewed: '2026-07-15'
next_review: '2027-01-15'
---

# Automated Payment Fraud at the Checkout

## Threat scenario

An attacker with a list of stolen card numbers submits small authorisations
against a merchant's checkout to learn which cards are live. Acme sees a spike
in low-value declines; the merchant sees chargebacks and a scheme fine; the
cardholders see a charge they did not make.

The same infrastructure supports two related patterns: enumeration of valid
merchant identifiers through the API, and credential stuffing against merchant
portal accounts.

## Why Acme is exposed

- The hosted checkout is by design reachable by anyone with the link.
- Rate limits are per merchant, so a distributed attack across many merchants
  stays under each limit.
- Bot management is in challenge mode rather than block, after false positives
  from a merchant integration.

## Existing controls

| Control | Where |
|---|---|
| Per-merchant rate limiting on the payments API | cloudflare |
| Bot management on the checkout, challenge mode | cloudflare |
| Velocity detections on decline patterns | elastic-siem |
| Scheme-level fraud monitoring | Card scheme, outside this repository |

## Residual exposure

Detection is per merchant, so the cross-merchant pattern that characterises card
testing is only visible manually. Moving bot management to block has been
deferred twice, which is a business decision recorded as a risk rather than a
security gap.
