---
id: da-workforce-identity
type: data-asset
title: Workforce Identity Data
description: 'Employee and contractor identity records held in the identity provider: accounts,
  entitlements, authentication factors and device associations.

  '
status: active
owner: role-it-manager
domains:
- data-security
related:
- rsk-workforce-account-takeover
- std-access-control
systems:
- okta
retention_years: 1
retention_justification: 'Accounts are disabled on departure and deleted after twelve months,
  which covers the period in which an access review or an investigation might need to establish
  what a departed account could reach.

  '
pii: true
classification: confidential
last_reviewed: '2026-08-01'
next_review: '2027-08-01'
---

# Workforce Identity Data

## What it is

The authoritative record of who works at Acme and what they can reach: account,
group memberships, application assignments, enrolled authentication factors and
associated devices.

## Why availability is rated critical

If this data is unavailable, nobody can log in to anything — including the
tools needed to fix it. That is the reason for the break-glass path documented
on `okta` and for the four-hour recovery objective on it.

## Controls

Classification `confidential` under `std-data-protection-controls` 6.1.
Administrative access is separate accounts with hardware keys only; every
administrative action generates an alert under `std-logging-monitoring` 5.6.

## Retention and disposal

Disabled on departure within the deadlines in `std-access-control` 1.4, deleted
twelve months later. Authentication factor material is destroyed with the
account.

## Known issues

Two legacy applications hold local credentials that are not represented in this
asset at all, which is the deviation recorded in `exc-legacy-billing-sso`.
