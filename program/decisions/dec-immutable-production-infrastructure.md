---
id: dec-immutable-production-infrastructure
type: decision
title: Production Infrastructure Is Immutable
description: 'Decision that production servers are never modified in place: changes are made
  by replacing the workload from a rebuilt image, and human access to production hosts is removed.

  '
status: active
owner: role-security-eng
domains:
- infra
related:
- std-asset-management
- std-secure-development
- thr-ransomware
systems:
- aws
- trivy
decided: '2024-11-12'
immutable: true
---

# Production Infrastructure Is Immutable

## Context

Production drift was the source of three incidents in 2024: a host patched by
hand and never re-patched, a security group widened during an outage and never
narrowed, and a configuration change nobody could attribute. Each was a small
failure of process rather than a control failure, and process was not fixing
them.

## Decision

Production infrastructure is immutable. Changes are made by rebuilding the
image or the infrastructure definition and replacing the running workload.
Interactive access to production hosts is removed; where investigation requires
it, an ephemeral session is granted, recorded and expires automatically.

## Consequences

**Positive.**

- Configuration state is what the repository says it is, which is what makes
  infrastructure-as-code scanning worth running at all.
- A compromised host is replaced rather than cleaned, which shortens incident
  recovery from hours to minutes.
- It removes most of the estate a ransomware attack would rely on, and is cited
  as a control against `thr-ransomware`.

**Negative.**

- Debugging a production-only problem is slower and depends on telemetry being
  good enough, which pushed investment into logging earlier than planned.
- The build pipeline became a production dependency, and therefore a target —
  a trade recorded against `thr-supply-chain-compromise`.

**Not covered.** The two legacy virtual machines running the billing
integration are exempt until that application is retired.
