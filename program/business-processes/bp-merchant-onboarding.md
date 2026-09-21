---
id: bp-merchant-onboarding
type: business-process
title: Merchant Onboarding
description: 'Taking a new merchant from application to live processing: due diligence, risk
  scoring, account creation and integration.

  '
status: active
owner: role-cto
domains:
- grc
related:
- da-merchant-pii
- std-data-protection-controls
systems:
- google-workspace
- jira
business_function: Commercial Operations
rto: 48h
criticality: medium
last_reviewed: '2026-04-20'
next_review: '2027-04-20'
---

# Merchant Onboarding

## What the process does

A prospective merchant applies, Acme performs customer due diligence, scores
the business for fraud and credit risk, creates the account and supports the
integration until the first live transaction.

## Business impact analysis

| Dimension | Assessment |
|---|---|
| Criticality | Medium — revenue-affecting, not revenue-stopping |
| Recovery time objective | 48 hours |
| Recovery point objective | 24 hours |
| Maximum tolerable outage | One week before the commercial pipeline is materially affected |
| Customer facing | Yes, but only for merchants in flight |

## Why it matters to security

This process collects the most sensitive personal data Acme holds outside
cardholder data: identity documents and beneficial ownership records. It also
collects them through the least controlled channel — email — before they reach
the document store.

| Concern | Position |
|---|---|
| Documents arriving by email | Copies persist in mailboxes with no retention rule |
| Manual review steps | Due diligence decisions are recorded in the tracker, not in a system of record |
| Data minimisation | Documents are kept in full where an extract would do |

## Continuity position

A 48-hour objective is comfortably met by the existing backup schedule.
Onboarding can also be run manually for a small number of merchants, which is
what makes this process tolerant of an outage in a way payment processing is
not.
