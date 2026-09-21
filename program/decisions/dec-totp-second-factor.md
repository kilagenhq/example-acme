---
id: dec-totp-second-factor
type: decision
title: Use TOTP as the Standard Second Factor
description: 'Decision to standardise on time-based one-time passwords for workforce multi-factor
  authentication. Superseded in 2026 by the move to phishing-resistant factors.

  '
status: retired
owner: role-it-manager
domains:
- iam
related:
- dec-phishing-resistant-authentication
- std-access-control
systems:
- okta
decided: '2024-02-08'
immutable: true
---

# Use TOTP as the Standard Second Factor

## Status

Superseded by `dec-phishing-resistant-authentication` on 2026-01-20. Kept
because the reasoning below explains why Acme spent two years with a control
that later proved insufficient, and because the record of a decision is not
improved by deleting it.

## Context

Acme was 40 people with no MFA on most applications. The identity provider had
just been introduced and the priority was coverage: getting every account onto
a second factor at all.

The options were TOTP applications, SMS codes, push notifications, and hardware
security keys.

## Decision

Standardise on TOTP, with push notifications permitted for applications that do
not support it. SMS is not accepted.

## Consequences

**Positive.** Coverage reached 100% within six weeks. No hardware to buy, ship
or replace for a remote-first workforce spread across two continents. No
dependency on the phone network.

**Negative.** TOTP and push are both phishable in real time by a proxy, and
push introduces prompt fatigue as an attack. Accepted at the time as a large
improvement over no second factor, with the note that it would need revisiting.

**Later.** It was revisited after `inc-finance-credential-phishing`, in
which exactly the anticipated attack occurred.
