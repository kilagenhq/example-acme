---
id: std-access-control
type: standard
title: Access Control Standard
description: 'Requirements for granting, authenticating, reviewing and revoking access to Acme
  systems, including the cardholder data environment.

  '
status: active
owner: role-it-manager
domains:
- grc
- iam
related:
- exc-legacy-billing-sso
- pol-information-security
- std-asset-management
approved_by:
- role-security-committee
requirements:
- ref: '1.1'
  text: Every person has a unique account; shared credentials are prohibited
  how_demonstrated: Quarterly export of every account from the identity provider, reconciled against the HR record by the IT Manager.
  evidence:
  - name: Account inventory Q3 2026 — Okta export
    url: https://drive.acme.example/security/access/2026-Q3-account-inventory.csv
    collected: '2026-09-01'
    freshness: quarterly
    collector: manual
  frameworks:
    iso_27001:
    - A.5.16
    pci_dss_4_0_1:
    - '8'
    soc2:
    - CC6.1
    nist_csf:
    - PR.AA
    iso_27018:
    - A.11.8
- ref: '1.2'
  text: Phishing-resistant MFA on all workforce authentication
  how_demonstrated: Authenticator enrolment report from the identity provider, showing the factor type held by each account.
  evidence:
  - name: MFA enrolment report — September 2026
    url: https://drive.acme.example/security/access/2026-09-mfa-enrolment.csv
    collected: '2026-09-10'
    freshness: quarterly
    collector: quarter-end
  frameworks:
    iso_27001:
    - A.8.5
    pci_dss_4_0_1:
    - '8'
    soc2:
    - CC6.1
    nist_csf:
    - PR.AA
- ref: '1.3'
  text: Applications authenticate against the identity provider
  how_demonstrated: Application list with authentication method, exported from okta.
  frameworks:
    iso_27001:
    - A.5.16
    soc2:
    - CC6.1
- ref: '1.4'
  text: Access is provisioned and revoked from the HR record within defined deadlines
  how_demonstrated: Provisioning and deprovisioning timestamps against HR dates, from okta.
  frameworks:
    iso_27001:
    - A.5.11
    - A.6.5
    pci_dss_4_0_1:
    - '7'
    soc2:
    - CC6.2
    nist_csf:
    - PR.AA
    iso_27018:
    - A.11.10
- ref: '1.5'
  text: Entitlements are certified by the system owner on a defined cycle
  how_demonstrated: Quarterly access review campaign, signed off per system by its named owner.
  evidence:
  - name: Access review Q3 2026 — signed campaign report
    url: https://drive.acme.example/security/access/2026-Q3-access-review.pdf
    collected: '2026-09-08'
    freshness: quarterly
    collector: okta-access-review
  - name: Access review Q2 2026 — signed campaign report
    url: https://drive.acme.example/security/access/2026-Q2-access-review.pdf
    collected: '2026-06-30'
    freshness: quarterly
  frameworks:
    iso_27001:
    - A.5.18
    pci_dss_4_0_1:
    - '7'
    soc2:
    - CC6.3
    nist_csf:
    - PR.AA
    iso_27018:
    - A.11.9
- ref: '1.6'
  text: Administrative access is time-bound and approved
  how_demonstrated: Export of standing and time-bound administrative grants from the privileged access tool, with the approval on each.
  evidence:
  - name: Privileged access grants Q2 2026
    url: https://drive.acme.example/security/access/2026-Q2-privileged-grants.csv
    collected: '2026-06-22'
    freshness: quarterly
    collector: manual
  frameworks:
    iso_27017:
    - CLD.12.1.5
version: '2.0'
capabilities:
- iam.access-reviews
- iam.identity-provider
- iam.joiner-mover-leaver
- iam.mfa
- iam.privileged-access-management
- iam.single-sign-on
last_reviewed: '2026-04-12'
next_review: '2027-04-12'
---

# Access Control Standard

## Purpose

Access is the control that every other control assumes. This standard says who
may hold it, how it is proven, how long it lasts and how it is taken away.

## Scope

All Acme systems and all workforce identities, including contractors. Merchant
and cardholder authentication to Acme's products is governed by the product's
own design and by `std-data-protection-controls`, not by this standard.

## Requirements

### Identity

1.1 Every person accessing an Acme system does so under an account identifying
them individually. Shared credentials are prohibited; where a supplier offers
no per-user model, the credential is held in the managed vault and its use is
recorded.

1.2 All workforce authentication requires a second factor. Phishing-resistant
factors are mandatory for administrative accounts and for any account with
access to the cardholder data environment.

1.3 Applications added to the estate authenticate against the identity provider
over SAML or OIDC. An application that cannot is either replaced or covered by
an approved exception with compensating controls.

### Lifecycle

1.4 Accounts are provisioned from the HR record on hire, adjusted on role
change and disabled on departure. Disablement completes within 24 hours of the
leaving date and within 4 hours where the departure is involuntary.

1.5 System owners certify who holds access to their system and at what level:
quarterly for systems in the cardholder data environment, annually elsewhere.
Entitlements not confirmed during a certification are removed.

### Privilege

1.6 Administrative rights are requested, approved and time-bound rather than
held permanently. Until the privileged access capability is in place, the
compensating control is the quarterly certification in 1.5 and the alerting on
administrative actions required by `std-logging-monitoring`.

## Revision History

| Version | Date | Approved by | Change |
|---|---|---|---|
| 1.0 | 2024-03-15 | Security Committee | Initial version |
| 1.1 | 2025-04-02 | Security Committee | Certification cadence split by CDE scope |
| 2.0 | 2026-04-12 | Security Committee | Phishing-resistant MFA required; deprovisioning deadlines tightened |
