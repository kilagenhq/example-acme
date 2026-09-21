---
id: thr-credential-phishing
type: threat
title: Credential Phishing Against the Workforce
description: 'An attacker phishes an Acme employee for their credentials and second factor,
  then uses the session to reach production or merchant data.

  '
status: active
owner: role-ciso
domains:
- grc
related:
- inc-finance-credential-phishing
- rsk-workforce-account-takeover
systems:
- google-workspace
- knowbe4
- okta
priority: 1
severity: critical
last_reviewed: '2026-07-15'
next_review: '2027-01-15'
---

# Credential Phishing Against the Workforce

## Threat scenario

An attacker sends a targeted message — usually impersonating a supplier, an
internal tool or the identity provider itself — that leads to a credential
capture page. Where a second factor is present, the attacker either proxies it
in real time or fatigues the user with repeated push prompts. The stolen
session is then used to reach whatever the account can reach: the merchant
portal, the ticketing system, or, at worst, an administrative console.

## Why Acme is exposed

- Remote-first: there is no network location that distinguishes a legitimate
  login from an attacker's.
- The finance and support teams routinely receive attachments and links from
  outside the company.
- One credential phishing incident has already occurred (`inc-finance-credential-phishing`).

## Threat actors

| Actor | Motivation | Sophistication |
|---|---|---|
| Financially motivated crews | Access to payment flows and merchant funds | Medium to high, tooling widely available |
| Initial access brokers | Resale of valid sessions | Medium |
| Opportunists | Whatever the account holds | Low |

## Existing controls

| Control | Where |
|---|---|
| Phishing-resistant MFA on all workforce accounts | `std-access-control` 1.2 |
| Quarterly phishing simulation with follow-up training | knowbe4 |
| Impossible-travel and MFA-fatigue detections | elastic-siem |
| Outbound DLP on card number patterns | google-workspace |
| Documented response playbook | pb-phishing-response |

## Residual exposure

Push-based factors remain enabled for two legacy applications covered by an
exception. Report rate is not measured, so the effectiveness of the training is
inferred from click rate alone.
