---
id: std-incident-response
type: standard
title: Incident Response Standard
description: 'The severity scale, the roles, the notification deadlines and the learning loop
  that apply when something goes wrong.

  '
status: active
owner: role-ciso
domains:
- grc
- ir
- secops
related:
- pb-phishing-response
- pol-information-security
- std-logging-monitoring
approved_by:
- role-security-committee
requirements:
- ref: '7.1'
  text: A documented plan names the roles and the decision points
  how_demonstrated: The plan itself and named roles, from program/roles/, this repository.
  frameworks:
    iso_27001:
    - A.5.24
    pci_dss_4_0_1:
    - '12'
    soc2:
    - CC7.4
    nist_csf:
    - RS.MA
- ref: '7.2'
  text: Incidents are classified on the common severity scale and escalated accordingly
  how_demonstrated: Severity recorded on each incident, from inc-* documents.
  frameworks:
    iso_27001:
    - A.5.25
    soc2:
    - CC7.4
    nist_csf:
    - RS.MA
- ref: '7.3'
  text: Notification obligations are met within the regulatory deadlines
  how_demonstrated: Notification timestamps against awareness time, from inc-* documents.
  frameworks:
    iso_27001:
    - A.5.26
    pci_dss_4_0_1:
    - '12'
    soc2:
    - CC7.5
    nist_csf:
    - RS.CO
    iso_27018:
    - A.10.1
- ref: '7.4'
  text: Every incident rated high or above gets a postmortem with tracked actions
  how_demonstrated: Postmortems and closed action tickets, from inc-*, jira.
  frameworks:
    iso_27001:
    - A.5.27
    soc2:
    - CC4.2
    nist_csf:
    - ID.IM
    - RC.CO
- ref: '7.5'
  text: The plan is exercised at least annually
  how_demonstrated: Report of the annual exercise, naming the scenario, who took part, what it found and what changed afterwards.
  evidence:
  - name: Incident response exercise 2026 — report and actions
    url: https://drive.acme.example/security/ir/2026-05-tabletop-report.pdf
    collected: '2026-05-19'
    freshness: annually
    collector: manual
  frameworks:
    iso_27001:
    - A.5.24
    nist_csf:
    - ID.IM
version: '1.1'
capabilities:
- ir.incident-communications
- ir.incident-response-plan
- ir.on-call-management
- ir.tabletop-exercises
last_reviewed: '2026-06-02'
next_review: '2027-06-02'
---

# Incident Response Standard

## Purpose

An incident is the one moment when the program is tested in public. What is
written here is what will actually be done, because nothing else will be
invented at the time.

## Scope

Any event that compromises, or plausibly compromises, the confidentiality,
integrity or availability of Acme, merchant or cardholder data.

## Requirements

### Preparation

7.1 A documented incident response plan names the incident commander, the
communications lead, the technical lead and the legal contact, and states the
decision points at which each is engaged.

7.2 Incidents are classified using the severity scale in `std-risk-framework`.
Classification is provisional at declaration and revisited as facts arrive;
under-classification is corrected upward without ceremony.

| Severity | Example | Commander | Notification |
|---|---|---|---|
| Critical | Cardholder data confirmed exposed | CTO | Schemes, supervisory authority, merchants |
| High | Workforce account compromise with production access | CISO | Merchants if affected |
| Medium | Contained malware on a single endpoint | Analyst | Internal only |
| Low | Phishing email reported, no click | Analyst | Internal only |

### Response

7.3 Notification obligations are met within their deadlines: 72 hours to the
supervisory authority for a personal data breach, and immediately to the card
schemes on suspected cardholder data compromise. The clock starts at awareness,
not at confirmation.

### Learning

7.4 Every incident rated `high` or above gets a written postmortem recorded as
an `inc-*` document, blameless in tone, with actions tracked to closure in the
tracker. The document is immutable once published.

7.5 The plan is exercised at least annually. The exercise must include the
executive and legal participants, not only the security team — an exercise that
only tests the people who wrote the plan tests nothing.

## Revision History

| Version | Date | Approved by | Change |
|---|---|---|---|
| 1.0 | 2025-01-15 | Security Committee | Initial version |
| 1.1 | 2026-06-02 | Security Committee | Exercise participation widened beyond the security team |
