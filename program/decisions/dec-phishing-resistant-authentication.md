---
id: dec-phishing-resistant-authentication
type: decision
title: Require Phishing-Resistant Authentication
description: 'Decision to require WebAuthn or platform passkeys for all workforce authentication,
  retiring TOTP and push factors, following a credential phishing incident.

  '
status: active
owner: role-ciso
domains:
- iam
related:
- dec-totp-second-factor
- inc-finance-credential-phishing
- rsk-workforce-account-takeover
- std-access-control
systems:
- okta
supersedes:
- dec-totp-second-factor
decided: '2026-01-20'
immutable: true
---

# Require Phishing-Resistant Authentication

## Context

In January 2026 an attacker phished a finance account through a real-time
proxy, capturing both the password and the TOTP code
(`inc-finance-credential-phishing`). The second factor did not fail — it
worked exactly as designed, and was relayed. `dec-totp-second-factor` had anticipated this
and accepted it as a temporary position; the incident ended the temporary
position.

Acme is now 250 people, the identity provider is mature, and hardware key
logistics are a solved problem for a remote workforce.

## Decision

All workforce authentication requires a phishing-resistant factor: WebAuthn
security keys or platform passkeys. TOTP and push are removed as primary
factors. Push is retained only as a step-up for two legacy applications covered
by `exc-legacy-billing-sso`, and lapses when that exception expires.

Every employee receives two security keys, one of which is registered as a
backup and kept off the desk.

## Consequences

**Positive.** The class of attack in the incident stops working: a relayed
assertion is bound to the origin and cannot be replayed against the real one.
It is also what allows `std-access-control` 1.2 to be written as a requirement
rather than an aspiration.

**Negative.** Cost of two keys per employee plus replacements. Onboarding gains
a shipping dependency, which is felt most for contractors. A lost key is a
support event with an identity-proofing burden — the recovery path is itself a
phishing target, and is deliberately manual.

**Rejected alternative.** Requiring keys only for administrative accounts. The
incident account was not administrative, and it still reached merchant data.
