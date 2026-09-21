---
id: std-third-party-risk
type: standard
title: Third-Party Risk Standard
description: 'How Acme assesses a supplier before it touches company or merchant data, what
  it requires contractually, and how often the assessment is repeated.

  '
status: draft
owner: role-grc-analyst
domains:
- grc
related:
- pol-information-security
- std-asset-management
- vnd-crowdstrike
- vnd-okta
approved_by:
- role-ciso
requirements:
- ref: '9.1'
  text: Suppliers are tiered by the data and access they hold
  how_demonstrated: Tier recorded on each vendor profile, from program/vendors/.
  frameworks:
    iso_27001:
    - A.5.19
    - A.5.21
    soc2:
    - CC9.2
    nist_csf:
    - GV.SC
- ref: '9.2'
  text: A security review is completed before a supplier receives data
  how_demonstrated: Completed reviews and reviewed attestations, from program/vendors/, jira.
  frameworks:
    iso_27001:
    - A.5.19
    pci_dss_4_0_1:
    - '12'
    soc2:
    - CC9.2
    nist_csf:
    - GV.SC
- ref: '9.3'
  text: Contracts carry security, breach notification and audit clauses
  how_demonstrated: Contract clauses, from the legal repository, referenced from the vendor profile.
  frameworks:
    iso_27001:
    - A.5.20
    pci_dss_4_0_1:
    - '12'
    nist_csf:
    - GV.SC
    iso_27017:
    - CLD.6.3.1
    iso_27018:
    - A.11.11
    - A.11.12
- ref: '9.4'
  text: Critical and important suppliers are reassessed annually
  how_demonstrated: Reassessment tracker for critical and important suppliers, with the date each was last assessed and when it is next due.
  evidence:
  - name: Supplier reassessment tracker — 2026
    url: https://drive.acme.example/security/tprm/2026-supplier-reassessment.csv
    collected: '2026-06-30'
    freshness: annually
    collector: manual
  frameworks:
    iso_27001:
    - A.5.22
    nist_csf:
    - GV.SC
version: '0.3'
capabilities:
- grc.vendor-risk-management
last_reviewed: '2026-08-20'
next_review: '2027-02-20'
---

# Third-Party Risk Standard

## Purpose

Acme's largest suppliers hold its identities, its endpoints and its data. This
standard is `draft` on purpose: the requirements are agreed and being followed,
but the standard has not yet been through the security committee, which is the
honest state of a document in flight.

## Why this is still a draft

`pol-information-security` has the security committee approve a standard. This
one is approved by the CISO alone and carries `status: draft` because the
tiering in 9.1 has not been applied to the whole supplier list yet — only to
the two vendors with profiles here. It binds those two today. It goes to the
committee when the remaining suppliers have been tiered, which is the
`vendor-reassessment` activity in `schedule.yml`.

## Scope

Every supplier processing Acme, merchant or cardholder data, or holding
privileged access to an Acme system.

## Requirements

### Tiering

9.1 Every supplier carries a `tier` on its vendor profile, set by the data it
holds and the access it has. The three values are the ones the schema allows,
so a tier that is not one of them cannot be written:

| Tier | Definition | Examples |
|---|---|---|
| `critical` | Holds cardholder data, or privileged access to production | Cloud provider, identity provider |
| `important` | Holds personal data, or access to production without privilege | Endpoint agent, SIEM |
| `standard` | Holds internal data only, or none | Ticketing, messaging, marketing tooling |

### Assessment

9.2 A security review is completed before the supplier receives any data.
`critical` and `important` suppliers require an independent attestation — a
current SOC 2 Type II report or ISO 27001 certificate — reviewed rather than
merely filed.

9.3 Contracts with `critical` and `important` suppliers include security
requirements, a breach notification deadline no longer than 48 hours, a right
to audit, and a data return and deletion clause on termination.

9.4 `critical` and `important` suppliers are reassessed annually, and on any
change to the data they process, their subprocessors, or their attestation
status.

## Revision History

| Version | Date | Approved by | Change |
|---|---|---|---|
| 0.1 | 2026-06-18 | CISO | First draft |
| 0.3 | 2026-08-20 | CISO | Tiering aligned to the shared severity scale; awaiting committee approval |
