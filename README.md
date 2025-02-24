# IAM Access Reviewer & Compliance Auditor

## Overview
This project automates IAM user access reviews and compliance audits. It supports multiple providers:
- **AWS IAM** (real integration)
- **ForgeRock** (simulated)
- **LDAP** (simulated)

The tool checks for issues such as missing MFA, stale accounts, weak password policies, and excessive privileges. It generates a detailed report that includes severity levels and recommendations for remediation.

## Features
- **Multi-Provider Support:** AWS, simulated ForgeRock, and LDAP.
- **Rich Reporting:** Issues include severity (Critical/Warning) and remediation recommendations.
- **Automated Testing & Linting:** Uses Pytest and Flake8 to ensure code quality.
- **Logging:** Built-in logging for troubleshooting.
- **CI/CD with GitHub Actions:** Automated audit runs and artifact uploads.
- **Artifact Uploads:** Audit reports are saved as artifacts for review.

## Setup & Usage

### Running Locally
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/iam-access-reviewer.git
   cd iam-access-reviewer
2. **Install dependencies:**
   ```bash
   Copy
   pip install -r requirements.txt
3. **Run an audit:**
For AWS (ensure your AWS credentials are set):
   ```bash
   Copy
   python iam_audit.py --provider aws
For simulated ForgeRock:
   ```bash
   Copy
   python iam_audit.py --provider forgerock
