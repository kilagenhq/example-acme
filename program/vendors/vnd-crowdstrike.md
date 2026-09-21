---
id: vnd-crowdstrike
type: vendor
title: CrowdStrike — Vendor Profile
description: 'Risk profile for the endpoint detection supplier, which holds a kernel-level agent
  on every managed device and telemetry describing what those devices do.

  '
status: active
owner: role-grc-analyst
domains:
- grc
related:
- std-third-party-risk
systems:
- crowdstrike-falcon
data_scope:
- Endpoint telemetry from workforce laptops and production hosts
- Process, file and network metadata; no document contents
- Incidental PII in file paths and usernames
vendor_name: CrowdStrike
certifications:
- name: ISO/IEC 27001
  verified: '2026-01-09'
  url: https://drive.acme.example/vendors/crowdstrike/iso-27001-certificate.pdf
- name: SOC 2 Type II
  verified: '2026-01-09'
tier: important
criticality: high
cia:
  confidentiality: high
  integrity: high
  availability: high
rto: 8h
rpo: 24h
last_reviewed: '2026-05-14'
next_review: '2027-05-14'
---

# CrowdStrike — Vendor Profile

## Why this vendor is important tier

The agent runs with the highest privilege available on every managed endpoint,
and a faulty update reaches the whole fleet at once. The risk here is less
about data than about availability and integrity of Acme's devices.

## Data and access

| Question | Answer |
|---|---|
| Personal data held | Device and user identifiers, process and network telemetry |
| Cardholder data held | None |
| Privileged access to Acme systems | Kernel-level agent on managed endpoints |
| Data location | EU region |
| Retention | 90 days of telemetry under the current plan |

## Assessment

| Item | Result | Date |
|---|---|---|
| SOC 2 Type II report | Reviewed, no relevant exceptions | 2026-05-14 |
| ISO 27001 certificate | Current | 2026-05-14 |
| Update rollout controls | N-1 sensor ring configured on the Acme side | 2026-05-14 |
| Breach notification clause | 48 hours, contractual | 2025-08-19 |

## Concentration and exit

Migration to another endpoint supplier is feasible within a quarter and has a
documented path. The more immediate control is the N-1 release ring: Acme does
not take sensor updates on the day they ship, which trades a short window of
lower coverage for protection against a bad update reaching every device.

## Next review

Annually, per `std-third-party-risk` 9.4.
