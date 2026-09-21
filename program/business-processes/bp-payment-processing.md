---
id: bp-payment-processing
type: business-process
title: Payment Processing
description: 'Authorising, capturing and settling card payments on behalf of merchants — the
  process Acme exists to run, and the one every recovery objective is set against.

  '
status: active
owner: role-cto
domains:
- grc
related:
- da-cardholder-data
- rsk-cardholder-data-exposure
- rsk-payments-platform-outage
- std-data-protection-controls
systems:
- aws
- aws-kms
- cloudflare
business_function: Payments Operations
rto: 4h
criticality: critical
last_reviewed: '2026-04-20'
next_review: '2027-04-20'
---

# Payment Processing

## What the process does

A cardholder pays a merchant through Acme's hosted checkout or the merchant's
own integration against the payments API. Acme authorises the payment with the
scheme, captures it, and settles funds to the merchant on the agreed cycle.

## Business impact analysis

| Dimension | Assessment |
|---|---|
| Criticality | Critical — it is the product |
| Recovery time objective | 4 hours |
| Recovery point objective | 15 minutes |
| Maximum tolerable outage | 8 hours before contractual penalties with tier-one merchants |
| Peak dependency | End of month, when merchant settlement volume triples |
| Customer facing | Yes — cardholders see failures directly at checkout |

## Systems this process depends on

| System | Role | Failure effect |
|---|---|---|
| `cloudflare` | Edge, TLS, WAF | Checkout unreachable |
| `aws` | Compute, payment database | Processing stops |
| `aws-kms` | Keys for tokenisation | Tokens cannot be resolved; capture stops |
| Card scheme | External authorisation | Degraded to store-and-forward where the scheme allows |

## Continuity position

The recovery objective is four hours. It has not been demonstrated end to end:
the annual exercise has tested the restore of one database, not the full path
from a destroyed environment to a processing platform. This is recorded as
`rsk-payments-platform-outage`, and it is the weakest part of this process's
control set.
