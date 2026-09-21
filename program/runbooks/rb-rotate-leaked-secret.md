---
id: rb-rotate-leaked-secret
type: runbook
title: Rotate a Leaked Secret
description: 'Treat a credential that has reached a remote repository as compromised: rotate
  it within four hours, check for use, and remove it from history.

  '
status: active
owner: role-appsec-eng
domains:
- appsec
capabilities:
- appsec.secrets-scanning
related:
- std-secure-development
- thr-supply-chain-compromise
systems:
- aws-kms
- github-advanced-security
- gitleaks
last_reviewed: '2026-07-30'
next_review: '2027-07-30'
---

# Rotate a Leaked Secret

## When to run

A secret has been found in a remote repository — by push protection, the weekly
sweep, or a person noticing. `std-secure-development` 2.4 sets four hours from
detection to rotation.

## The rule that governs every step

**Rotate first, investigate second.** A secret that reached a remote is
compromised regardless of whether the repository is private, whether it was
force-pushed away, or how briefly it was there.

## Steps

1. **Identify what it opens.** Read the secret's format and scope. If this
   takes more than ten minutes, rotate anyway and continue investigating after.
2. **Rotate at the source.** Issue the new credential in the system that owns
   it, deploy it, and confirm the service works on the new value before
   revoking the old one — unless the exposure is public, in which case revoke
   immediately and accept the outage.
3. **Revoke the old value.** Not merely superseded: revoked, so that the old
   value fails.
4. **Check for use.** Search the logs for the exposed credential's identifier
   for the whole window between the commit date and the revocation. Any use
   from an unexpected source makes this an incident under
   `std-incident-response`, not a runbook.
5. **Remove from history.** Rewriting history is the last step, not the first.
   It does not undo the exposure, and doing it first destroys the evidence
   needed for step 4.
6. **Fix the cause.** A secret in a repository means it had nowhere better to
   live. Move it to the secret store and open a ticket if the pattern will
   recur.
7. **Record.** Note the detection time, the rotation time and the outcome of
   step 4 in the ticket.

## Verification

- The old credential fails against its service.
- The new credential is in the secret store, not in the repository.
- The log search covering the exposure window is attached to the ticket.

## Escalate when

- The credential opened anything in the cardholder data environment.
- Step 4 shows use from an unrecognised source.
- Rotation cannot be completed within four hours.

All three go to the CISO immediately and are handled as incidents.
