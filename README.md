# IAM Access Reviewer & Compliance Auditor

## Overview
This project automates IAM user access reviews and compliance audits. It simulates audits against three providers:
- **AWS** (real integration using boto3)
- **ForgeRock** (simulated dummy data)
- **LDAP** (simulated dummy data)

The tool checks for issues like missing MFA, stale accounts, weak password policies, and excessive privileges. It produces a detailed report with severity levels and remediation recommendations.

## Features
- **Multi-Provider Support:** AWS, simulated ForgeRock, and simulated LDAP.
- **Richer Reporting:** Issues include a message, severity (Critical/Warning), and recommendations.
- **Automated CI/CD:** GitHub Actions runs linting, unit tests, the audit, and uploads the report as an artifact.
- **Detailed Logging:** Uses Python’s logging module for production-quality logs.
- **Unit Testing:** Tests with pytest ensure code quality and proper function behavior.

## Setup & Usage

### Prerequisites
- Python 3.9+
- AWS credentials (if you wish to run the AWS audit) added as GitHub Secrets:
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`
  - `AWS_DEFAULT_REGION` (set to your desired region, e.g. `us-east-2`)

### Running Locally
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
