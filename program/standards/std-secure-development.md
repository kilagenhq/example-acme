---
id: std-secure-development
type: standard
title: Secure Development Standard
description: 'Requirements for how Acme writes, reviews, scans and ships code, including the
  scanning gates in the pipeline and the handling of secrets.

  '
status: active
owner: role-appsec-eng
domains:
- grc
- appsec
related:
- gl-secure-coding
- pol-information-security
- std-vulnerability-management
approved_by:
- role-security-committee
requirements:
- ref: '2.1'
  text: Every change is reviewed by someone other than its author
  how_demonstrated: Branch protection settings exported from the forge, showing review required on every protected branch.
  evidence:
  - name: Branch protection settings — all repositories
    url: https://drive.acme.example/security/appsec/2026-08-branch-protection.json
    collected: '2026-08-14'
    freshness: semi-annually
    collector: manual
  frameworks:
    iso_27001:
    - A.8.28
    - A.8.32
    soc2:
    - CC8.1
    nist_csf:
    - PR.PS
- ref: '2.2'
  text: Static analysis runs on every pull request and blocks on high findings
  how_demonstrated: Pipeline configuration showing the static analysis gate, with a sample run that blocked on a high finding.
  evidence:
  - name: SAST gate configuration and blocking run
    url: https://drive.acme.example/security/appsec/2026-09-sast-gate.pdf
    collected: '2026-09-02'
    freshness: quarterly
    collector: quarter-end
  frameworks:
    iso_27001:
    - A.8.28
    pci_dss_4_0_1:
    - '6'
    nist_csf:
    - PR.PS
- ref: '2.3'
  text: Dependencies are scanned continuously and patched within the deadlines
  how_demonstrated: Dependency scanner report listing open findings by severity against the remediation deadlines.
  evidence:
  - name: Dependency findings — September 2026
    url: https://drive.acme.example/security/appsec/2026-09-dependency-findings.csv
    collected: '2026-09-15'
    freshness: monthly
    collector: manual
  frameworks:
    iso_27001:
    - A.8.8
    pci_dss_4_0_1:
    - '6'
    nist_csf:
    - PR.PS
- ref: '2.4'
  text: Secrets are never committed; a leaked secret is rotated within 4 hours
  how_demonstrated: Secret scanning configuration, and the rotation record for every secret it has caught.
  evidence:
  - name: Secret scanning configuration and rotation log
    url: https://drive.acme.example/security/appsec/2026-09-secret-scanning.pdf
    collected: '2026-09-01'
    freshness: semi-annually
    collector: manual
  frameworks:
    iso_27001:
    - A.5.17
    pci_dss_4_0_1:
    - '6'
    nist_csf:
    - PR.DS
- ref: '2.5'
  text: Images and infrastructure code are scanned before deployment
  how_demonstrated: Build logs showing scan results, from trivy.
  frameworks:
    iso_27001:
    - A.8.9
    pci_dss_4_0_1:
    - '6'
    iso_27017:
    - CLD.9.5.2
- ref: '2.6'
  text: New services and payment flow changes are threat modelled
  how_demonstrated: Threat models in `program/threat-models/`, held in this repository.
  frameworks:
    iso_27001:
    - A.8.27
    nist_csf:
    - ID.RA
- ref: '2.7'
  text: Production data is never used in non-production environments
  how_demonstrated: Environment configuration and access reviews, from aws.
  frameworks:
    iso_27001:
    - A.8.33
    pci_dss_4_0_1:
    - '6'
version: '1.4'
capabilities:
- appsec.container-scanning
- appsec.iac-scanning
- appsec.sast
- appsec.sca
- appsec.secrets-scanning
- appsec.threat-modeling
last_reviewed: '2026-05-08'
next_review: '2027-05-08'
---

# Secure Development Standard

## Purpose

Acme's product is code that moves money. This standard sets what must be true
of a change before it reaches production.

## Scope

All application and infrastructure repositories, all environments, and every
engineer including contractors.

## Requirements

### Review

2.1 Every change is reviewed and approved by someone other than its author
before merge. Changes to the cardholder data environment require two approvals,
one from the platform team.

### Scanning gates

2.2 Static analysis runs on every pull request. High and critical findings
block the merge; medium and below are triaged within the sprint. Suppressions
require a reason and an expiry date.

2.3 Dependencies are scanned continuously and patched within the deadlines in
`std-vulnerability-management`. A dependency with no upstream fix is escalated
as a gap, not silently accepted.

2.4 Credentials, keys and tokens are never committed. Push protection is
enabled on all repositories; a secret that reaches a remote is treated as
compromised and rotated within 4 hours, following `rb-rotate-leaked-secret`.

2.5 Container images are scanned before publication and fail the build on
critical findings. Infrastructure-as-code is scanned on every pull request;
findings are advisory until the platform baseline is agreed, and that gap is
tracked.

### Design

2.6 A new service, or a change to a payment flow, is threat modelled before
implementation. The model is recorded as a `TM-*` document and reviewed when the
design changes.

2.7 Production data is not copied into staging, analytics or a developer
machine. Non-production environments use synthetic or tokenised data.

## Revision History

| Version | Date | Approved by | Change |
|---|---|---|---|
| 1.0 | 2024-05-20 | Security Committee | Initial version |
| 1.2 | 2025-06-14 | Security Committee | Added container and IaC scanning |
| 1.3 | 2025-11-03 | Security Committee | Secret rotation deadline set at 4 hours |
| 1.4 | 2026-05-08 | Security Committee | Threat modelling made mandatory for payment flows |
