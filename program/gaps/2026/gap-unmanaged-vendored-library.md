---
id: gap-unmanaged-vendored-library
type: gap
title: Vendored JavaScript library in the merchant portal is outside dependency scanning
description: A charting library is committed into the merchant portal rather than installed, so dependency scanning cannot see it and nothing reports when it is vulnerable.
owner: role-appsec-eng
requirement: std-secure-development#2.3
source: threat-model
found: '2026-06-11'
severity: high
tracker: https://acme.atlassian.net/browse/APPSEC-88
domains:
- appsec
related:
- rsk-vulnerable-dependency-in-production
- thr-supply-chain-compromise
systems:
- dependabot
---

# Vendored JavaScript library in the merchant portal is outside dependency scanning

## What is missing

The merchant portal vendors a charting library as a committed minified file
rather than declaring it as a dependency. Software composition analysis reads
the manifest, so the library is invisible to it: no version is known, no
advisory reaches anybody, and the mean-time-to-patch measured against
`std-vulnerability-management` 3.1 does not cover it.

It is also drift-prone in a way a declared dependency is not. The committed file
and whatever version anybody believes is in it can disagree silently, and
nothing would notice.

## Why it is still open

It was vendored to work around a build issue that no longer exists. Undoing it
is a small change to the build and a re-test of every chart in the portal, which
is half a day of somebody's time and has never been the most important half-day
available.

## What closes it

The library declared in the manifest at a pinned version, the committed copy
deleted, and a check that fails the build if a file matching the vendored
pattern reappears. `rsk-vulnerable-dependency-in-production` carries the
exposure in the meantime.
