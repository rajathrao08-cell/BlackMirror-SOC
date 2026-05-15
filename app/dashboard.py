import streamlit as st
import pandas as pd
import plotly.express as px

from log_monitor import analyze_logs
from ai_engine import generate_ai_analysis
from mitre_mapper import map_to_mitre
from report_generator import generate_pdf_report

from packet_monitor import (
    traffic_stats,
    run_packet_monitor
)

from network_scanner import scan_network

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="BlackMirror-XDR",
    page_icon="🛡️",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

body {
    background-color: #0d1117;
    color: white;
}

.metric-card {
    background-color: #161b22;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #30363d;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# START PACKET MONITOR
# ---------------------------------------------------

if "monitor_started" not in st.session_state:
    run_packet_monitor()
    st.session_state.monitor_started = True

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.title("🛡️ BlackMirror-XDR")
st.subheader("AI-Powered SOC & Network Monitoring Platform")

st.markdown("---")

# ---------------------------------------------------
# LOAD ALERTS
# ---------------------------------------------------

alerts = analyze_logs("logs/security_logs.txt")

# ---------------------------------------------------
# METRICS
# ---------------------------------------------------

total_threats = len(alerts)

critical_alerts = len([
    alert for alert in alerts
    if alert["severity"] == "CRITICAL"
])

high_alerts = len([
    alert for alert in alerts
    if alert["severity"] == "HIGH"
])

system_health = max(100 - (total_threats * 2), 65)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Threats Detected", total_threats)

with col2:
    st.metric("Critical Alerts", critical_alerts)

with col3:
    st.metric("High Severity", high_alerts)

with col4:
    st.metric("System Health", f"{system_health}%")

st.markdown("---")

# ---------------------------------------------------
# LIVE THREAT FEED
# ---------------------------------------------------

st.header("🚨 Live Threat Feed")

for index, alert in enumerate(alerts):

    severity = alert["severity"]
    message = alert["message"]

    mitre_data = map_to_mitre(alert)

    if severity == "CRITICAL":
        color = "#ff0000"

    elif severity == "HIGH":
        color = "#ff4d4d"

    elif severity == "MEDIUM":
        color = "#ff9900"

    else:
        color = "#00cc66"

    with st.expander(f"[{severity}] {message}"):

        st.markdown(
            f"""
            <div style="
                background-color:#161b22;
                padding:15px;
                border-radius:10px;
                border-left:8px solid {color};
                color:white;
            ">
                <b>Threat Alert</b><br><br>
                {message}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("### MITRE ATT&CK Mapping")

        st.write(f"**Tactic:** {mitre_data['tactic']}")
        st.write(f"**Technique:** {mitre_data['technique']}")

        if st.button(
            f"Analyze with AI - {message[:20]}",
            key=f"ai_button_{index}"
        ):

            with st.spinner("Generating AI analysis..."):

                ai_analysis = generate_ai_analysis(alert)

                st.markdown("### 🤖 AI Threat Analysis")

                st.write(ai_analysis)

st.markdown("---")

# ---------------------------------------------------
# THREAT ANALYTICS
# ---------------------------------------------------

st.header("📊 Threat Analytics")

data = pd.DataFrame({
    "Attack Type": [
        "Brute Force",
        "SQL Injection",
        "XSS",
        "Malware",
        "Phishing"
    ],
    "Count": [15, 8, 5, 10, 6]
})

fig = px.bar(
    data,
    x="Attack Type",
    y="Count",
    title="Detected Threats"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------
# ATTACK TIMELINE
# ---------------------------------------------------

st.markdown("---")

st.header("📈 Attack Timeline")

timeline_data = pd.DataFrame({
    "Time": [
        "10:15",
        "10:16",
        "10:20",
        "10:22",
        "10:25",
        "10:30",
        "10:31",
        "10:35"
    ],
    "Threat Count": [3, 5, 2, 4, 6, 3, 5, 2]
})

timeline_fig = px.line(
    timeline_data,
    x="Time",
    y="Threat Count",
    markers=True,
    title="Threat Activity Timeline"
)

st.plotly_chart(timeline_fig, use_container_width=True)

# ---------------------------------------------------
# LIVE NETWORK TRAFFIC
# ---------------------------------------------------

st.markdown("---")

st.header("📡 Real-Time Network Traffic")

if traffic_stats:

    packet_df = pd.DataFrame({
        "Source IP": list(traffic_stats.keys()),
        "Packet Count": list(traffic_stats.values())
    })

    st.dataframe(packet_df)

    packet_fig = px.bar(
        packet_df,
        x="Source IP",
        y="Packet Count",
        title="Real-Time Network Activity"
    )

    st.plotly_chart(packet_fig, use_container_width=True)

else:

    st.info("Waiting for network traffic...")

# ---------------------------------------------------
# NETWORK ASSET DISCOVERY
# ---------------------------------------------------

st.markdown("---")

st.header("🖥️ Network Asset Discovery")

if st.button("Scan Local Network"):

    with st.spinner("Scanning local devices..."):

        try:

            devices = scan_network()

            if devices:

                st.success(f"Found {len(devices)} devices")

                device_df = pd.DataFrame(devices)

                st.dataframe(device_df, use_container_width=True)

            else:

                st.warning("No devices found.")

        except Exception as e:

            st.error(f"Network scan failed: {e}")

# ---------------------------------------------------
# INCIDENT REPORT GENERATION
# ---------------------------------------------------

st.markdown("---")

st.header("📄 Incident Report Generation")

if st.button("Generate Incident Report"):

    report_path = generate_pdf_report(alerts)

    st.success("Incident report generated successfully!")

    with open(report_path, "rb") as pdf_file:

        st.download_button(
            label="⬇️ Download Incident Report",
            data=pdf_file,
            file_name="BlackMirror_XDR_Report.pdf",
            mime="application/pdf"
        )

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("---")

st.caption(
    "BlackMirror-XDR | Python • Streamlit • Scapy • AI Security Analytics"
)