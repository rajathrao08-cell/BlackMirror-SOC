def map_to_mitre(alert):

    message = alert["message"]

    # ---------------- SQL INJECTION ----------------
    if "SQL Injection" in message:
        return {
            "tactic": "Initial Access",
            "technique": "Exploit Public-Facing Application"
        }

    # ---------------- BRUTE FORCE ----------------
    elif "Brute Force" in message:
        return {
            "tactic": "Credential Access",
            "technique": "Brute Force"
        }

    # ---------------- MALWARE ----------------
    elif "Malware" in message:
        return {
            "tactic": "Persistence",
            "technique": "Malware Installation"
        }

    # ---------------- POWERSHELL ----------------
    elif "PowerShell" in message:
        return {
            "tactic": "Execution",
            "technique": "PowerShell"
        }

    # ---------------- XSS ----------------
    elif "XSS" in message:
        return {
            "tactic": "Initial Access",
            "technique": "Cross Site Scripting"
        }

    # ---------------- PHISHING ----------------
    elif "Phishing" in message:
        return {
            "tactic": "Credential Access",
            "technique": "Phishing"
        }

    # ---------------- DEFAULT ----------------
    else:
        return {
            "tactic": "Unknown",
            "technique": "Unknown"
        }