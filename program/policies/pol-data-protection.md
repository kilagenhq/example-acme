---
id: pol-data-protection
type: policy
title: Data Protection Policy
description: 'How Acme classifies, protects, retains and disposes of personal and cardholder
  data, and the obligations that follow from processing it in the European Union and the United
  States.

  '
status: active
owner: role-ciso
domains:
- grc
related:
- da-cardholder-data
- da-merchant-pii
- pol-information-security
- std-asset-management
- std-data-protection-controls
approved_by:
- role-security-committee
version: '1.3'
last_reviewed: '2026-03-05'
next_review: '2027-03-05'
---

# Data Protection Policy

## Purpose

Acme holds two kinds of data that carry obligations beyond good practice:
cardholder data, governed by the card schemes, and personal data, governed by
law in the jurisdictions where Acme operates. This policy states the
principles; `std-data-protection-controls` states the controls.

## Scope

All personal and cardholder data processed by Acme, in any environment,
including copies held for analytics, testing or support.

## Principles

1. **Classify before protecting.** Every data asset carries one of four
   classifications — public, internal, confidential, restricted — and the
   controls follow from it.
2. **Collect the minimum.** A field that is not collected cannot be breached,
   mis-shared or subpoenaed.
3. **Do not store the primary account number where a token will do.** Full card
   numbers exist in one system, for one purpose, for as short a time as the
   scheme rules allow.
4. **Encrypt in transit and at rest, with keys held apart from the data.**
5. **Keep data only as long as there is a reason.** Every asset has a retention
   period and a justification for it, and disposal is as deliberate as
   collection.
6. **Non-production means non-production data.** Staging and analytics use
   synthetic or tokenised data.
7. **A personal data breach starts a clock.** Notification obligations are
   measured in hours; the incident process is built around that, not adapted to
   it afterwards.

## Roles

| Role | Responsibility |
|---|---|
| CISO | Owns this policy and the controls implementing it |
| GRC Analyst | Maintains the data asset inventory and retention schedule |
| System owners | Apply the controls their asset's classification requires |
| Legal | Owns the lawful basis, the notifications and the records of processing |

## Compliance

Acme is subject to the EU General Data Protection Regulation for its European
merchants and to US state privacy law for its US operations. Cardholder data is
additionally governed by PCI DSS. Where obligations differ, the strictest
applies.

## Review

Annually, and on any material change to what Acme collects or where it is
processed.

## Revision History

| Version | Date | Approved by | Change |
|---|---|---|---|
| 1.0 | 2024-06-11 | Security Committee | Initial version |
| 1.1 | 2025-01-20 | Security Committee | Added the non-production data principle |
| 1.2 | 2025-09-02 | Security Committee | Retention justification made mandatory per asset |
| 1.3 | 2026-03-05 | Security Committee | Aligned with PCI DSS v4.0 tokenisation requirements |
