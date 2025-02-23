# IAM Access Reviewer & Compliance Auditor

## Overview
This project automates AWS IAM user access reviews and compliance audits. It checks for:
- Users without Multi-Factor Authentication (MFA)
- Inactive or stale accounts (based on last password usage)
- Users with AdministratorAccess policies

The tool generates a comprehensive report for quick review and is integrated with GitHub Actions for continuous automation.

## Features
- **Automated Access Reviews:** Scans AWS IAM users.
- **Compliance Checks:** Verifies MFA configuration, account activity, and excessive privileges.
- **Report Generation:** Outputs an audit report in a human-readable format.
- **CI/CD Integration:** Runs automatically via GitHub Actions on every push or on a schedule.

## Technologies
- **Python** for core logic.
- **Boto3** for AWS IAM integration.
- **Jinja2** for templated report generation.

## Setup & Usage

### Prerequisites
- Python 3.9+
- AWS credentials configured as environment variables or via GitHub repository secrets:
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`
  - `AWS_DEFAULT_REGION`

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/iam-access-reviewer.git
   cd iam-access-reviewer
