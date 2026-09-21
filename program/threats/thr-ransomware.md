---
id: thr-ransomware
type: threat
title: Ransomware and Destructive Attack
description: 'An attacker encrypts or destroys Acme systems and data, halting payment processing
  and forcing a recovery from backups.

  '
status: active
owner: role-security-eng
domains:
- grc
related:
- rsk-payments-platform-outage
systems:
- aws
- crowdstrike-falcon
priority: 3
severity: high
last_reviewed: '2026-07-15'
next_review: '2027-01-15'
---

# Ransomware and Destructive Attack

## Threat scenario

Initial access through a phished credential or an exposed service, followed by
privilege escalation and lateral movement, ending in mass encryption or
deletion. For a cloud-native platform the destructive step is less likely to be
file encryption than deletion of storage, snapshots and account access — the
modern version of the same attack.

## Why Acme is exposed

- Backups live in the same cloud provider as the data, though in a separate
  account with separate credentials.
- Restore has been tested against one database, not against the full recovery
  objective for payment processing.
- Endpoint coverage is 243 of 248 devices; five are outside it.

## Existing controls

| Control | Where |
|---|---|
| Endpoint detection with prevention enforced | crowdstrike-falcon |
| Cross-region encrypted backups in a separate account | aws, `std-data-protection-controls` |
| Write-once log retention that survives account compromise | `std-logging-monitoring` 5.3 |
| Immutable infrastructure — production is rebuilt, not repaired | `dec-immutable-production-infrastructure` |

## Residual exposure

Business continuity is the weakest link in this chain. The recovery objective
in `bp-payment-processing` is four hours and has never been demonstrated end to
end; that distance is the single largest piece of residual exposure Acme
carries against this threat.
