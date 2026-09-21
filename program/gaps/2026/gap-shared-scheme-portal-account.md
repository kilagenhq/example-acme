---
id: gap-shared-scheme-portal-account
type: gap
title: Shared login on the card scheme portal, exception expired and not renewed
description: The card scheme portal still has one shared login for six operators, three months after the exception covering it was revoked on the belief the migration was done.
owner: role-it-manager
requirement: std-access-control#1.1
source: internal
found: '2026-07-02'
severity: medium
tracker: https://acme.atlassian.net/browse/GRC-152
domains:
- iam
related:
- exc-shared-support-account
systems:
- 1password
---

# Shared login on the card scheme portal, exception expired and not renewed

## What is missing

`std-access-control` 1.1 prohibits shared credentials. The card scheme's
merchant portal issued per-user accounts in June 2026, and on that basis
`exc-shared-support-account` was revoked on 2026-06-30 and
`rsk-scheme-portal-shared-access` was retired the next day.

The access review of 2026-07-02 found the shared credential still in daily use
by the six-person payment operations team. The per-user accounts had been
issued and nobody had moved to them. Revoking the exception had changed nothing
on the portal — it had only removed the paperwork that acknowledged the
deviation.

So this gap is the deviation standing on its own: prohibited by the standard,
no longer covered by an exception, and still happening.

## Why it is still open

The migration needs each operator enrolled by the scheme's support desk, which
has a two-week turnaround per request, and it needs the shared credential
retired in the same window so nobody falls back to it. It has been started
twice and abandoned both times when a settlement issue took the team's
attention.

## What closes it

Six enrolled accounts, the shared credential deleted at the scheme rather than
merely rotated, and the 1Password entry removed. Nothing here closes on an
assurance that the migration is done — that is exactly what went wrong the first
time, and it is recorded in `rsk-scheme-portal-shared-access`.
