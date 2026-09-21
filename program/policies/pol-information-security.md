---
id: pol-information-security
type: policy
title: Information Security Policy
description: 'The board-approved principles governing how Acme protects its own, its merchants''
  and its cardholders'' information, and the authority under which every standard in this program
  is issued.

  '
status: active
publish: all
owner: role-ciso
domains:
- grc
related:
- std-access-control
- std-asset-management
- std-data-protection-controls
- std-incident-response
- std-logging-monitoring
- std-risk-framework
- std-secure-development
- std-vulnerability-management
approved_by:
- role-security-committee
version: '2.1'
last_reviewed: '2026-02-10'
next_review: '2027-02-10'
---

# Information Security Policy

## Purpose

Acme processes payments on behalf of merchants. The information it holds —
cardholder data, merchant records, the systems that move money — is the
business, not a supporting asset. This policy states what Acme requires of
itself in protecting it, and delegates the detail to the standards listed
below.

## Scope

Everyone who works for Acme, including contractors, and every system that
processes Acme, merchant or cardholder data, whether operated by Acme or by a
supplier on its behalf.

## Principles

1. **Security is a condition of shipping, not a stage after it.** Controls are
   built into the development and deployment path rather than inspected at the
   end.
2. **Least privilege, by default and on a timer.** Access is granted for a
   stated reason, at the lowest level that works, and is removed when the
   reason ends.
3. **Cardholder data is minimised.** Acme does not store what it does not need,
   and what it must keep is encrypted and tokenised.
4. **Everything of consequence is logged, and the log is trustworthy.** An
   event nobody can reconstruct afterwards is an event Acme cannot answer for.
5. **Risk is owned, not admired.** Every risk has an owner, a treatment
   decision and a review date; acceptance is a decision made by a named role.
6. **Suppliers are held to this policy.** A control Acme requires of itself is
   required of anyone processing its data.
7. **Incidents are expected.** The measure is detection, containment and
   honesty about what happened, not their absence.
8. **The program is written down and kept current.** This repository is the
   source of truth; anything not recorded here does not exist.

## Governance

| Body or role | Responsibility |
|---|---|
| Security Committee | Approves this policy and every standard under it |
| CTO | Accountable to the board; accepts high and critical risk |
| CISO | Runs the program; owns the standards and the risk register |
| System owners | Accountable for the controls on the systems they own |
| Everyone | Completes training and reports anything that looks wrong |

## Compliance and exceptions

Acme is measured against PCI DSS and ISO/IEC 27001 as mandatory obligations,
and against the SOC 2 Trust Services Criteria and NIST CSF 2.0 on a
comply-or-explain basis. A requirement that cannot be met is either a **gap**,
recorded as a gap in `program/gaps/` and remediated, or an **exception**, approved by a named
role with compensating controls and a hard expiry. There is no third option.

Deliberate breach of this policy is a disciplinary matter.

## Review

Annually, and after any incident rated `critical`.

## Revision History

| Version | Date | Approved by | Change |
|---|---|---|---|
| 1.0 | 2024-03-01 | Security Committee | Initial version |
| 2.0 | 2025-02-14 | Security Committee | Rewritten for PCI DSS v4.0 and the ISO 27001:2022 transition |
| 2.1 | 2026-02-10 | Security Committee | Added supplier principle; delegated detail to eight standards |
