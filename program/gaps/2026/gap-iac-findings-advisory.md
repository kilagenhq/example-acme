---
id: gap-iac-findings-advisory
type: gap
title: Infrastructure-as-code findings are advisory and nobody is required to act on them
description: Terraform scanning reports on the pull request but cannot block it, so a misconfiguration is caught before deployment and shipped anyway.
owner: role-security-eng
requirement: std-secure-development#2.5
source: internal
found: '2026-06-25'
severity: medium
tracker: https://acme.atlassian.net/browse/APPSEC-91
domains:
- appsec
related:
- rsk-cloud-misconfiguration-exposure
systems:
- trivy
---

# Infrastructure-as-code findings are advisory and nobody is required to act on them

## What is missing

Infrastructure-as-code scanning runs on every pull request and comments its
findings. It is not a required check, so a pull request merges with findings
open and nobody has to say why.

This is the asymmetry `rsk-cloud-misconfiguration-exposure` is really about:
cloud posture management finds the same class of problem *after* deployment and
blocks it there, while the control that would have stopped it reaching
production only advises. The expensive half works and the cheap half does not.

## Why it is still open

Making the check required with the current rule set would block roughly a third
of infrastructure pull requests, most of them on findings the platform team
considers acceptable for non-production. Nobody has done the work of splitting
the rules into "must not merge" and "worth knowing".

## What closes it

A rule set triaged into blocking and advisory, the blocking half made a required
check on the production workspaces, and a documented route for an engineer to
override with a reason recorded on the pull request.
