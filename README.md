# AI-Powered Network Anomaly Detection Lab

This project is my take on how FAANG and Fortune 500 companies could build an AI-powered monitoring system for large-scale networks. It’s not just a lab — I designed it to look and feel like a production setup, with streaming pipelines, ML-driven detection, and live dashboards.

---

## What’s Inside

Here’s what this repo actually does:

- **Kafka + NetFlow Generator** → streams simulated network traffic in real time  
- **Spark (PySpark)** → processes logs and extracts traffic patterns  
- **ML Models (Isolation Forest, Autoencoders)** → detect anomalies like DDoS, spikes, and routing issues  
- **Prometheus + Grafana** → dashboards and alerts on anomalies  
- **Terraform (optional)** → infra provisioning for cloud deployment  
- **GitHub Actions CI/CD** → every config or model change triggers validation and test runs  

---

## Quick Start

Clone this repo and spin everything up in Docker:

```bash
git clone https://github.com/roshanreddy1108/NetSage-Anomaly-Detection.git
cd NetSage-Anomaly-Detection
docker-compose up --build
```

- Grafana → http://localhost:3000 (admin/admin)  
- Prometheus → http://localhost:9090  
- Kafka logs will stream, Spark will process them, and ML will flag anomalies.  

---

## Proof

- `terraform_apply.log` → Infra created (simulated)  
- `anomaly_output.log` → Sample anomaly detections  
- `grafana_dashboard.png` → Dashboard screenshot  

---

## Scalability

- Start: 1–2 simulated sites  
- Next: Multi-topic Kafka, Spark clusters  
- Enterprise: 50+ sites with multi-cloud ingestion and SIEM integration  

---

## What I Learned

- How to merge **network telemetry with ML pipelines**  
- How to make a **streaming ML system production-shaped**  
- How to design dashboards that translate raw logs into **actionable insights**  

---
