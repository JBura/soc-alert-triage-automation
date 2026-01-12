import json
from datetime import datetime

REQUIRED_FIELDS = {
    "alert_type": str,
    "source_ip": str,
    "username": str,
    "account_type": str,
    "asset_type": str,
    "attempt_count": int,
    "time_window_minutes": int,
    "timestamp": str
}

def load_alert(file_path):
    with open(file_path, "r") as f:
        alert = json.load(f)

    validate_alert(alert)
    return alert

def validate_alert(alert):
    for field, field_type in REQUIRED_FIELDS.items():
        if field not in alert:
            raise ValueError(f"Missing required field: {field}")

        if not isinstance(alert[field], field_type):
            raise ValueError(
                f"Invalid type for field '{field}'. "
                f"Expected {field_type.__name__}"
            )

    # Validate timestamp format
    try:
        datetime.fromisoformat(alert["timestamp"].replace("Z", ""))
    except ValueError:
        raise ValueError("Invalid timestamp format. Use ISO 8601.")

    if alert["alert_type"] != "failed_login":
        raise ValueError("Unsupported alert type")

    if alert["attempt_count"] < 1:
        raise ValueError("Attempt count must be >= 1")
