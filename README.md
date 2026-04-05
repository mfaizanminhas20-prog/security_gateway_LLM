# Secure LLM Gateway - Lab Mid Project

## 🛡️ Project Overview
This project is a **Modular Security Gateway** designed to protect Large Language Models (LLMs) from common vulnerabilities. It acts as a middleware that filters user inputs before they reach the LLM.

### Key Features:
* **Prompt Injection Detection:** Uses a keyword-based scoring mechanism to block malicious instructions (e.g., jailbreaks).
* **PII Masking:** Integrated with **Microsoft Presidio** to detect and mask sensitive information like Student IDs, Phone Numbers, and API Keys.
* **Policy-Based Security:** Supports three modes: `Lenient`, `Balanced`, and `Strict`.
* **Quantitative Metrics:** Tracks `risk_score`, `pii_found`, and `latency_ms` for every request.

---

## 🏗️ System Architecture
The gateway follows a modular pipeline:
1.  **Input Reception:** Receives JSON payload via FastAPI.
2.  **Security Scan:** Checks for injection keywords and calculates a risk score.
3.  **PII Analysis:** Uses Presidio with custom recognizers for Pakistani phone numbers and University IDs.
4.  **Policy Decision:** Applies logic based on the configured security mode.
5.  **Output Generation:** Returns either the original text, masked text, or a "Blocked" message.

---

## 🚀 Getting Started

### Prerequisites:
* Python 3.8+
* Spacy NLP Model: `en_core_web_lg`

### Installation:
1. Clone the repository:
   ```bash
   git clone [https://github.com/mfaizanminhas20-prog/security_gateway_LLM.git](https://github.com/mfaizanminhas20-prog/security_gateway_LLM.git)
   cd security_gateway_LLM
