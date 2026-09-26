# Phishing Alert Ticket

## Alert

A medium-severity alert indicated that an employee may have downloaded and opened a malicious attachment from a phishing email.

## Indicators Reviewed

The message contained several suspicious indicators:

- inconsistency between the sender address, sender name, and the name used in the email body
- grammatical errors in the subject and body
- a password-protected executable attachment
- a file hash previously identified as malicious

## Decision

Based on the combination of phishing indicators and the known-malicious attachment, I documented the findings and **escalated the ticket to a level-two SOC analyst** for further action.

## Security Relevance

This activity demonstrates that SOC triage depends on combining multiple indicators rather than relying on one clue. Sender anomalies, message quality, attachment type, and hash reputation collectively supported the escalation decision.

## Skills Demonstrated

SOC alert triage, phishing analysis, malware indicators, file-hash interpretation, escalation, and ticket documentation.
