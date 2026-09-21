---
id: std-data-protection-controls
type: standard
title: Data Protection Controls Standard
description: 'The controls that implement the data protection policy: classification, encryption
  in transit and at rest, key lifecycle, retention, disposal and loss prevention.

  '
status: active
owner: role-security-eng
domains:
- grc
- data-security
- infra
related:
- da-cardholder-data
- da-merchant-pii
- pol-data-protection
- std-asset-management
approved_by:
- role-security-committee
requirements:
- ref: '6.1'
  text: Data assets carry a classification that determines their controls
  how_demonstrated: Classification on every data asset, from program/data-assets/.
  frameworks:
    iso_27001:
    - A.5.12
    - A.5.13
    soc2:
    - C1.1
    nist_csf:
    - ID.AM
- ref: '6.2'
  text: All data in transit is encrypted with approved protocols
  how_demonstrated: TLS configuration and continuous monitoring, from cloudflare.
  frameworks:
    iso_27001:
    - A.8.24
    pci_dss_4_0_1:
    - '4'
    soc2:
    - C1.1
    nist_csf:
    - PR.DS
    iso_27018:
    - A.11.6
- ref: '6.3'
  text: All data at rest is encrypted, and cardholder data is tokenised
  how_demonstrated: Encryption-at-rest settings for every store holding cardholder or personal data, and the tokenisation vault attestation.
  evidence:
  - name: Encryption at rest — settings export and vault attestation
    url: https://drive.acme.example/security/data/2026-H2-encryption-at-rest.pdf
    collected: '2026-07-01'
    freshness: semi-annually
    collector: manual
  frameworks:
    iso_27001:
    - A.8.24
    pci_dss_4_0_1:
    - '3'
    nist_csf:
    - PR.DS
- ref: '6.4'
  text: Keys follow a documented lifecycle and are held apart from the data
  how_demonstrated: Key policies, rotation state, access review, from aws-kms.
  frameworks:
    iso_27001:
    - A.8.24
    pci_dss_4_0_1:
    - '3'
    nist_csf:
    - PR.DS
- ref: '6.5'
  text: Data is retained only for its stated period and then disposed of
  how_demonstrated: Retention schedule and deletion job records, from program/data-assets/.
  frameworks:
    iso_27001:
    - A.8.10
    pci_dss_4_0_1:
    - '3'
    soc2:
    - C1.2
    iso_27017:
    - CLD.8.1.5
    iso_27018:
    - A.10.3
- ref: '6.6'
  text: Sensitive data leaving Acme through monitored channels is detected
  how_demonstrated: DLP rules and quarantine events, from google-workspace.
  frameworks:
    iso_27001:
    - A.8.12
    nist_csf:
    - PR.DS
version: '1.2'
capabilities:
- data-security.data-classification
- data-security.data-loss-prevention
- data-security.data-retention
- data-security.encryption-at-rest
- data-security.encryption-in-transit
- data-security.key-management
last_reviewed: '2026-03-05'
next_review: '2027-03-05'
---

# Data Protection Controls Standard

## Purpose

`pol-data-protection` states the principles. This standard states what must be
configured, where, and what evidence proves it.

## Scope

All Acme data in all environments, with the strictest requirements applying to
cardholder data and personal data.

## Requirements

### Classification

6.1 Every data asset carries one of four classifications, and the
classification determines the minimum controls:

| Classification | Encryption | Access | Sharing |
|---|---|---|---|
| Restricted | In transit and at rest, tokenised where possible | Named roles only, logged | Never outside Acme |
| Confidential | In transit and at rest | Role-based, reviewed quarterly | Under contract only |
| Internal | In transit | All staff | Not published |
| Public | In transit | All staff | Unrestricted |

### Cryptography

6.2 Data in transit is encrypted with TLS 1.2 or above. Weak ciphers are
disabled at the edge and between services within the cardholder data
environment.

6.3 Data at rest is encrypted at the storage layer, including backups and
snapshots. The primary account number is tokenised; the only system able to
reverse a token is the tokenisation service.

6.4 Keys are generated, stored, rotated and destroyed under a documented
lifecycle, held in the key management service, and separated by environment and
data class. Annual rotation is automatic; emergency rotation is a runbook.

### Lifecycle

6.5 Each data asset records a retention period and the reason for it. Data past
its period is deleted or irreversibly anonymised. Automated deletion exists for
logs; everything else is a scheduled manual task, and that difference is a
known gap.

6.6 Sensitive data leaving through monitored channels is detected and, where
the rule is confident, blocked. Only outbound email is monitored today; file
sharing and endpoints are not, and the shortfall is recorded as a gap.

## Revision History

| Version | Date | Approved by | Change |
|---|---|---|---|
| 1.0 | 2024-10-14 | Security Committee | Initial version |
| 1.1 | 2025-07-08 | Security Committee | Classification matrix added |
| 1.2 | 2026-03-05 | Security Committee | Tokenisation required for the primary account number |
