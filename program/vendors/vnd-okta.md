---
id: vnd-okta
type: vendor
title: Okta — Vendor Profile
description: 'Risk profile for the workforce identity provider: the supplier holding authentication
  for every Acme system, and therefore a critical-tier dependency.

  '
status: active
owner: role-grc-analyst
domains:
- grc
related:
- rsk-workforce-account-takeover
- std-access-control
- std-third-party-risk
systems:
- okta
vendor_name: Okta
data_scope:
- Workforce identity and authentication data
- Session and authentication event logs
- No cardholder data, no merchant PII
certifications:
- name: ISO/IEC 27001
  verified: '2026-02-14'
  url: https://drive.acme.example/vendors/okta/iso-27001-certificate.pdf
- name: SOC 2 Type II
  verified: '2026-02-14'
  url: https://drive.acme.example/vendors/okta/soc2-type2-2025.pdf
- name: ISO/IEC 27018
  verified: '2026-02-14'
  url: https://drive.acme.example/vendors/okta/iso-27018-certificate.pdf
tier: critical
criticality: critical
cia:
  confidentiality: high
  integrity: critical
  availability: critical
rto: 4h
rpo: 1h
last_reviewed: '2026-05-14'
next_review: '2027-05-14'
---

# Okta — Vendor Profile

## Why this vendor is critical tier

It authenticates every workforce identity at Acme. A compromise of the
supplier, or a prolonged outage, is indistinguishable in effect from a
compromise or outage of Acme's own access control.

## Data and access

| Question | Answer |
|---|---|
| Personal data held | Workforce names, work email addresses, device metadata |
| Cardholder data held | None |
| Privileged access to Acme systems | None inbound; the supplier is the authority for outbound access |
| Data location | EU cell |
| Subprocessors | Reviewed at contract renewal; list held by Legal |

## Assessment

| Item | Result | Date |
|---|---|---|
| SOC 2 Type II report | Reviewed, no exceptions relevant to Acme | 2026-05-14 |
| ISO 27001 certificate | Current, scope covers the EU cell | 2026-05-14 |
| Penetration test summary | Provided under NDA, reviewed | 2026-05-14 |
| Breach notification clause | 24 hours, contractual | 2025-11-01 |
| Right to audit | Yes, on notice | 2025-11-01 |

## Concentration and exit

There is no second identity provider, and there is no realistic short-term
migration: the exit plan is a documented break-glass path (`okta`) that
keeps administrative access to the cloud accounts available if the provider is
unreachable. That is a mitigation for outage, not for supplier compromise, and
the residual concentration risk is accepted at board level.

## Next review

Annually, or on any material change to the subprocessor list or the
attestation status, per `std-third-party-risk` 9.4.
