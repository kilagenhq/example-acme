---
id: rb-offboard-user
type: runbook
title: Offboard a User
description: 'Revoke all access for a departing employee or contractor within the deadlines
  set by the access control standard, including the systems the identity provider does not reach.

  '
status: active
owner: role-it-manager
domains:
- iam
capabilities:
- iam.joiner-mover-leaver
related:
- exc-legacy-billing-sso
- pro-access-review
- std-access-control
systems:
- 1password
- crowdstrike-falcon
- okta
last_reviewed: '2026-07-10'
next_review: '2027-07-10'
---

# Offboard a User

## When to run

On departure. Trigger is the HR record, not a ticket. Deadlines from
`std-access-control` 1.4: within 24 hours of the leaving date, or within 4
hours where the departure is involuntary.

## Preconditions

- The HR record shows a leaving date.
- For an involuntary departure, HR has confirmed the exact time access must be
  removed. Run the steps before that time, not after.

## Steps

1. **Suspend the identity.** In `okta`, suspend rather than delete. Deletion
   removes the audit trail; suspension keeps it and blocks access immediately.

   ```text
   Okta → Directory → People → [user] → Suspend
   ```

2. **Revoke live sessions.** Suspension does not end an existing session. Clear
   all sessions and refresh tokens explicitly.
3. **Revoke the second factors.** Remove enrolled keys and passkeys so a
   re-enabled account cannot be reached with an old factor.
4. **Handle the vault.** In `1password`, remove the user and rotate any
   shared credential they could see. This step is skipped most often and is the
   one that matters most.
5. **Non-federated systems.** Work the list on the offboarding checklist — the
   legacy billing application under `exc-legacy-billing-sso`, the card scheme
   portal, and anything else marked non-federated in the system inventory.
6. **Devices.** Mark the device for return in `crowdstrike-falcon`, and
   remote-lock it if it is not returned within five working days.
7. **Transfer ownership.** Reassign any `da-*` or `bp-*` document
   naming the departing person's role as owner if they were the sole holder.
8. **Record.** Attach timestamps for steps 1 to 6 to the offboarding ticket.
   The evidence for `std-access-control` 1.4 is the gap between the HR date and
   these timestamps.

## Verification

- The identity provider shows the account suspended with no active sessions.
- A search for the user's email across federated applications returns no active
  account.
- Shared credentials the user could see have a rotation date after the
  departure date.

## If something goes wrong

If a non-federated system cannot be reached — the owner is away, the vendor
portal is down — suspend at the network or contractual level, record the
exposure in the ticket, and escalate to the CISO if it lasts more than 24
hours. Do not close the ticket with a step outstanding.
