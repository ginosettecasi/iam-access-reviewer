import os
import sys
from unittest.mock import Mock

# Add repository root to sys.path so that utils can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def test_check_user_compliance_no_mfa():
    dummy_user = {"UserName": "testuser"}
    dummy_client = Mock()
    dummy_client.list_mfa_devices.return_value = {"MFADevices": []}

    from utils import check_user_compliance
    issues = check_user_compliance(dummy_client, dummy_user, stale_threshold_days=180)
    assert any("No MFA enabled" in issue["message"] for issue in issues)
