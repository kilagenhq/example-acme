---
id: role-appsec-eng
type: role
title: Application Security Engineer
description: 'Owns the application security toolchain and the secure development lifecycle:
  SAST, SCA, secrets scanning, threat modelling and the security champions network.

  '
status: active
owner: role-ciso
domains:
- appsec
reports_to: role-ciso
role_type: individual
last_reviewed: '2026-01-01'
next_review: '2027-01-01'
---

# Application Security Engineer

The role closest to the engineering teams. Most of `04-appsec` belongs here.

## Responsibilities

- Operate the scanning toolchain in CI and keep its noise low enough to be believed.
- Triage findings from SAST, SCA, secrets and container scanning, and route
  them into the tracker with an owner.
- Run threat models for new services and payment flows.
- Run the security champions network and the secure coding guidance.

## Authority

- Sets the severity threshold that breaks a build.
- Grants short-lived scanner suppressions; anything permanent becomes an
  exception under `exc-*`.
