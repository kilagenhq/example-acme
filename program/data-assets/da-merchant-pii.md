---
id: da-merchant-pii
type: data-asset
title: Merchant and Contact Personal Data
description: 'Identity, contact and onboarding data for merchants and their named representatives,
  including the due diligence records collected at onboarding.

  '
status: active
owner: role-grc-analyst
domains:
- data-security
related:
- bp-merchant-onboarding
- pol-data-protection
- std-data-protection-controls
systems:
- aws
- google-workspace
retention_years: 6
retention_justification: 'Anti-money-laundering rules require customer due diligence records
  to be kept for five years after the relationship ends; six is the internal figure to cover
  the year in which the relationship closes.

  '
pii: true
classification: confidential
last_reviewed: '2026-03-05'
next_review: '2027-03-05'
---

# Merchant and Contact Personal Data

## What it is

Everything Acme holds about the businesses it serves and the people who run
them: company details, beneficial ownership, identity documents collected
during onboarding, bank details for settlement, and the contact records used by
support and sales.

## Where it lives

| Location | Form | Notes |
|---|---|---|
| Merchant database | Structured, encrypted at rest | Primary record |
| Onboarding document store | Identity documents, encrypted | Access restricted to compliance |
| Corporate email and drive | Copies in correspondence | The weakest point; DLP covers email only |
| Support tooling | Contact records | Synchronised, not authoritative |

## Controls

Classification `confidential`: encryption in transit and at rest, role-based
access reviewed quarterly, sharing outside Acme under contract only.

## Retention and disposal

Six years after the merchant relationship ends. Deletion is a scheduled manual
task rather than an automated job, which is the retention gap recorded against
`std-data-protection-controls` 6.5.

## Known issues

Identity documents reach the compliance team by email before they reach the
document store, so copies exist in mailboxes with no retention rule. Drive
retention is unbounded, which conflicts with the six-year period stated here.
