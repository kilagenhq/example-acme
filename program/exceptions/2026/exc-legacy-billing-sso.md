---
id: exc-legacy-billing-sso
type: exception
title: Legacy Billing Application Without Single Sign-On
description: 'The legacy billing application authenticates with local credentials rather than
  through the identity provider, pending its replacement.

  '
owner: role-it-manager
domains:
- iam
related:
- rsk-workforce-account-takeover
- std-access-control
systems:
- 1password
- okta
approved_by:
- role-ciso
compensating_controls:
- Access limited to four named finance users, reviewed monthly against the HR record
- The application holds no cardholder data; merchant PII is read-only
risk_severity: medium
expires: '2026-12-31'
requirement: std-access-control#1.3
---

# Legacy Billing Application Without Single Sign-On

## Deviation

`std-access-control` 1.3 requires applications to authenticate against the
identity provider. The legacy billing application, used by four people in
Finance Operations, supports only local username and password authentication.

## Why it was granted

Granted 2026-07-01 by the CISO and expiring 2026-12-31 — exactly the six months
`role-ciso` can authorise. A day longer would have gone to the CTO.

The application is being replaced as part of the finance systems migration,
with cutover planned for the fourth quarter. Building a SAML integration for a
system due to be retired would cost more than the exposure it removes, and the
vendor has confirmed no SSO support on the current version.

## Compensating controls

| Control | Detail |
|---|---|
| Credential storage | Individual credentials held in `1password`, no sharing |
| Password policy | 20-character minimum, unique, rotated on any departure |
| Access scope | Four named users, reviewed monthly rather than quarterly |
| Monitoring | Application logs forwarded to the SIEM with a failed-login detection |
| Network | Reachable only from managed devices |

## Residual risk

`medium`. The account cannot be centrally disabled at the moment of
offboarding, so departure handling depends on the manual step in
`rb-offboard-user` rather than on the identity provider. This is the specific
reason the residual exposure on `rsk-workforce-account-takeover` has not yet
fallen to `high`.

## Expiry and review

Expires 2026-12-31 and will not be renewed: if the migration slips, the
application is disconnected rather than the exception extended. Reviewed at the
November access review.
