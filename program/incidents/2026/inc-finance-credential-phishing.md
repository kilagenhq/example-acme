---
id: inc-finance-credential-phishing
type: incident
title: Credential Phishing of a Finance Account
description: 'An attacker phished a finance team member through a real-time proxy, relayed the
  TOTP code, and held a valid session for 47 minutes before it was terminated.

  '
status: active
publish: none
owner: role-ciso
domains:
- ir
related:
- dec-phishing-resistant-authentication
- pb-phishing-response
- rsk-workforce-account-takeover
- thr-credential-phishing
systems:
- crowdstrike-falcon
- elastic-siem
- okta
severity: high
occurred: '2026-01-11'
source_of_truth: https://drive.acme.example/security/ir/2026-001-post-mortem
resolved: '2026-01-12'
---

# Credential Phishing of a Finance Account

## What happened

On 11 January 2026 a finance team member was phished through a real-time proxy
that captured the password and relayed the TOTP prompt. The attacker held a
valid session for 47 minutes, opened the merchant portal, exported the merchant
list, and submitted a settlement bank account change.

## Impact

No cardholder data was accessed and no payment was diverted. The bank account
change required a second approval the attacker did not have, which is the
control that turned this from a loss into an incident report. One merchant list
left the environment.

The full timeline, the SIEM exports and the forensic notes are in the incident
record linked from `source_of_truth`. They are not in this repository: they
carry personal data, and `publish: none` is not a confidentiality control.

## What changed

Four things, each of which is a document rather than a promise:

- `dec-phishing-resistant-authentication` — TOTP was replaced by phishing-resistant
  factors across the workforce. This incident is why, and it supersedes
  `dec-totp-second-factor`.
- `gap-mfa-push-factors` — push and TOTP factors stayed enabled for six weeks
  after the decision. Found here, remediated on 2026-02-28.
- `pb-phishing-response` — the playbook gained the step that was improvised on
  the day: revoke the session before resetting the password, because a reset
  alone leaves the stolen session live.
- `rsk-workforce-account-takeover` — rescored from `high` to `critical`. The
  register said this was unlikely; it happened.

## What did not change

The second approval on settlement account changes, which worked. It is recorded
here so that a future review of that control knows it has been tested for real.
