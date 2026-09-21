---
id: role-secops-analyst
type: role
title: Security Operations Analyst
description: 'Runs detection and response: the SIEM, the detection rules, alert triage and the
  first hour of every incident.

  '
status: active
owner: role-ciso
domains:
- secops
reports_to: role-ciso
role_type: individual
last_reviewed: '2026-01-01'
next_review: '2027-01-01'
---

# Security Operations Analyst

The role on the other end of the alert.

## Responsibilities

- Triage alerts within the response times set by `std-logging-monitoring`.
- Write and tune detection rules, and retire the ones that only ever fire falsely.
- Keep log sources onboarded and prove they are still arriving.
- Run the incident playbooks in `program/playbooks/` and write the postmortem.

## Authority

- Declares an incident and its initial severity.
- Escalates to the CISO as incident commander when the severity reaches `high`.
