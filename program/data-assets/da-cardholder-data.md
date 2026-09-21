---
id: da-cardholder-data
type: data-asset
title: Cardholder Data
description: 'Primary account numbers, expiry dates and transaction data processed on behalf
  of merchants. The most restricted asset Acme holds and the reason PCI DSS is in scope.

  '
status: active
owner: role-ciso
domains:
- data-security
related:
- bp-payment-processing
- pol-data-protection
- rsk-cardholder-data-exposure
- std-data-protection-controls
systems:
- aws
- aws-kms
retention_years: 1
retention_justification: 'Scheme rules require transaction records to support chargebacks and
  dispute resolution for 13 months. The primary account number itself is tokenised on capture
  and the original is not retained.

  '
pii: true
classification: restricted
last_reviewed: '2026-03-05'
next_review: '2027-03-05'
---

# Cardholder Data

## What it is

Payment card data processed for merchant transactions: the primary account
number, expiry date, cardholder name where supplied, and the transaction
record. Sensitive authentication data — the security code and full magnetic
stripe or chip data — is never stored after authorisation.

## Where it lives

| Location | Form | Notes |
|---|---|---|
| Tokenisation service | Encrypted, key held separately | The only system able to reverse a token |
| Payment database | Token plus last four digits | In the CDE account, no human access path |
| Transaction records | Token, amount, merchant, timestamp | Retained 13 months |
| Logs | Never | A card number in a log is a reportable event |

## Controls

Set by classification `restricted` under `std-data-protection-controls` 6.1:
encryption in transit and at rest, tokenisation, named-role access only, access
logged, never shared outside Acme.

## Retention and disposal

Transaction records are deleted after 13 months by an automated job. Tokens
whose transaction records have been deleted are purged in the same run.

## Known issues

Copies of production data in analytics environments would fall outside these
controls, and nothing currently detects them. That is the largest open question
against this asset.
