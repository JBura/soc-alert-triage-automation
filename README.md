# SOC Alert Triage & Security Automation Tool

## Overview
This project simulates a **Security Operations Center (SOC) alert triage workflow**.  
It automates the analysis of failed login alerts by enriching events, calculating risk,
assigning severity, and determining response actions.

The goal is to reduce alert fatigue and demonstrate **security automation and blue-team thinking**
using Python.


## Problem Statement
SOC teams receive a high volume of alerts, many of which are low risk or false positives.
Manual triage is time-consuming and inefficient.

This project demonstrates how automation can:
- Prioritize real threats
- Reduce analyst workload
- Improve response consistency


## How It Works (Workflow)

1. Ingests a raw security alert (JSON)
2. Enriches alert context (e.g., threat intelligence hit)
3. Calculates risk using **likelihood + impact**
4. Assigns a severity level (LOW to CRITICAL)
5. Determines an automated response action
6. Logs actions for audit and SOC visibility

RAW ALERT → RISK SCORING → SEVERITY → RESPONSE → LOGGING



## Technologies Used
- Python
- Linux
- JSON
- YAML
- Logging
- Security risk modeling


## Project Structure
Automation/
├── main.py
├── alerts/
│   └── failed_login_sample.json
├── triage/
│   ├── parser.py
│   ├── intel.py
│   ├── risk_model.py
│   ├── decision_engine.py
│   └── responder.py
├── config/
│   └── thresholds.yaml
├── logs/
│   └── soc_triage.log


## Example Output

=== SOC TRIAGE RESULT ===

Severity : CRITICAL
Action : BLOCK_AND_ESCALATE

Reasons:
Source IP found in threat intelligence

High number of failed login attempts

Rapid login attempts detected

Admin account targeted

Server asset targeted

Login attempts from external source


---

## Key Security Concepts Demonstrated
- SOC alert triage
- Risk-based decision making
- Alert enrichment
- Incident response automation
- Defensive programming
- Logging and audit trails

---

## Why This Project Matters
This project reflects **real SOC challenges** and shows how automation can support security analysts
by handling repetitive tasks while keeping response decisions explainable and low-risk.

It is designed to be an **entry-level security automation project** suitable for SOC analyst
and junior security engineering roles.

---

## Author
**Josephat Bura**  
Bachelor of Cyber Security (2025 Graduate)



