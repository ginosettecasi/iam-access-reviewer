import datetime
from jinja2 import Template

def check_user_compliance(iam_client, user, stale_threshold_days):
    """
    Checks compliance for a given AWS IAM user.
    Returns a list of issues found.
    """
    issues = []
    user_name = user["UserName"]

    # Check if the user has MFA enabled
    mfa_response = iam_client.list_mfa_devices(UserName=user_name)
    mfa_devices = mfa_response.get("MFADevices", [])
    if not mfa_devices:
        issues.append("No MFA enabled")

    # Check for inactive accounts (stale password)
    password_last_used = user.get("PasswordLastUsed")
    if password_last_used:
        days_since_last_used = (datetime.datetime.utcnow() - password_last_used.replace(tzinfo=None)).days
        if days_since_last_used > stale_threshold_days:
            issues.append(f"Stale account (last used {days_since_last_used} days ago)")
    else:
        # If PasswordLastUsed is not set, consider it as never used
        issues.append("No record of password usage (possible inactive account)")

    # Check for admin privileges by inspecting attached policies
    policies = iam_client.list_attached_user_policies(UserName=user_name).get("AttachedPolicies", [])
    for policy in policies:
        if "AdministratorAccess" in policy.get("PolicyName", ""):
            issues.append("User has AdministratorAccess policy")
            break

    return issues

def generate_report(issues, report_date):
    """
    Generates a text report from the issues list using Jinja2 templating.
    """
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
   - ❌ {{ issue }}
{% endfor %}
------------------------------------
{% endfor %}
{% endif %}
"""
    template = Template(template_str)
    return template.render(issues=issues, report_date=report_date)
