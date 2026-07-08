#!/usr/bin/env python3

import subprocess
import re
import json
from collections import defaultdict
from datetime import datetime

SSH_TARGET = "user@172.16.243.132"
REMOTE_COMMAND = "cat /var/log/auth.log /var/log/auth.log.1 2>/dev/null"

OUTPUT = "../logs/security_alerts.json"

pattern = re.compile(
    r"Failed password for (?:invalid user )?(\S+) from (\d+\.\d+\.\d+\.\d+)"
)

result = subprocess.run(
    ["ssh", SSH_TARGET, REMOTE_COMMAND],
    capture_output=True,
    text=True
)

failed_attempts = defaultdict(int)

for line in result.stdout.splitlines():

    match = pattern.search(line)

    if match:
        username = match.group(1)
        ip = match.group(2)

        failed_attempts[(ip, username)] += 1

alerts = []

print("\n========== SSH Detection Summary ==========\n")

for (ip, username), attempts in failed_attempts.items():

    print(f"Source IP : {ip}")
    print(f"Username  : {username}")
    print(f"Attempts  : {attempts}")
    print("-" * 40)

    alerts.append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "source_ip": ip,
        "username": username,
        "attempts": attempts,
        "event": "SSH_BRUTE_FORCE"
    })

with open(OUTPUT, "w") as outfile:
    json.dump(alerts, outfile, indent=4)

print(f"\nSaved {len(alerts)} alerts to {OUTPUT}")
