# Executive Summary

## Overview

A security assessment was conducted to evaluate how effectively SSH brute-force attacks can be detected, analyzed, and reported within a controlled Linux environment.

The assessment focused on monitoring authentication events, identifying suspicious login activity, evaluating the associated security risk, and automatically generating incident documentation.

---

## What Was Tested

The following components were included in the assessment:

- SSH authentication service
- Centralized log collection using rsyslog
- Detection of failed SSH login attempts
- Risk assessment based on attack severity
- Automated incident reporting

A simulated SSH brute-force attack was performed using Hydra to validate the detection and reporting workflow.

---

## Key Findings

The monitoring system successfully identified repeated failed SSH login attempts originating from the attacking system.

The automated workflow was able to:

- Detect suspicious authentication activity.
- Calculate a risk level based on the number of failed login attempts.
- Generate structured security alerts.
- Produce an incident report and executive summary automatically.

The simulated brute-force attack was classified as **High Risk** because of the large number of authentication attempts within a short period.

---

## Business Impact

If similar activity occurred in a production environment and weak credentials were used, an attacker could gain unauthorized access to critical systems.

Potential consequences include:

- Unauthorized access to sensitive information.
- Service disruption.
- Data compromise.
- Increased recovery costs.
- Reputational damage.

Early detection significantly reduces the likelihood of these outcomes by enabling faster investigation and response.

---

## Recommendations

To reduce the risk of successful brute-force attacks, the following controls are recommended:

- Enforce strong password policies.
- Enable Multi-Factor Authentication (MFA) where possible.
- Implement account lockout or rate limiting.
- Deploy tools such as Fail2Ban to block repeated failed login attempts.
- Continuously monitor authentication logs through centralized logging.
- Perform periodic reviews of SSH access policies.

---

## Overall Assessment

The objective of this project was successfully achieved.

The monitoring pipeline detected the simulated attack, evaluated its severity, and automatically generated documentation to support incident response.

Although this project was developed in a laboratory environment, the overall workflow reflects how security events are processed in many organizations—from technical detection through risk assessment to management reporting.
