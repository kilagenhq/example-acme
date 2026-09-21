---
id: tm-merchant-portal
type: threat-model
title: Threat Model — Merchant Portal
description: 'STRIDE analysis of the merchant-facing web portal: session handling, settlement
  account changes, and the third-party JavaScript running beside the merchant''s session.

  '
status: draft
owner: role-appsec-eng
domains:
- appsec
capabilities:
- appsec.threat-modeling
related:
- da-merchant-pii
- std-secure-development
- thr-credential-phishing
systems:
- cloudflare
- owasp-zap
methodology: stride
scope: The merchant-facing portal — authentication, the settlement account change flow, the transaction and payout views, and the third-party scripts loaded on those pages.
source_of_truth: https://miro.acme.example/board/tm-merchant-portal
last_reviewed: '2026-06-10'
next_review: '2026-12-10'
---

# Threat Model — Merchant Portal

> [!note]
> This document is the record. The model itself — the data flow, the STRIDE
> table and the notes from the walkthrough — lives on the board linked in
> `source_of_truth`, which is where it was drawn and where it gets edited.
>
> `tm-payments-api` is written out in full instead. Both shapes are legitimate;
> what has to be here either way is who owns it, what it covers, when it was
> last looked at, and what it found.

## Status

`draft`: written and reviewed by the AppSec engineer, not yet walked through
with the portal team — which is the step that usually finds the interesting
things.

## What it found

- `gap-portal-export-idor` — the export endpoint returned another merchant's
  transactions. Found by the bug bounty before this model reached the team, and
  remediated.
- `gap-unmanaged-vendored-library` — a vendored JavaScript library on the portal
  pages sits outside dependency scanning. Open.

## What it deliberately does not cover

The payments API, which is modelled separately, and the hosted checkout, which
shares the API's trust boundary rather than the portal's.
