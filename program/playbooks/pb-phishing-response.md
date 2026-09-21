---
id: pb-phishing-response
type: playbook
title: Phishing and Credential Compromise Response
description: 'What to do when a phishing message is reported or a credential compromise is suspected,
  from first report to closure.

  '
status: active
owner: role-secops-analyst
domains:
- ir
capabilities:
- ir.incident-playbooks
related:
- inc-finance-credential-phishing
- std-incident-response
- std-logging-monitoring
- thr-credential-phishing
systems:
- crowdstrike-falcon
- elastic-siem
- okta
- pagerduty
- slack
last_reviewed: '2026-07-01'
next_review: '2027-07-01'
---

# Phishing and Credential Compromise Response

## Trigger

Any of: a reported phishing message, an impossible-travel or MFA-fatigue alert,
an endpoint detection following a link click, or a person saying "I think I
entered my password on something".

## First ten minutes

The order matters. Containment before investigation.

1. **Assume compromise.** If credentials were entered anywhere, treat the
   account as compromised. Do not wait for confirmation.
2. **Revoke sessions** in `okta` — not just a password reset. A password
   reset leaves a live session working.
3. **Suspend the account** if the user does not need it in the next hour.
4. **Isolate the device** in `crowdstrike-falcon` if a link was opened or
   an attachment run.
5. **Declare** in `pagerduty` at severity `high`. This opens the incident
   channel in `slack` automatically.

## Investigation

| Question | Where to look |
|---|---|
| When did the attacker authenticate? | Identity provider system log |
| What did the session reach? | Application access logs, SIEM |
| Was anything exported or changed? | Merchant portal, drive, ticketing audit logs |
| Was a payment or bank detail changed? | Finance systems — escalate to the CTO if yes |
| Were other people targeted? | Mail logs for the same sender, domain, or subject |

Set the search window from the phishing message delivery time, not from the
report time. In `inc-finance-credential-phishing` those were 50 minutes
apart.

## Eradication and recovery

1. Reset credentials and re-enrol authentication factors in person or over
   video — never over the same channel that was compromised.
2. Remove the message from all mailboxes, not only the reporter's.
3. Block the sending domain and any look-alike registered near it.
4. Restore the device from a rebuild if anything was executed.
5. Return the account to service only after the factor re-enrolment is
   confirmed.

## Communication

| Audience | When | Who |
|---|---|---|
| Incident channel | Immediately | Analyst |
| CISO | On declaration | Analyst |
| Affected person's manager | Within the hour | Analyst |
| Merchants | Only if their data was reached | CISO with Legal |
| Supervisory authority | Only on a personal data breach, 72-hour clock | Legal |

Do not send a company-wide warning until the message is removed from mailboxes.
Warning first causes people to go looking for it.

## Closure

- Postmortem required if severity was `high` or above (`std-incident-response` 7.4).
- Feed the message into the next phishing simulation.
- Record whether detection or the human report came first. In the last
  incident the human was 72 minutes faster, and that number drove a detection
  change.
