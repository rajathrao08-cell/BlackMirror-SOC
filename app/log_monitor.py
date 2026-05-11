def analyze_logs(log_file):

    alerts = []

    with open(log_file, "r") as file:
        logs = file.readlines()

    for log in logs:

        # ---------------- BRUTE FORCE ----------------
        if "FAILED_LOGIN" in log:
            alerts.append({
                "severity": "MEDIUM",
                "message": f"🚨 Brute Force Attempt Detected -> {log.strip()}"
            })

        # ---------------- SQL INJECTION ----------------
        elif "SQL_INJECTION" in log:
            alerts.append({
                "severity": "CRITICAL",
                "message": f"💉 SQL Injection Attempt -> {log.strip()}"
            })

        # ---------------- MALWARE ----------------
        elif "MALWARE_DETECTED" in log:
            alerts.append({
                "severity": "HIGH",
                "message": f"🦠 Malware Activity Detected -> {log.strip()}"
            })

        # ---------------- POWERSHELL ----------------
        elif "POWERSHELL_EXECUTION" in log:
            alerts.append({
                "severity": "HIGH",
                "message": f"⚡ Suspicious PowerShell Execution -> {log.strip()}"
            })

        # ---------------- XSS ----------------
        elif "XSS_ATTEMPT" in log:
            alerts.append({
                "severity": "HIGH",
                "message": f"🕷️ XSS Attack Attempt -> {log.strip()}"
            })

        # ---------------- PHISHING ----------------
        elif "PHISHING_LINK_DETECTED" in log:
            alerts.append({
                "severity": "MEDIUM",
                "message": f"🎣 Phishing Link Detected -> {log.strip()}"
            })

    return alerts