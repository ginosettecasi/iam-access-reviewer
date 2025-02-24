import datetime
from jinja2 import Template

def generate_report(issues, report_date):
    template_str = """
IAM Access Review Report (Generated: {{ report_date }})
{% if issues|length == 0 %}
✅ No issues found. All IAM users are compliant.
{% else %}
⚠️ {{ issues|length }} issue(s) found:
------------------------------------
{% for item in issues %}
User: {{ item.user }}
{% for issue in item.issues %}
   - ❌ {{ issue.message }} [Severity: {{ issue.severity }}]
     Recommendation: {{ issue.recommendation }}
{% endfor %}
------------------------------------
{% endfor %}
{% endif %}
"""
    template = Template(template_str)
    return template.render(issues=issues, report_date=report_date)

def check_user_compliance(iam_client, user, stale_threshold_days):
    issues = []
    user_name = user["UserName"]

    # Check if the user has MFA enabled
    mfa_response = iam_client.list_mfa_devices(UserName=user_name)
    mfa_devices = mfa_response.get("MFADevices", [])
    if not mfa_devices:
        issues.append({
            "message": "No MFA enabled",
            "severity": "Critical",
            "recommendation": "Enable MFA for all users immediately."
        })

    # Check for inactive accounts (stale password)
    password_last_used = user.get("PasswordLastUsed")
    if password_last_used:
        days_since_last_used = (datetime.datetime.utcnow() - password_last_used.replace(tzinfo=None)).days
        if days_since_last_used > stale_threshold_days:
            issues.append({
                "message": f"Stale account (last used {days_since_last_used} days ago)",
                "severity": "Warning",
                "recommendation": "Review account activity and disable if necessary."
            })
    else:
        issues.append({
            "message": "No record of password usage (possible inactive account)",
            "severity": "Warning",
            "recommendation": "Review the user account for activity."
        })

    # Check for admin privileges by inspecting attached policies
    policies = iam_client.list_attached_user_policies(UserName=user_name).get("AttachedPolicies", [])
    for policy in policies:
        if "AdministratorAccess" in policy.get("PolicyName", ""):
            issues.append({
                "message": "User has AdministratorAccess policy",
                "severity": "Critical",
                "recommendation": "Review the necessity of admin privileges."
            })
            break

    return issues
