---
id: std-logging-monitoring
type: standard
title: Logging and Monitoring Standard
description: 'What Acme logs, how long it keeps it, how the record is protected from tampering,
  and how quickly an alert must reach a human.

  '
status: active
owner: role-secops-analyst
domains:
- grc
- secops
- infra
related:
- pol-information-security
- std-incident-response
approved_by:
- role-security-committee
requirements:
- ref: '5.1'
  text: Defined log sources are collected centrally
  how_demonstrated: Coverage report from the platform, showing every defined source, when it last delivered, and what is missing.
  evidence:
  - name: Log source coverage — Q3 2026
    url: https://drive.acme.example/security/secops/2026-Q3-log-coverage.pdf
    collected: '2026-08-31'
    freshness: quarterly
    collector: quarter-end
  frameworks:
    iso_27001:
    - A.8.15
    pci_dss_4_0_1:
    - '10'
    soc2:
    - CC7.2
    nist_csf:
    - DE.CM
    iso_27017:
    - CLD.12.4.5
- ref: '5.2'
  text: Logs are retained for at least twelve months, three months immediately available
  how_demonstrated: Retention configuration and archive policy, from elastic-siem, aws.
  frameworks:
    iso_27001:
    - A.8.15
    pci_dss_4_0_1:
    - '10'
    nist_csf:
    - PR.PS
- ref: '5.3'
  text: The log record is protected against modification and deletion
  how_demonstrated: Bucket policy and access review of the log account, from aws.
  frameworks:
    iso_27001:
    - A.8.15
    pci_dss_4_0_1:
    - '10'
    soc2:
    - CC7.2
- ref: '5.4'
  text: Alerts reach a human within the times set by severity
  how_demonstrated: Time from alert raised to human acknowledgement, by severity, from the on-call tool.
  evidence:
  - name: Alert acknowledgement times by severity
    url: https://drive.acme.example/security/secops/alert-acknowledgement.pdf
    collected: '2026-09-01'
    freshness: monthly
    collector: manual
  frameworks:
    iso_27001:
    - A.8.16
    soc2:
    - CC7.2
    nist_csf:
    - DE.AE
    - RS.MA
- ref: '5.5'
  text: System clocks are synchronised to a common source
  how_demonstrated: Time source configuration, from aws.
  frameworks:
    iso_27001:
    - A.8.17
    pci_dss_4_0_1:
    - '10'
- ref: '5.6'
  text: Administrative actions on critical systems generate an alert
  how_demonstrated: Alert rules on administrative events, from elastic-siem.
version: '1.2'
capabilities:
- secops.alert-triage
- secops.log-management
- secops.siem
last_reviewed: '2026-06-02'
next_review: '2027-06-02'
---

# Logging and Monitoring Standard

## Purpose

Detection is only possible over data that was collected, and an investigation
is only credible over a record that could not have been edited. This standard
covers both.

## Scope

All production systems, the cloud accounts, the identity provider, the edge and
the build environment.

## Requirements

### Collection

5.1 The following source families are collected centrally: cloud audit,
identity provider, edge and WAF, endpoint, application, build, and database
access within the cardholder data environment.

5.2 Logs are retained for at least twelve months, of which the most recent
three are immediately searchable. Acme retains thirteen months hot and
twenty-five in archive, which exceeds the requirement deliberately, to cover an
investigation that starts late.

5.3 Logs are written to an account with separate credentials and a write-once
retention policy. No operator, including a platform administrator, can delete a
log within its retention period.

### Detection and response

5.4 Alerts reach a human within the following times:

| Severity | Acknowledgement | Out of hours |
|---|---|---|
| Critical | 15 minutes | Paged |
| High | 30 minutes | Paged |
| Medium | Next business day | Queued |
| Low | Weekly review | Queued |

5.5 All systems synchronise their clocks to a common time source. Correlation
across sources is worthless without it, and a disputed timeline is worse than
no timeline.

5.6 Administrative actions on the identity provider, the key management service
and the cardholder data environment generate an alert, not merely a log entry.

## Revision History

| Version | Date | Approved by | Change |
|---|---|---|---|
| 1.0 | 2024-08-22 | Security Committee | Initial version |
| 1.1 | 2025-08-19 | Security Committee | Retention raised to thirteen months hot |
| 1.2 | 2026-06-02 | Security Committee | Administrative action alerting added as 5.6 |
