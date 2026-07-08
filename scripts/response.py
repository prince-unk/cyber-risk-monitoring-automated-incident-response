import json
from datetime import datetime

INPUT = "../logs/risk_assessment.json"
REPORT = "../reports/incident_report.txt"
SUMMARY = "../reports/executive_summary.md"
LOG = "../logs/response.log"

with open(INPUT, "r") as f:
    alerts = json.load(f)

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(REPORT, "w") as report, \
     open(SUMMARY, "w") as summary, \
     open(LOG, "a") as log:

    report.write("===== INCIDENT REPORT =====\n\n")

    summary.write("# Executive Security Summary\n\n")
    summary.write(f"Generated: {now}\n\n")

    for i, alert in enumerate(alerts, start=1):

        if alert["risk_level"] == "HIGH":
            recommendation = "Immediately investigate source IP. Consider blocking the IP and reviewing SSH configuration."
        elif alert["risk_level"] == "MEDIUM":
            recommendation = "Monitor the source and increase logging."
        else:
            recommendation = "No immediate action required."

        report.write(f"""
Incident ID : INC-{i:03}
Time        : {alert["timestamp"]}
Source IP   : {alert["source_ip"]}
Username    : {alert["username"]}
Attempts    : {alert["attempts"]}
Risk Level  : {alert["risk_level"]}
Risk Score  : {alert["risk_score"]}

Recommendation:
{recommendation}

----------------------------------------
""")

        summary.write(
f"""## Incident INC-{i:03}

- Risk Level: **{alert["risk_level"]}**
- Source IP: {alert["source_ip"]}
- Attempts: {alert["attempts"]}
- Recommendation: {recommendation}

"""
)

        log.write(
f"[{now}] Incident INC-{i:03} processed ({alert['risk_level']})\n"
)

print("Automated response completed.")
print(f"Incident Report : {REPORT}")
print(f"Executive Summary : {SUMMARY}")
print(f"Response Log : {LOG}")
