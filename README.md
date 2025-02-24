# IAM Access Reviewer & Compliance Auditor

## Overview

The **IAM Access Reviewer & Compliance Auditor** is a security automation tool that simplifies **user access reviews** and ensures **compliance with industry standards** such as **PCI DSS, ISO 27001, and FedRAMP**. It provides structured IAM audits across **AWS IAM, ForgeRock, and LDAP environments**, detecting excessive permissions, inactive accounts, and security misconfigurations.

This project demonstrates a **real-world enterprise IAM security solution**, aligning with **Visa’s security automation needs** and showcasing expertise in **IAM governance, compliance enforcement, and security engineering**.

## Key Features

- **Multi-Provider Support** – Integrates with **AWS IAM (real implementation)** and simulates **ForgeRock & LDAP** to demonstrate cross-platform IAM security automation.
- **Automated IAM Audits** – Identifies **excessive privileges, missing MFA, and inactive accounts** to mitigate security risks.
- **Regulatory Compliance Enforcement** – Validates IAM configurations against **PCI DSS, ISO 27001, and least privilege policies**.
- **Comprehensive Reporting** – Generates **structured audit reports** with **severity levels and remediation recommendations**.
- **CI/CD Integration with GitHub Actions** – Automates IAM security audits on every commit, ensuring **continuous compliance monitoring**.
- **Test-Driven Development (TDD)** – Uses **Pytest-based unit tests** to maintain audit accuracy and ensure code reliability.

## How It Works

1. **Collects IAM user data** from **AWS, ForgeRock, or LDAP**.
2. **Analyzes permissions and access levels** to detect **overprivileged users and inactive accounts**.
3. **Performs compliance checks** based on **PCI DSS, ISO 27001, and least privilege policies**.
4. **Generates a structured IAM audit report** detailing security risks and recommended remediation actions.
5. **Runs continuously via GitHub Actions**, ensuring that IAM security remains **up-to-date and aligned with compliance frameworks**.

## GitHub Actions Integration

This project is fully **automated** using **GitHub Actions**, enabling a streamlined IAM audit pipeline. Every **code commit** automatically triggers:

- **Unit Testing with Pytest** – Ensures compliance validation accuracy.
- **IAM Audit Execution** – Fetches user data and applies IAM security checks.
- **Audit Report Generation & Upload** – Stores security reports as artifacts for review.

By leveraging **CI/CD best practices**, this automation reduces **manual IAM security overhead** and provides **real-time compliance enforcement**.

## Installation & Usage

### **1. Clone the Repository**
```bash
git clone https://github.com/ginosettecasi/iam-access-reviewer.git
cd iam-access-reviewer
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Run an IAM Audit**
- **For AWS IAM (Requires AWS Credentials):**
  ```bash
  python iam_audit.py --provider aws
  ```
- **For Simulated ForgeRock:**
  ```bash
  python iam_audit.py --provider forgerock
  ```
- **For Simulated LDAP:**
  ```bash
  python iam_audit.py --provider ldap
  ```

### **4. View Audit Reports**
The tool generates an IAM security audit report in the `reports/` directory:
```bash
cat reports/iam_report_YYYY-MM-DD.txt
```

## Example Audit Report Output
```
IAM Access Review Report (Generated: 2025-02-23)

⚠️ 3 Issues Found:
------------------------------------
1️⃣ User: JohnDoe (AWS IAM)
   - ❌ Admin privileges assigned but user role is "Support"
   - 🔥 Recommended: Downgrade to appropriate least privilege access

2️⃣ User: JaneAdmin (ForgeRock)
   - ❌ No Multi-Factor Authentication (MFA) enabled
   - 🔥 Recommended: Enforce MFA through ForgeRock policy

3️⃣ User: test_user (LDAP)
   - ❌ Last login: 380 days ago (Inactive Account)
   - 🔥 Recommended: Disable or review account activity justification

✅ Compliance Status: PCI DSS ✅ | ISO 27001 ❌ (MFA Policy Violation)
```

This project **demonstrates real-world security automation skills**, making it a valuable addition to an **enterprise IAM security framework**.

## GitHub Repository

Full source code, setup instructions, and workflow automation details can be found here:  
**[GitHub Repository: IAM Access Reviewer & Compliance Auditor](https://github.com/ginosettecasi/iam-access-reviewer)**

## License

This project is licensed under the **MIT License**.

---
