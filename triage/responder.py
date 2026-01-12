import os
import logging

# Resolve project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "soc_triage.log")

# Ensure logs directory exists
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

def execute_response(alert, risk_result, decision):
    message = (
        f"AlertType={alert['alert_type']} | "
        f"SourceIP={alert['source_ip']} | "
        f"Severity={risk_result['severity']} | "
        f"Action={decision['action']} | "
        f"Reasons={'; '.join(risk_result['reasons'])}"
    )

    if decision["action"] == "BLOCK_AND_ESCALATE":
        logging.warning(f"[BLOCKED IP] {message}")

    elif decision["action"] in ["ESCALATE", "NOTIFY_SOC"]:
        logging.info(f"[SOC ALERT] {message}")

    else:
        logging.info(f"[LOGGED] {message}")
