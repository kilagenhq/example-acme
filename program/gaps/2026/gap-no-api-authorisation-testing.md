---
id: gap-no-api-authorisation-testing
type: gap
title: No automated authorisation testing against the payments API
description: The payments API authorises every request at the resource, and nothing tests that it does — the one control standing between merchants is unverified.
owner: role-appsec-eng
requirement: std-secure-development#2.6
source: pentest
found: '2026-03-18'
severity: high
source_url: https://drive.acme.example/security/pentest/2026-Q1-payments-api.pdf
tracker: https://acme.atlassian.net/browse/SEC-412
domains:
- appsec
related:
- tm-payments-api
systems:
- owasp-zap
---

# No automated authorisation testing against the payments API

## What is missing

`tm-payments-api` identifies a merchant reaching another merchant's data as the
highest-severity design concern, and the control against it is that
authorisation is checked at the resource on every request. Nothing tests that
control. The test suite covers authentication — that a caller is who they say —
and not authorisation, which is whether they should have this particular
record.

The 2026 penetration test found it by hand. `gap-portal-export-idor` is the same
class of defect in the merchant portal, found the same way, four weeks later.
Two instances of one bug class, both found by a person, is what an absent test
looks like.

## Why it is still open

The fix is not a single test but a fixture: two merchants, a token for each,
and a generated case for every endpoint asserting that merchant A's token
cannot reach merchant B's resource. Building it is a week, and the AppSec
engineer has spent that week on the portal defect instead.

## What closes it

The cross-tenant fixture in the API's own suite, running on every pull request,
with a case generated per endpoint so a new endpoint is covered by existing
it. Then a re-test in the next penetration test to confirm.
