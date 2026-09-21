---
id: rsk-ai-assistant-data-leakage
type: risk
title: Merchant Data Reaching a Third-Party AI Assistant
description: 'Support and engineering staff paste merchant data into assistants Acme does not
  run, where retention, training use and jurisdiction are the supplier''s decision rather than
  ours.

  '
status: active
owner: role-ciso
domains:
- data-security
- awareness
related:
- da-merchant-pii
- pol-data-protection
- std-data-protection-controls
systems:
- google-workspace
impact: medium
likelihood: high
severity: high
treatment: tbd
root_causes:
- human-error
- inadequate-monitoring
risk_category:
  principle: compliance-risk
  category1: privacy
  category2: unlawful-processing
tracker: https://acme.atlassian.net/browse/SEC-455
last_reviewed: '2026-09-01'
next_review: '2026-10-15'
---

# Merchant Data Reaching a Third-Party AI Assistant

## The scenario

Somebody pastes a merchant record, a log extract or a support transcript into an
assistant Acme has no contract with. What happens to it then is the supplier's
decision: how long it is kept, whether it trains a model, and which jurisdiction
it sits in.

## Why the treatment is `tbd`

The committee has not decided, and saying so is more honest than writing
`mitigate` and doing nothing. The choice is between blocking the category at the
edge, contracting with one provider so there is a sanctioned place to go, or
accepting it with guidance — and it is on the agenda for the November meeting.

`tbd` is the state that makes the decision visible instead of letting an
undecided risk sit in the register looking handled.
