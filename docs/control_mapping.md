# Control Mapping

## Overview

This document maps the findings identified during the SSH brute-force assessment to commonly used cybersecurity frameworks. The objective is to demonstrate how technical findings can be translated into security controls and compliance requirements.

The mappings below are based on ISO/IEC 27001:2022, the NIST Cybersecurity Framework (CSF 2.0), and CIS Critical Security Controls v8.

---

| Finding | ISO/IEC 27001:2022 | NIST CSF 2.0 | CIS Controls v8 | Recommended Remediation |
|----------|--------------------|--------------|-----------------|-------------------------|
| Repeated failed SSH login attempts | A.8.5 – Secure Authentication | Detect (DE) | Control 8 – Audit Log Management | Monitor authentication logs and investigate repeated failures. |
| SSH brute-force attack detected | A.8.16 – Monitoring Activities | Detect (DE) | Control 13 – Network Monitoring and Defense | Continuously monitor authentication events and investigate suspicious activity. |
| Weak password authentication may allow credential guessing | A.5.17 – Authentication Information | Protect (PR) | Control 5 – Account Management | Enforce strong password policies and regular password reviews. |
| No automated protection against repeated login attempts | A.8.5 – Secure Authentication | Protect (PR) | Control 6 – Access Control Management | Deploy Fail2Ban or similar protection to automatically block repeated failed logins. |
| SSH service exposed to unnecessary attack attempts | A.8.20 – Network Security | Protect (PR) | Control 12 – Network Infrastructure Management | Restrict SSH access using firewall rules, VPN, or trusted IP addresses. |
| High-risk authentication event identified | A.5.24 – Information Security Incident Management Planning and Preparation | Respond (RS) | Control 17 – Incident Response Management | Follow the incident response process, investigate the event, and document actions taken. |

---

## Summary

The assessment identified authentication-related risks that primarily affect access control, monitoring, and incident response.

Implementing stronger authentication controls, centralized monitoring, and automated defensive measures would significantly reduce the likelihood of successful brute-force attacks while improving the organization's ability to detect and respond to security incidents.

The control mappings provided in this document demonstrate how technical findings can be aligned with recognized cybersecurity frameworks and translated into practical remediation actions.
