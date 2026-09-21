---
id: gl-pci-dss-scope
type: guideline
title: PCI DSS Scope and Applicability
description: >
  Why PCI DSS applies to Acme, what is inside the cardholder data environment
  and what is deliberately outside it, and where the current Attestation of
  Compliance lives.
status: active
owner: role-grc-analyst
domains:
- grc
- data-security
capabilities:
- grc.compliance-management
related:
- pol-information-security
- std-data-protection-controls
- da-cardholder-data
last_reviewed: '2026-07-15'
next_review: '2027-07-15'
---

# PCI DSS Scope and Applicability

## Why it applies

Acme operates a hosted checkout, a payments API and a merchant portal. Cardholder
data is processed and transiently stored in Acme's own environment rather than
passed straight to a processor, which makes Acme a **merchant service provider**
under PCI DSS and puts the full standard in scope rather than a self-assessment
questionnaire.

The obligation is contractual, not statutory: it arrives through the acquiring
bank agreement and through the card brands' rules. Losing it does not produce a
regulator's fine; it produces the loss of the ability to process cards, which is
the business.

## What is in scope

The cardholder data environment (CDE) is the set of systems that store, process
or transmit account data, plus everything that can reach them.

| In scope | Why |
|---|---|
| Hosted checkout | Accepts the primary account number from the cardholder |
| Payments API | Receives account data from merchant server integrations |
| Tokenisation service | Holds the token vault and the mapping to account data |
| Settlement batch jobs | Read account data to produce settlement files |
| Bastion and CI runners that deploy the above | Connected systems, per the standard's definition |

## What is deliberately out of scope

| Out of scope | Why |
|---|---|
| Merchant portal | Displays tokens and the last four digits only; never receives account data |
| Marketing site | No connectivity to the CDE, separate account and network |
| Internal corporate IT | Segmented from the CDE; segmentation is tested annually |

Segmentation is what makes these exclusions real rather than asserted. A failed
segmentation test therefore does not only produce a finding — it enlarges the
scope of the whole assessment, so it is treated as a critical issue.

## Where the evidence lives

- The current **Attestation of Compliance** and the **Report on Compliance** are
  held by the GRC analyst and shared with merchants under NDA on request. They
  are not in this repository: they are dated artefacts produced by the QSA, and
  this repository holds the record, not the evidence
  (see the Reference tab of the dashboard, "Why Kilagen is this way").
- The mapping from each PCI requirement to the Acme requirement that addresses
  it is computed, not written here. It is in the Compliance lens, and it comes
  from the `frameworks:` block on each requirement in the standards.

## How this document is used

This is the answer to "why does PCI apply to us, and to what". An auditor asks
for it by name at the start of an assessment, it has an owner, and it is
reviewed annually alongside the assessment itself — which is what earns it a
place in the repository rather than in a wiki page nobody revisits.
