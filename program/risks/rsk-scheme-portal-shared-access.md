---
id: rsk-scheme-portal-shared-access
type: risk
title: Shared Access to the Card Scheme Portal
description: 'A single shared login to the card scheme portal means an action in the portal cannot
  be attributed to a person, and a leaver keeps access until the password changes.

  '
status: active
owner: role-it-manager
domains:
- grc
- iam
related:
- exc-shared-support-account
- gap-shared-scheme-portal-account
- std-access-control
systems:
- 1password
impact: medium
likelihood: low
severity: medium
treatment: mitigate
root_causes:
- process-not-followed
risk_category:
  principle: operational-risk
  category1: information-security
  category2: unauthorised-access
last_reviewed: '2026-07-02'
next_review: '2026-10-15'
---

# Shared Access to the Card Scheme Portal

## Why this was retired, and why it is open again

The scheme released per-user accounts for the portal in June 2026 and the
migration was recorded as done the same month. `exc-shared-support-account` was
withdrawn on 2026-06-30 on that basis, and this risk was retired on 2026-07-01
with the treatment `avoid`: the activity that created it was supposed to have
stopped existing.

It had not. The access review of 2026-07-02 found the shared login still in
use by the operations team — the per-user accounts had been issued but nobody
had moved to them, and revoking the exception had changed nothing on the
portal. That is `gap-shared-scheme-portal-account`, and it is still open.

The risk is active again, with `mitigate` rather than `avoid`, and it stays
that way until the gap closes on evidence rather than on an assurance.

## What this cost

A month of believing a control was in place that was not, and an exception
withdrawn while the deviation it covered was still happening. The lesson is in
the treatment: `avoid` is a claim that an activity stopped, and a claim about
the world needs the same evidence as any other — retiring the risk on the
migration being *planned* is what made the register wrong.
