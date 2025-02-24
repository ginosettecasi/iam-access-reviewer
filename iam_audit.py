#!/usr/bin/env python3
import os
import json
import boto3
import datetime
import argparse
import logging
from utils import check_user_compliance, generate_report

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

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
        logger.info("Running AWS audit")
        config = load_config("config/aws_config.json")
        region = config.get("region", "us-east-2")
        stale_threshold_days = config.get("stale_threshold_days", 180)

        iam_client = boto3.client("iam", region_name=region)
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
        logger.info("Running simulated ForgeRock audit")
        simulated_users = [
            {
                "UserName": "jane_forgerock",
                "MFAEnabled": False,
                "LastLogin": "2025-02-01",
                "Role": "admin"
            },
            {
                "UserName": "john_forgerock",
                "MFAEnabled": True,
                "LastLogin": "2025-02-20",
                "Role": "user"
            }
        ]
        for user in simulated_users:
            user_issues = []
            if not user.get("MFAEnabled"):
                user_issues.append({
                    "message": "No MFA enabled",
                    "severity": "Critical",
                    "recommendation": "Enable MFA for all users immediately."
                })
            last_login_date = datetime.datetime.strptime(user["LastLogin"], "%Y-%m-%d")
            days_since_last_login = (datetime.datetime.utcnow() - last_login_date).days
            if days_since_last_login > 30:
                user_issues.append({
                    "message": f"Stale account (last login {days_since_last_login} days ago)",
                    "severity": "Warning",
                    "recommendation": "Prompt a password update."
                })
            if user.get("Role") == "admin":
                user_issues.append({
                    "message": "User has admin privileges",
                    "severity": "Critical",
                    "recommendation": "Review the necessity of admin rights."
                })
            if user_issues:
                issues.append({
                    "user": user["UserName"],
                    "issues": user_issues
                })

    elif provider == "ldap":
        logger.info("Running simulated LDAP audit")
        simulated_ldap_users = [
            {
                "UserName": "ldap_user1",
                "PasswordPolicy": "Weak",
                "LastChange": "2025-02-01"
            },
            {
                "UserName": "ldap_user2",
                "PasswordPolicy": "Strong",
                "LastChange": "2025-02-20"
            }
        ]
        for user in simulated_ldap_users:
            user_issues = []
            if user["PasswordPolicy"] == "Weak":
                user_issues.append({
                    "message": "Weak LDAP password policy",
                    "severity": "Critical",
                    "recommendation": "Enforce stronger password policies."
                })
            last_change_date = datetime.datetime.strptime(user["LastChange"], "%Y-%m-%d")
            days_since_change = (datetime.datetime.utcnow() - last_change_date).days
            if days_since_change > 90:
                user_issues.append({
                    "message": f"Password last changed {days_since_change} days ago",
                    "severity": "Warning",
                    "recommendation": "Prompt a password update."
                })
            if user_issues:
                issues.append({
                    "user": user["UserName"],
                    "issues": user_issues
                })
    else:
        logger.error(f"Provider '{provider}' is not supported.")
        return

    now = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    report_filename = f"reports/iam_report_{now}.txt"
    os.makedirs("reports", exist_ok=True)
    report_content = generate_report(issues, now)
    with open(report_filename, "w") as f:
        f.write(report_content)

    logger.info(f"IAM Audit Report generated: {report_filename}")
    logger.info(report_content)

if __name__ == "__main__":
    main()
