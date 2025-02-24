from unittest.mock import Mock

def test_check_user_compliance_no_mfa():
    dummy_user = {"UserName": "testuser"}
    dummy_client = Mock()
    dummy_client.list_mfa_devices.return_value = {"MFADevices": []}

    from utils import check_user_compliance
    issues = check_user_compliance(dummy_client, dummy_user, stale_threshold_days=180)
    assert any("No MFA enabled" in issue["message"] for issue in issues)
