---
id: gap-endpoint-coverage-incomplete
type: gap
title: Five devices are outside endpoint detection coverage
description: Five build machines run without the endpoint agent because it breaks their toolchain, so the fleet inventory and the agent console disagree by five.
owner: role-security-eng
requirement: std-asset-management#4.1
source: internal
found: '2026-03-02'
severity: negligible
tracker: https://acme.atlassian.net/browse/SEC-401
domains:
- infra
related:
- thr-ransomware
systems:
- crowdstrike-falcon
---

# Five devices are outside endpoint detection coverage

## What is missing

The reconciliation between the asset inventory and the endpoint agent console
leaves five machines unmatched. All five are build agents in the engineering
estate: the agent's file-system hooks slow their toolchain to the point that
builds time out, so it was uninstalled and never reinstated.

## Why the severity is `negligible`

These five are not a soft target standing open. They hold no cardholder data,
sit on an isolated build network, are rebuilt from an image on every boot, and
carry no interactive logins. The exposure is the absence of *telemetry* rather
than the absence of a control — if `thr-ransomware` reached them, nobody would
see it there first, but there would be nothing on them to encrypt that is not
rebuilt hourly anyway.

The severity records the exposure, not the tidiness. What is untidy is that
`std-asset-management` 4.1 is written as an absolute and this is an exception to
it that was never filed as one.

## What closes it

Either the vendor's exclusion profile for build workloads, which restores
telemetry without the file-system hooks, or an exception that says plainly why
these five are out of scope. The second is the honest outcome if the first does
not work, and it has not been written.
