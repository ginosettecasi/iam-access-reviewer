#!/usr/bin/env python3
import os
import json
import boto3
import datetime
import argparse
from utils import check_user_compliance, generate_report

def load_config(config_file):
    with open(config_file, 'r') as f:
        return json.load(f)

def main():
    parser = argparse.ArgumentParser(description="IAM Access Reviewer & Compliance Auditor")
    parser.add_argument("--provider", required=True, help="IAM provider to audit (aws, forgerock, ldap)")
    args = parser.parse_args()

    provider = args.provider.lower()
    issues = []

    if provider == "aws":
        # Load AWS config
        config = load_config("config/aws_config.json")
        region = config.get("region", "us-east-1")
        stale_threshold_days = config.get("stale_threshold_days", 180)

        iam_client = boto3.client("iam", region_name=region)
        # List IAM users
        response = iam_client.list_users()
        users = response.get("Users", [])

        for user in users:
            user_issues = check_user_compliance(iam_client, user, stale_threshold_days)
            if user_issues:
                issues.append({
                    "user": user["UserName"],
                    "issues": user_issues
                })

    elif provider == "forgerock":
        # Simulated Forgerock audit using dummy data
        simulated_users = [
            {
                "UserName": "jane_forgerock",
                "MFAEnabled": False,
                "LastLogin": "2025-02-01",  # YYYY-MM-DD format
                "Role": "admin"
            },
            {
                "UserName": "john_forgerock",
                "MFAEnabled": True,
                "LastLogin": "2025-02-20",  # Recent login
                "Role": "user"
            }
        ]
        for user in simulated_users:
            user_issues = []
            if not user.get("MFAEnabled"):
                user_issues.append("No MFA enabled")
            # Check for stale accounts (if last login > 30 days ago)
            last_login_date = datetime.datetime.strptime(user["LastLogin"], "%Y-%m-%d")
            days_since_last_login = (datetime.datetime.utcnow() - last_login_date).days
            if days_since_last_login > 30:
                user_issues.append(f"Stale account (last login {days_since_last_login} days ago)")
            if user.get("Role") == "admin":
                user_issues.append("User has admin privileges")
            if user_issues:
                issues.append({
                    "user": user["UserName"],
                    "issues": user_issues
                })

    else:
        print(f"Provider '{provider}' is not supported in this version.")
        return

    # Generate report
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    report_filename = f"reports/iam_report_{now}.txt"
    os.makedirs("reports", exist_ok=True)
    report_content = generate_report(issues, now)
    with open(report_filename, "w") as f:
        f.write(report_content)

    print(f"IAM Audit Report generated: {report_filename}")
    print(report_content)

if __name__ == "__main__":
    main()
