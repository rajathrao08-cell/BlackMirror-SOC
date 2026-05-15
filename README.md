BlackMirror XDR

AI-Assisted Cybersecurity Monitoring & Threat Visibility Platform

Overview

BlackMirror XDR is a Python-based cybersecurity monitoring platform built to simulate how modern SOC (Security Operations Center) and XDR (Extended Detection & Response) systems work.

The project combines:

Real-time packet monitoring
Network visibility
Threat analytics
MITRE ATT&CK mapping
AI-powered incident analysis
Automated reporting

The goal of this project was to understand how detection engineering, network monitoring, and incident analysis work behind modern cybersecurity operations.

Features
Real-Time Network Traffic Monitoring

Using Scapy, the platform captures live packets and visualizes network activity in real time.

Monitors:

Source IP activity
Packet counts
Traffic spikes
Network behavior patterns
Network Asset Discovery

The platform performs local network discovery using ARP scanning.

Discovers:

Active devices
Local IP addresses
MAC addresses
AI-Assisted Threat Analysis

BlackMirror XDR integrates local AI models using Ollama.

The AI engine can generate:

Threat summaries
Possible impact analysis
MITRE ATT&CK behavior references
Recommended response actions

Runs fully locally for privacy-focused analysis.

MITRE ATT&CK Mapping

Suspicious activities are mapped to MITRE ATT&CK techniques to simulate:

Threat categorization
SOC investigation workflows
Adversary behavior analysis
Automated Incident Reporting

The system can generate PDF-based incident reports automatically.

Reports include:

Detected alerts
AI-generated analysis
MITRE mappings
Incident summaries
Tech Stack
Python
Streamlit
Scapy
Plotly
Ollama
FPDF
MITRE ATT&CK Framework
Project Structure
BlackMirror-SOC/
│
├── app/
│   ├── dashboard.py
│   ├── packet_monitor.py
│   ├── network_scanner.py
│   ├── ai_engine.py
│   ├── mitre_mapper.py
│   ├── report_generator.py
│   └── log_monitor.py
│
├── logs/
├── reports/
├── static/
├── datasets/
└── screenshots/
Installation
Clone Repository
git clone https://github.com/rajathrao08-cell/BlackMirror-SOC.git
cd BlackMirror-SOC
Create Virtual Environment
python3 -m venv venv
source venv/bin/activate
Install Dependencies
pip install streamlit scapy plotly pandas fpdf ollama streamlit-autorefresh
Run Dashboard
sudo venv/bin/python -m streamlit run app/dashboard.py

Dashboard launches at:

http://localhost:8501
AI Setup (Ollama)

Install Ollama:

brew install ollama

Pull lightweight model:

ollama pull tinyllama

Or:

ollama pull llama3

Run model:

ollama run tinyllama
Current Capabilities
Live traffic visualization
Packet inspection
AI-generated threat summaries
Network device discovery
MITRE ATT&CK mapping
PDF incident reporting
Future Improvements

Planned upgrades:

Port scanning engine
Threat severity scoring
IOC detection engine
GeoIP visualization
Endpoint telemetry
Sigma-style detection rules
Multi-endpoint monitoring
Anomaly detection
Learning Outcomes

This project helped build practical understanding of:

SOC workflows
XDR concepts
Network reconnaissance
Packet analysis
Cybersecurity automation
Threat intelligence mapping
AI integration in cybersecurity
Important Note

This project was created for:

Educational purposes
Security research
Learning cybersecurity workflows

Use only in authorized environments.

Author

Rajath Rao

Cybersecurity Enthusiast | Python Developer | SOC/XDR Learning Journey

GitHub:
BlackMirror-SOC Repository