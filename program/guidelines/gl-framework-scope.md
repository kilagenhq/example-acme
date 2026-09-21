---
id: gl-framework-scope
type: guideline
title: Which Frameworks Apply, and How Far They Are Mapped
description: >
  Why each of the six frameworks is in scope, what binding means for each, and
  which parts of each have deliberately not been mapped yet. The coverage
  numbers on the dashboard are only readable with this.
status: active
owner: role-grc-analyst
domains:
- grc
capabilities:
- grc.compliance-management
related:
- gl-pci-dss-scope
- pol-information-security
- std-risk-framework
last_reviewed: '2026-09-15'
next_review: '2027-09-15'
---

# Which Frameworks Apply, and How Far They Are Mapped

## Read the numbers correctly

The dashboard shows a mapped-over-total ratio for each framework. **Mapped means a clause is addressed by a written requirement in one of Acme's nine standards. It does not mean the control is implemented, and it does not mean it was tested.** A clause counts as mapped the moment a requirement names it, whether or not anything is attached to prove it.

The ratio is therefore a measure of how much of a framework Acme has *written against*, and the honest reading of a low one is "we have not claimed this yet", not "we are failing this".

## The six, and why each is here

| Framework | Binding | Why it is in scope |
|---|---|---|
| PCI DSS v4.0.1 | `mandatory` | Acme processes cardholder data in its own environment. The scheme requires it and an assessor checks it. Scope is in `gl-pci-dss-scope`. |
| ISO/IEC 27001:2022 | `voluntary` | Certification is a commercial requirement for European enterprise merchants. Acme chose it; nobody imposed it. |
| SOC 2 | `voluntary` | The equivalent for US merchants, who ask for a Type II report rather than a certificate. |
| NIST CSF | `reference` | Used as a vocabulary for talking about coverage with people who do not read the other three. Nobody certifies against it. |
| ISO/IEC 27017 | `reference` | Cloud-specific guidance, read for the controls it adds over 27001 rather than mapped exhaustively. |
| ISO/IEC 27018 | `reference` | Personal data in the cloud. Relevant because merchant PII is processed by the same platform. |

The difference between the three bindings is **who checks**. `mandatory` means somebody outside Acme audits it and the answer has consequences. `voluntary` means Acme has committed to it and is audited, but chose to be. `reference` means Acme reads it and maps what is useful; no one comes to check.

## What has deliberately not been mapped

**PCI DSS — 8 of 12 requirements.** The four unmapped are requirement 9 (physical access), which is the hosting provider's under a shared-responsibility model; and three sub-areas of 10, 11 and 12 that fall to the provider for the same reason. Acme's Attestation of Compliance names them as inherited. Mapping them here would claim work Acme does not do.

**ISO/IEC 27001 — 30 of 93 Annex A controls.** This is the number that looks worst and is the most deliberate. Acme's nine standards were written against PCI DSS first, because that is the one with an assessor; the Annex A controls they happen to address were mapped as they were written. The remaining 63 have not been assessed, not been written against, and are not being claimed. Closing that is the 2027 certification programme, and it is a year of work rather than a mapping exercise — several of the 63 need a control to exist before a requirement can honestly name them.

**SOC 2 — 18 of 38 criteria.** The Security category is substantially mapped. Availability, Confidentiality, Processing Integrity and Privacy are not: Acme's report is scoped to Security only, which is what its merchants ask for.

**NIST CSF — 14 of 22 categories, ISO 27017 — 5 of 7, ISO 27018 — 8 of 25.** All three are `reference`. They are mapped where a requirement already written happens to satisfy a clause, and not otherwise. A `reference` framework at 100% would mean somebody had gone looking for clauses to claim, which is the opposite of what these are for.

## Why this is published rather than kept quiet

A compliance repository that showed every framework fully mapped would be either a much older programme than this one or a dishonest one. The value of writing the programme down is that the distance between what is claimed and what is proven is visible and has an owner. That distance is `gap-*` documents, the requirements with no evidence on the Evidence page, and this note.
