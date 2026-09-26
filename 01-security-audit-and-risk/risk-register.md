# Risk Register

## Scenario

I evaluated risks for a fictional bank operating with on-premises and remote employees, individual and commercial customers, third-party marketing relationships, and financial-regulatory obligations.

## Risk Evaluation Method

Each risk was evaluated using:

- **Likelihood:** probability that a vulnerability could be exploited.
- **Severity:** potential business impact.
- **Priority:** calculated as `Likelihood × Severity`.

## Risks Assessed

| Risk | Description | Likelihood | Severity | Priority |
|---|---|---:|---:|---:|
| Business email compromise | Employee may be tricked into sharing confidential information | 2 | 2 | 4 |
| Compromised user database | Customer data is poorly encrypted | 2 | 3 | 6 |
| Financial records leak | Backup database server is publicly accessible | 3 | 3 | 9 |
| Theft | Bank safe is left unlocked | 1 | 3 | 3 |
| Supply-chain disruption | Delivery delays caused by natural disasters | 1 | 2 | 2 |

## Key Finding

The publicly accessible financial-record backup received the highest priority score because both likelihood and potential impact were high. The exercise demonstrated how a structured risk matrix helps security teams prioritize remediation instead of treating every risk as equally urgent.

## Skills Demonstrated

Risk identification, likelihood and severity assessment, risk prioritization, business-impact analysis, and security documentation.
