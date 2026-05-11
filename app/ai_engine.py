def generate_ai_analysis(alert):

    message = alert["message"]

    # ---------------- SQL INJECTION ----------------
    if "SQL Injection" in message:

        return """
        Possible SQL Injection attack detected.

        Impact:
        Attackers may attempt to access or manipulate database records.

        Recommended Actions:
        - Use parameterized SQL queries
        - Enable WAF protection
        - Block suspicious IP addresses
        """

    # ---------------- BRUTE FORCE ----------------
    elif "Brute Force" in message:

        return """
        Possible brute-force login attack identified.

        Impact:
        Repeated login attempts may compromise user accounts.

        Recommended Actions:
        - Enable multi-factor authentication
        - Apply account lockout policies
        - Monitor attacker IP activity
        """

    # ---------------- MALWARE ----------------
    elif "Malware" in message:

        return """
        Malware-related activity detected.

        Impact:
        Malicious software may compromise system integrity.

        Recommended Actions:
        - Isolate affected endpoint
        - Run antivirus and EDR scans
        - Investigate persistence mechanisms
        """

    # ---------------- XSS ----------------
    elif "XSS" in message:

        return """
        Cross-site scripting attack attempt identified.

        Impact:
        Attackers may inject malicious scripts into webpages.

        Recommended Actions:
        - Sanitize user input
        - Implement Content Security Policy (CSP)
        - Validate frontend forms
        """

    # ---------------- PHISHING ----------------
    elif "Phishing" in message:

        return """
        Potential phishing activity detected.

        Impact:
        Users may be redirected to malicious credential harvesting pages.

        Recommended Actions:
        - Block malicious domains
        - Educate users on phishing risks
        - Enable email filtering
        """

    # ---------------- POWERSHELL ----------------
    elif "PowerShell" in message:

        return """
        Suspicious PowerShell execution detected.

        Impact:
        Attackers may attempt lateral movement or remote execution.

        Recommended Actions:
        - Restrict PowerShell execution policies
        - Monitor encoded commands
        - Investigate parent processes
        """

    # ---------------- DEFAULT ----------------
    else:

        return """
        Suspicious activity detected.

        Recommended Actions:
        - Investigate logs
        - Monitor affected systems
        - Apply security controls
        """