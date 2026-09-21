---
id: gap-mfa-push-factors
type: gap
title: Push and TOTP factors remained enabled after the phishing incident
description: Push and TOTP stayed enabled as fallbacks after the phishing incident, leaving the phishable factor the incident turned on available. Closed 2026-02-28.
owner: role-it-manager
requirement: std-access-control#1.2
source: internal
found: '2026-01-12'
severity: high
tracker: https://acme.atlassian.net/browse/SEC-360
remediated: '2026-02-28'
domains:
- iam
related:
- exc-legacy-billing-sso
- rsk-workforce-account-takeover
- thr-credential-phishing
---

# Push and TOTP factors remained enabled after the phishing incident

Phishing-resistant factors mandated by dec-phishing-resistant-authentication and enforced in the identity provider; the legacy billing application under exc-legacy-billing-sso is unaffected, because it never authenticated through the provider at all.
