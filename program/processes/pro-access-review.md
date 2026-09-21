---
id: pro-access-review
type: process
title: Access Certification Process
description: 'How Acme runs the periodic certification of who holds access to which system,
  what the reviewer must confirm, and what happens to entitlements nobody confirms.

  '
status: active
owner: role-grc-analyst
domains:
- iam
capabilities:
- iam.access-reviews
related:
- rb-offboard-user
- std-access-control
systems:
- jira
- okta
last_reviewed: '2026-07-10'
next_review: '2027-07-10'
---

# Access Certification Process

## Purpose

`std-access-control` 1.5 requires system owners to certify who holds access to
their system. This process is how that happens without becoming a rubber stamp.

## Cadence

| Scope | Frequency | Owner |
|---|---|---|
| Systems in the cardholder data environment | Quarterly | System owner |
| Systems rated high or above | Quarterly | System owner |
| All other systems | Annually | System owner |
| Administrative accounts, all systems | Quarterly | CISO |

## Steps

1. **Prepare (GRC Analyst).** Export current entitlements per system from the
   identity provider. Where a system is not federated, request the export from
   its owner and record that it was manual.
2. **Distribute.** Open one ticket per system owner with the entitlement list
   attached and a two-week deadline.
3. **Review (System owner).** For each entitlement, confirm, reduce or remove.
   Confirming requires a reason that is not "they still work here" — the test
   is whether the person would be granted this access today if they asked.
4. **Escalate.** Deadlines missed by more than a week are escalated to the
   owner's manager and, at two weeks, to the CISO.
5. **Act (IT Manager).** Removals are applied within five working days.
   Reductions are applied in the same window.
6. **Evidence (GRC Analyst).** Attach the completed list, the changes applied
   and the dates to the certification record. This is what the auditor reads.
7. **Close.** Entitlements not confirmed by the deadline are removed, not
   carried forward.

## What makes this fail

The failure mode is not that reviewers refuse; it is that they confirm
everything in one click. Two countermeasures are built into step 3: the list
shows when each entitlement was last used, and any entitlement unused for 90
days must be justified individually.

## Revision History

| Date | Change |
|---|---|
| 2025-02-11 | Initial version |
| 2025-09-30 | Added last-used data to the review pack |
| 2026-07-10 | Unconfirmed entitlements are now removed rather than carried forward |
