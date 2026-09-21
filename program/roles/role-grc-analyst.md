---
id: role-grc-analyst
type: role
title: GRC Analyst
description: 'Keeps the governance layer honest: evidence for audits, the gap register, vendor
  reviews, access reviews and the compliance calendar.

  '
status: active
owner: role-ciso
domains:
- grc
reports_to: role-ciso
role_type: individual
last_reviewed: '2026-01-01'
next_review: '2027-01-01'
---

# GRC Analyst

The role that turns what the program does into what an auditor can check.

## Responsibilities

- Collect evidence for the ISO 27001 surveillance audit and the SOC 2 examination.
- Maintain the gap register in `program/gaps/`: every open gap has an owner, a tracker and a found date.
- Run vendor security reviews and keep `program/vendors/` current.
- Coordinate the activities in `schedule.yml` and chase the overdue ones.

## Authority

- Opens a gap against any requirement without needing the owner's agreement.
- Blocks a vendor from processing cardholder data until the review is done.
