---
id: exc-shared-support-account
type: exception
title: Shared Support Account on the Card Scheme Portal
description: 'A single shared login on the card scheme portal, which offers no per-user accounts,
  used by the payment operations team.

  '
owner: role-it-manager
domains:
- iam
related:
- std-access-control
systems:
- 1password
approved_by:
- role-ciso
compensating_controls:
- Credential held in 1Password, shared with the six named operators only
- Every use logged in the change record, reconciled weekly
- Scheme portal access is read-only for all but two operations
risk_severity: medium
expires: '2026-06-30'
revoked: '2026-06-30'
requirement: std-access-control#1.1
---

# Shared Support Account on the Card Scheme Portal

## Deviation

`std-access-control` 1.1 prohibits shared credentials. The card scheme's
merchant portal issues one login per member organisation and offers no per-user
accounts, so the payment operations team of six shares one credential.

## When it was granted

Granted 2026-01-05 by the CISO for six months, which is the limit `role-ciso`
carries. It ran to its full term.

## Status: lapsed and not renewed

`revoked: 2026-06-30` records that this exception stopped authorising anything
on its expiry date. It was not renewed. It is kept here
rather than deleted because the underlying condition has not changed — the
scheme still offers no per-user accounts — and an expired exception with a live
deviation behind it is exactly what an auditor should be able to find.

The choice now is to renew it with evidence that the scheme has been chased, or
to accept the risk formally. That decision sits with the security committee at
the next quarterly review, and until it is made this is a shortfall, tracked as
`gap-shared-scheme-portal-account`.

## Compensating controls

| Control | Detail |
|---|---|
| Credential storage | Held in the restricted vault in `1password` |
| Attribution | Vault access events identify who retrieved the credential and when |
| Rotation | Rotated on any change to the team, and at least quarterly |
| Scope | The portal holds no cardholder data; it is used for scheme reporting |

## Residual risk

`medium`. Attribution is indirect: the vault says who took the credential, not
what they did with it once inside the portal.
