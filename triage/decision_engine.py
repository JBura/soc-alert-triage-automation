def decide_action(risk_result):
    severity = risk_result["severity"]

    if severity == "CRITICAL":
        return {
            "action": "BLOCK_AND_ESCALATE",
            "notify": True
        }

    if severity == "HIGH":
        return {
            "action": "ESCALATE",
            "notify": True
        }

    if severity == "MEDIUM":
        return {
            "action": "NOTIFY_SOC",
            "notify": True
        }

    return {
        "action": "LOG_ONLY",
        "notify": False
    }
