from fpdf import FPDF
from datetime import datetime


def generate_pdf_report(alerts):

    pdf = FPDF()

    pdf.add_page()

    # ---------------- TITLE ----------------
    pdf.set_font("Arial", "B", 20)
    pdf.cell(200, 10, "BlackMirror SOC Incident Report", ln=True, align="C")

    pdf.ln(10)

    # ---------------- TIMESTAMP ----------------
    pdf.set_font("Arial", "", 12)

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    pdf.cell(200, 10, f"Generated: {current_time}", ln=True)

    pdf.ln(10)

    # ---------------- SUMMARY ----------------
    total_alerts = len(alerts)

    critical_alerts = len([
        alert for alert in alerts
        if alert["severity"] == "CRITICAL"
    ])

    high_alerts = len([
        alert for alert in alerts
        if alert["severity"] == "HIGH"
    ])

    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, "Incident Summary", ln=True)

    pdf.set_font("Arial", "", 12)

    pdf.cell(200, 10, f"Total Threats Detected: {total_alerts}", ln=True)
    pdf.cell(200, 10, f"Critical Alerts: {critical_alerts}", ln=True)
    pdf.cell(200, 10, f"High Severity Alerts: {high_alerts}", ln=True)

    pdf.ln(10)

    # ---------------- ALERT DETAILS ----------------
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, "Threat Details", ln=True)

    pdf.set_font("Arial", "", 11)

    for alert in alerts:

        clean_message = (
            alert["message"]
            .replace("🚨", "")
            .replace("💉", "")
            .replace("🦠", "")
            .replace("⚡", "")
            .replace("🕷️", "")
            .replace("🎣", "")
        )

        pdf.multi_cell(
            0,
            10,
            f"[{alert['severity']}] {clean_message}"
        )

        pdf.ln(2)

    # ---------------- SAVE REPORT ----------------
    report_path = "reports/incident_report.pdf"

    pdf.output(report_path)

    return report_path