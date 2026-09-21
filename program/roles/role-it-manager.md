---
id: role-it-manager
type: role
title: IT Manager
description: 'Owns corporate IT: the identity provider, the device fleet, the business applications
  and the joiner-mover-leaver process.

  '
status: active
owner: role-ciso
domains:
- iam
reports_to: role-cto
role_type: individual
last_reviewed: '2026-01-01'
next_review: '2027-01-01'
---

# IT Manager

Owns the systems everyone at Acme touches, and therefore most of `02-iam`.

## Responsibilities

- Operate the identity provider and enforce single sign-on for new applications.
- Run joiner-mover-leaver within the deadlines in `std-access-control`.
- Own the business applications in the system inventory and their control configuration.
- Keep the device fleet enrolled, encrypted and patched.

## Authority

- Approves new SaaS applications for corporate use, after the vendor review.
- Suspends an account immediately on a credible compromise signal.
