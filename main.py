from triage.parser import load_alert
from triage.intel import check_ip_reputation
from triage.risk_model import evaluate_failed_login_risk
from triage.decision_engine import decide_action
from triage.responder import execute_response

def main():
    alert = load_alert("alert/failed_login_sample.json")

    intel_result = check_ip_reputation(alert["source_ip"])
    threat_intel_hit = intel_result["malicious"]

    risk_result = evaluate_failed_login_risk(
        alert,
        threat_intel_hit=threat_intel_hit,
        external_source=True
    )

    decision = decide_action(risk_result)

    execute_response(alert, risk_result, decision)

    print("=== SOC TRIAGE RESULT ===")
    print(f"Severity : {risk_result['severity']}")
    print(f"Action   : {decision['action']}")
    print("Reasons:")
    for reason in risk_result["reasons"]:
        print(f" - {reason}")

if __name__ == "__main__":
    main()
