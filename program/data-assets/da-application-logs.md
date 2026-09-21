---
id: da-application-logs
type: data-asset
title: Application and Security Logs
description: 'The event record across the platform, cloud, identity provider and edge — the
  evidence base for every investigation and most compliance claims.

  '
status: active
owner: role-secops-analyst
domains:
- data-security
related:
- std-logging-monitoring
systems:
- aws
- elastic-siem
retention_years: 2
retention_justification: 'PCI DSS requires twelve months with three immediately available. Acme
  keeps thirteen months hot and twenty-five in archive so that an investigation starting late
  still has the period before the incident.

  '
pii: true
classification: internal
last_reviewed: '2026-06-02'
next_review: '2027-06-02'
---

# Application and Security Logs

## What it is

Authentication events, cloud API calls, edge requests, endpoint detections,
application events and build activity. Personal data is present incidentally —
user identifiers, IP addresses — which is why this asset is marked as
containing PII despite being classified `internal`.

## Why integrity is rated critical

Confidentiality here is `medium`: most of this data would be uninteresting to
an attacker. Integrity is `critical`, because the entire value of the asset is
that it can be trusted. An attacker who can edit or delete the record defeats
every investigation that would otherwise follow, which is why
`std-logging-monitoring` 5.3 puts the archive in a separate account with
write-once retention.

## Where it lives

| Location | Form | Retention |
|---|---|---|
| SIEM hot storage | Indexed, searchable | 13 months |
| Log archive account | Compressed, write-once | 25 months |
| Source systems | Native retention | Varies, shorter |

## Known issues

The merchant portal's application logs are not onboarded, so one of the seven
required source families is missing. Tracked as `gap-portal-logs-not-onboarded`.
