---
id: gl-detection-writing
type: guideline
title: Detection Writing Guideline
description: 'Recommended practice for writing, testing and retiring detection rules so that
  the alert queue stays believable.

  '
status: active
owner: role-secops-analyst
domains:
- secops
capabilities:
- secops.detection-engineering
related:
- pro-vulnerability-triage
- std-logging-monitoring
systems:
- elastic-siem
last_reviewed: '2026-07-15'
next_review: '2027-07-15'
---

# Detection Writing Guideline

## The test a rule must pass

Before writing the query, answer three questions in the rule's description:

1. **What would an analyst do at 03:00 when this fires?** If the answer is
   "look at it and close it", the rule is a report, not an alert.
2. **What is the expected volume?** A rule expected to fire more than twice a
   week is a dashboard.
3. **What legitimate activity looks the same?** If you cannot name it, you have
   not looked hard enough, and the first false positive will arrive within a
   day.

## Writing

- Start from a behaviour, not a tool. "MFA prompt approved after five denials"
  survives a change of identity provider; a rule keyed to a specific event id
  does not.
- Bound every rule in time and scope. An unbounded rule is a cost and a
  latency problem before it is a detection.
- Prefer one rule with clear intent over three near-duplicates, which drift
  apart and are tuned separately.

## Testing

- Test against replayed data from a real window that contains the behaviour,
  and against a window that does not.
- Record the expected true positive and the observed false positives in the
  rule's own header. That is what makes retirement possible later.
- A rule reaches production only through a pull request with a second reviewer,
  as with any other code.

## Tuning and retirement

| Signal | Action |
|---|---|
| Three false positives from one rule | Tuning ticket, owner assigned |
| Ninety days with no true positive | Review: retire, or document why it stays |
| Analyst closes without reading | Retire it — it is training people to ignore alerts |
| Fires only during known maintenance | Add the suppression window, do not weaken the logic |

## What this guideline does not cover

Coverage measurement. Acme counts rules, not techniques, which says how much
has been written and nothing about what it would catch. Purple teaming is what
would answer that, and Acme does none.
