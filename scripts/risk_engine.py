import json

INPUT = "../logs/security_alerts.json"
OUTPUT = "../logs/risk_assessment.json"

# Load alerts
with open(INPUT, "r") as infile:
    alerts = json.load(infile)

# Calculate risk
for alert in alerts:
    attempts = alert["attempts"]

    if attempts <= 3:
        risk = "LOW"
        score = 25
    elif attempts <= 7:
        risk = "MEDIUM"
        score = 60
    else:
        risk = "HIGH"
        score = 95

    alert["risk_level"] = risk
    alert["risk_score"] = score

# Print results
print("\n========== Risk Assessment ==========\n")

for alert in alerts:
    print(f"IP         : {alert['source_ip']}")
    print(f"Username   : {alert['username']}")
    print(f"Attempts   : {alert['attempts']}")
    print(f"Risk Level : {alert['risk_level']}")
    print(f"Risk Score : {alert['risk_score']}")
    print("-" * 40)

# Save results
with open(OUTPUT, "w") as outfile:
    json.dump(alerts, outfile, indent=4)

print(f"\nRisk assessment saved to {OUTPUT}")
