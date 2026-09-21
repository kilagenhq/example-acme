---
id: std-asset-management
type: standard
title: Asset Management Standard
description: 'What Acme must know about every system it runs: who owns it, what data it holds,
  how critical it is, and how often that record is confirmed.

  '
status: active
owner: role-it-manager
domains:
- grc
- infra
- data-security
related:
- pol-data-protection
- pol-information-security
- std-access-control
- std-data-protection-controls
approved_by:
- role-security-committee
requirements:
- ref: '4.1'
  text: Every system in use is recorded in the inventory
  how_demonstrated: Reconciliation of the inventory against the cloud accounts and the endpoint agent, with the unmatched list.
  evidence:
  - name: Inventory reconciliation — September 2026
    url: https://drive.acme.example/security/assets/2026-09-inventory-reconciliation.csv
    collected: '2026-09-05'
    freshness: annually
    collector: manual
  frameworks:
    iso_27001:
    - A.5.9
    pci_dss_4_0_1:
    - '12'
    soc2:
    - CC6.1
    nist_csf:
    - ID.AM
- ref: '4.2'
  text: Every system has a named owner and a second owner
  how_demonstrated: Owner and second owner per system, from the estate’s inventory. This repository names systems; it does not own their records.
  frameworks:
    iso_27001:
    - A.5.9
    soc2:
    - CC1.3
    nist_csf:
    - ID.AM
- ref: '4.3'
  text: Criticality and CIA ratings are recorded for systems in scope
  how_demonstrated: Criticality, CIA ratings and recovery objectives per system, from the estate’s inventory. Recorded here only for business processes.
  frameworks:
    iso_27001:
    - A.5.12
    nist_csf:
    - ID.AM
- ref: '4.4'
  text: Data assets are inventoried, classified and linked to the systems processing them
  how_demonstrated: Data asset inventory and system links, from program/data-assets/.
  frameworks:
    iso_27001:
    - A.5.12
    pci_dss_4_0_1:
    - '3'
    nist_csf:
    - ID.AM
- ref: '4.5'
  text: Inventory records are confirmed at least annually
  how_demonstrated: Annual confirmation campaign, in which each owner signs that their records are still correct.
  evidence:
  - name: Inventory confirmation 2025 — signed by owner
    url: https://drive.acme.example/security/assets/2025-inventory-confirmation.pdf
    collected: '2025-09-12'
    freshness: annually
version: '1.1'
capabilities:
- data-security.data-classification
- grc.asset-inventory
last_reviewed: '2026-04-12'
next_review: '2027-04-12'
---

# Asset Management Standard

## Purpose

Every other standard is scoped by this one. A control applies to the systems on
the list; a system that is not on the list has no controls at all.

## Scope

All systems processing Acme, merchant or cardholder data, whether operated by
Acme or by a supplier, and all data assets they process.

## Requirements

### Inventory

4.1 Every system in use is named in `program/model/systems.yml`, and every
document that touches it names it in `systems:`. A system nobody can name there
is not approved for use. The record itself — what it runs on, who pays for it,
when it was last patched — stays in the estate, at the end of that entry's URL.

4.2 Every system has a named owner and a second owner in the estate's
inventory, both recorded as roles rather than people. The second owner exists
so that ownership survives a holiday and a resignation.

4.3 Systems in the cardholder data environment, and any system rated `high` or
above, carry criticality, CIA ratings and recovery objectives in that same
inventory. This repository does not mirror them: a copy taken once is a number
nobody re-checks.

### Data

4.4 Data assets are inventoried as `da-*` documents, classified under
`pol-data-protection`, and linked from the systems that process them. A system
holding restricted data without a corresponding data asset is a gap.

### Maintenance

4.5 Inventory records are confirmed at least annually by their owner. The
review date on the document is the evidence; an overdue record is reported by
CI every week.

## Revision History

| Version | Date | Approved by | Change |
|---|---|---|---|
| 1.0 | 2024-09-30 | Security Committee | Initial version |
| 1.1 | 2026-04-12 | Security Committee | Second owner made mandatory; recovery objectives added |
