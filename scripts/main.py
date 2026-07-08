import subprocess
import sys

print("=" * 60)
print("      AUTOMATED DETECTION & RESPONSE PIPELINE")
print("=" * 60)

steps = [
    ("Detection Engine", "detect.py"),
    ("Risk Assessment Engine", "risk_engine.py"),
    ("Response Engine", "response.py")
]

for name, script in steps:
    print(f"\n[+] Running {name}...")

    result = subprocess.run(
        ["python3", script],
        text=True,
        capture_output=True
    )

    print(result.stdout)

    if result.returncode != 0:
        print(result.stderr)
        print(f"\n[-] {name} failed.")
        sys.exit(1)

print("\n" + "=" * 60)
print("         PIPELINE COMPLETED SUCCESSFULLY")
print("=" * 60)

print("""
Generated Files
---------------
logs/
  ├── security_alerts.json
  ├── risk_assessment.json
  └── response.log

reports/
  ├── incident_report.txt
  └── executive_summary.md
""")
