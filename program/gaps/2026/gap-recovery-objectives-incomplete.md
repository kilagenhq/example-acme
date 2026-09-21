---
id: gap-recovery-objectives-incomplete
type: gap
title: Recovery objectives are recorded per business process but not per system
description: Recovery objectives exist per business process but no system carries its own, so a restore cannot be sequenced and nobody owns a system's target.
owner: role-it-manager
requirement: std-asset-management#4.3
source: audit
found: '2026-05-06'
severity: medium
tracker: https://acme.atlassian.net/browse/GRC-140
domains:
- grc
related:
- rsk-payments-platform-outage
systems:
- aws
---

# Recovery objectives are recorded per business process but not per system

## What is missing

`bp-payment-processing` carries a four-hour recovery objective and
`bp-merchant-onboarding` carries one day. Neither decomposes into the systems
that would have to come back for those numbers to hold. `std-asset-management`
4.3 requires criticality, CIA ratings and recovery objectives for in-scope
systems, and the estate's inventory does not hold them.

Two things follow. A restore cannot be sequenced, because nothing says which
system has to be up before which. And no system has an owner accountable for a
recovery target, so the four hours in `bp-payment-processing` is a number the
process owner wrote about systems other people run.

## Why it is still open

It is unglamorous and it is cross-team: the objectives have to be agreed with
every system owner, and each agreement is a commitment to a restore time
somebody will be held to. Two rounds of the exercise have been scheduled and
displaced by incident work.

## What closes it

An RTO and RPO per in-scope system in the estate's inventory, derived from the
process objectives rather than asserted independently, and a restore sequence
that reconciles with them. `rsk-payments-platform-outage` carries the residual
risk until the sequence has been run end to end.
