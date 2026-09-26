# Least-Privilege Data Leak Analysis

## Incident Summary

A sales manager shared access to an internal folder containing unreleased product information, customer analytics, and promotional materials. Access was not revoked after the meeting. Later, a sales representative unintentionally shared the internal-folder link with a business partner, who then posted the link publicly.

## Control Issue

The central control issue was a violation of the **principle of least privilege**. Users retained access to more information than was necessary for their immediate tasks, and the temporary access was not revoked promptly.

## NIST SP 800-53 AC-6

The analysis referenced **AC-6: Least Privilege**, which focuses on providing only the minimum access and authorization required to perform assigned tasks.

## Recommendations

- restrict sensitive resources according to user role
- grant only the minimum required permissions
- use time-limited access where appropriate
- promptly revoke permissions when tasks are complete
- regularly audit user privileges
- maintain activity logs for provisioned accounts
- educate employees on access and sharing policies

## Security Rationale

Applying least privilege would reduce the likelihood that a user could accidentally expose unrelated sensitive information. Regular reviews and timely revocation also reduce the duration of unnecessary access.

## Skills Demonstrated

Least privilege, access control, data-loss prevention, NIST SP 800-53, security recommendations, and policy analysis.
