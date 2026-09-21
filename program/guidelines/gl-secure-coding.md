---
id: gl-secure-coding
type: guideline
title: Secure Coding Guideline
description: 'Recommended practice for Acme engineers writing payment and merchant-facing code,
  with the patterns the custom scanning rules look for.

  '
status: active
publish:
- confluence
owner: role-appsec-eng
domains:
- appsec
capabilities:
- appsec.security-champions
related:
- std-secure-development
- tm-payments-api
systems:
- semgrep
last_reviewed: '2026-05-20'
next_review: '2027-05-20'
---

# Secure Coding Guideline

> This document is a snapshot. The version engineers read lives in the
> engineering handbook (`managed_externally` in the frontmatter); this copy
> exists so that the security program can reference it and so an auditor can
> see what it says without an account on the wiki.

## Money

- **Never represent an amount as a floating point number.** Use integer minor
  units. `semgrep` has a rule for this and it is not advisory.
- Currency travels with the amount, always. An amount without a currency is a
  bug waiting for a merchant in another country.
- Rounding happens once, at the boundary, in a documented direction.

## Authorisation

- Check authorisation at the resource, not at the route. Every merchant-scoped
  endpoint verifies that the authenticated merchant owns the object, on every
  request.
- Object identifiers in URLs are opaque. A sequential integer invites
  enumeration, and enumeration of merchant identifiers is a live threat.
- Deny by default. A new endpoint with no explicit authorisation rule is
  unreachable, not public.

## Data

- Card numbers do not enter logs, error messages, analytics events or exception
  trackers. The scanning rule catches the obvious cases; the discipline covers
  the rest.
- Log identifiers, not payloads.
- Redact at the point of logging, not in a downstream pipeline.

## Input and output

- Validate at the edge against a schema, and reject rather than coerce.
- Parameterise every query. There is no acceptable string-concatenated SQL.
- Encode on output for the context — HTML, attribute, URL, JavaScript — rather
  than sanitising on input.

## Secrets and dependencies

- No credential in source, ever, including tests. Use the secret store.
- A new dependency needs a reason. Prefer the standard library, then a
  maintained package with a real release history.
- Pin versions and let `dependabot` move them.

## Errors

- Return the minimum to the caller and the maximum to the log.
- A payment failure message tells the merchant what to do next, not what the
  system does internally.
