# Risk Register

This register summarizes the security risks identified during the SSH brute-force detection assessment. Risk ratings are based on the likelihood of occurrence and the potential impact on the target system.

| Risk ID | Finding | Likelihood (1-5) | Impact (1-5) | Risk Score | Risk Level | Owner | Status |
|----------|---------|------------------|--------------|------------|------------|-------|--------|
| R-001 | Repeated failed SSH login attempts detected | 5 | 2 | 10 | Low | System Administrator | Open |
| R-002 | SSH brute-force attack against user account | 5 | 5 | 25 | High | System Administrator | Open |
| R-003 | Weak password authentication policy could allow credential guessing | 4 | 5 | 20 | High | System Administrator | Recommended |
| R-004 | No protection against repeated authentication attempts (e.g., Fail2Ban) | 4 | 4 | 16 | High | Security Team | Recommended |
| R-005 | Internet-exposed SSH service increases attack surface | 3 | 4 | 12 | Medium | Network Administrator | Under Review |
| R-006 | Continuous brute-force activity may lead to unauthorized system access if valid credentials are compromised | 5 | 5 | 25 | Critical | Security Team | Open |

---

## Risk Rating Scale

| Score | Risk Level |
|--------|------------|
| 1 – 5 | Low |
| 6 – 10 | Medium |
| 11 – 15 | High |
| 16 – 25 | Critical |

---

## Recommended Actions

- Review SSH authentication logs regularly.
- Enforce strong password policies for all user accounts.
- Enable multi-factor authentication where possible.
- Deploy Fail2Ban or similar tools to block repeated failed login attempts.
- Restrict SSH access to trusted IP addresses whenever practical.
- Monitor authentication events continuously through centralized logging.

---

## Overall Risk

The assessment identified one active brute-force attack that generated a **Critical** overall risk rating. Although the attack occurred in a controlled lab environment, the same behavior on a production server could lead to unauthorized access if weak credentials are used. Implementing stronger authentication controls and automated protection mechanisms would significantly reduce this risk.
