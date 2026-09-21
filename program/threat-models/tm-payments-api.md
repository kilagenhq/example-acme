---
id: tm-payments-api
type: threat-model
title: Threat Model — Payments API
description: 'STRIDE analysis of the public payments API: the authorisation path, the tokenisation
  boundary and the trust assumptions between Acme and its merchants.

  '
status: active
owner: role-appsec-eng
domains:
- appsec
capabilities:
- appsec.threat-modeling
related:
- da-cardholder-data
- gl-secure-coding
- std-data-protection-controls
- std-secure-development
- thr-supply-chain-compromise
systems:
- aws
- aws-kms
- cloudflare
methodology: stride
scope: The public payments API — merchant authentication, the authorisation and capture endpoints, and the tokenisation boundary into the cardholder data environment.
last_reviewed: '2026-07-30'
next_review: '2027-01-30'
---

# Threat Model — Payments API

## Scope

The public payments API: authentication of merchant integrations, the
authorisation and capture endpoints, and the tokenisation boundary between the
API and the cardholder data environment. The hosted checkout is modelled
separately in `tm-merchant-portal`.

## Data flow

```text
Merchant server ──(1) API key over TLS──▶ Edge (WAF, rate limit)
                                            │
                                     (2) authenticated request
                                            ▼
                                   Payments API service
                                     │              │
                          (3) tokenise│              │(4) authorise
                                     ▼              ▼
                          Tokenisation service   Card scheme
                            (CDE account)         (external)
                                     │
                             (5) token + last four
                                     ▼
                             Payment database
```

Trust boundaries: between the merchant and the edge (1), between the API
service and the cardholder data environment (3), and between Acme and the card
scheme (4).

## STRIDE

| Threat | Where | Assessment | Control |
|---|---|---|---|
| **Spoofing** | (1) Merchant identity | API key alone identifies the merchant | Keys are per environment, rotatable, and bound to an IP allowlist for tier-one merchants. Weak for smaller merchants who cannot allowlist. |
| **Tampering** | (2) Request in flight | Low — TLS 1.2 minimum enforced at the edge | `std-data-protection-controls` 6.2 |
| **Repudiation** | (4) Disputed authorisation | Merchant claims a payment was not requested | Every request logged with merchant, key id and timestamp; 13-month retention |
| **Information disclosure** | (5) Card data at rest | The principal risk in the model | Tokenised on capture; only the tokenisation service can reverse it; keys in a separate account |
| **Denial of service** | (1) Volumetric or targeted | Present and routine | Edge DDoS mitigation, per-merchant rate limits. Cross-merchant patterns are not detected — see `thr-payment-fraud-automation` |
| **Elevation of privilege** | (2) Merchant reaching another merchant's data | The highest-severity design concern | Authorisation checked at the resource on every request, per `gl-secure-coding`. Nothing tests it automatically — `gap-no-api-authorisation-testing` |

## Findings

| Finding | Severity | Disposition |
|---|---|---|
| No automated authorisation testing against the API | High | Gap `gap-no-api-authorisation-testing` |
| API keys are long-lived for merchants who cannot rotate automatically | Medium | Accepted; rotation reminder at 12 months |
| The API is out of scope for the bug bounty | Medium | Deliberate — no capacity to triage findings against it yet |

## Assumptions

- The card scheme connection is trusted and out of Acme's control.
- Merchant servers are not trusted: every input is validated as hostile.
- The tokenisation service is the only path into the cardholder data
  environment, and that assumption is tested annually by the segmentation test.

## Review trigger

Any change to the authorisation model, the tokenisation boundary, or the
addition of a new endpoint that accepts card data.
