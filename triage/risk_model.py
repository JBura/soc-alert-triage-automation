import os
import yaml

# Resolve project root directory safely
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(BASE_DIR, "config", "thresholds.yaml")

with open(CONFIG_PATH, "r") as f:
    CONFIG = yaml.safe_load(f)

def evaluate_failed_login_risk(alert, threat_intel_hit=False, external_source=True):
    reasons = []
    likelihood = 0
    impact = 0

    rules = CONFIG["failed_login"]

    # Likelihood
    if threat_intel_hit:
        likelihood += rules["likelihood"]["threat_intel_hit"]
        reasons.append("Source IP found in threat intelligence")

    if alert["attempt_count"] >= 10:
        likelihood += rules["likelihood"]["high_attempt_count"]
        reasons.append("High number of failed login attempts")

    if alert["time_window_minutes"] <= 5:
        likelihood += rules["likelihood"]["rapid_attempts"]
        reasons.append("Rapid login attempts detected")

    # Impact
    if alert["account_type"] == "admin":
        impact += rules["impact"]["admin_account"]
        reasons.append("Admin account targeted")

    if alert["asset_type"] == "server":
        impact += rules["impact"]["server_asset"]
        reasons.append("Server asset targeted")

    if external_source:
        impact += rules["impact"]["external_source"]
        reasons.append("Login attempts from external source")

    risk_score = likelihood + impact
    severity = determine_severity(risk_score)

    return {
        "likelihood": likelihood,
        "impact": impact,
        "risk_score": risk_score,
        "severity": severity,
        "reasons": reasons
    }

def determine_severity(score):
    levels = CONFIG["severity_levels"]

    if score >= levels["critical"]:
        return "CRITICAL"
    elif score >= levels["high"]:
        return "HIGH"
    elif score >= levels["medium"]:
        return "MEDIUM"
    return "LOW"
