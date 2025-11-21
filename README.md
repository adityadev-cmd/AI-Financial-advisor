# AI Financial Advisor Agent (Gemini + Google ADK)

A smart financial advisory agent built using **Google ADK**, **Gemini 3 Pro**, and real-time search tools.  
This project follows the pattern from Google’s official demo:  
https://github.com/GoogleCloudPlatform/devrel-demos/tree/main/ai-ml/agent-labs/gemini-3-pro-agent-demo

## 🚀 Features

- Financial Q&A using Gemini 3 Pro  
- Real‑time Google Search integration  
- Runs locally using `adk web`  
- Fully compatible with Google ADK agent framework  
- Ready for Cloud Run deployment  

## 📦 Project Setup

### 1. Create Python Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Application Locally
```bash
adk web --port 8080
```

Your app will be live at:
```
http://localhost:8080
```

---

## 📁 Project Structure
```
.
├── agent.py
├── requirements.txt
├── README.md
└── (other ADK agent files)
```

---

## 🧠 How It Works

The agent uses:
- **Google ADK Agent framework**
- **Gemini 3 Pro** as the model
- **Google Search tool** for fresh data
- **InMemorySessionService** to maintain chat history

A typical call:
```python
asyncio.run(call_agent("What are today's market trends?"))
```

---

## ☁️ Deploy to Cloud Run

### Grant Secret Manager Access
```bash
gcloud secrets add-iam-policy-binding gemini-api-key   --member="serviceAccount:PROJECT_NUM-compute@developer.gserviceaccount.com"   --role="roles/secretmanager.secretAccessor"
```

### Deploy Service
```bash
gcloud run deploy <SERVICE_NAME>   --region=us-central1   --source .
```

---

## 🔗 Reference

Original Google demo reference:  
https://github.com/GoogleCloudPlatform/devrel-demos/tree/main/ai-ml/agent-labs/gemini-3-pro-agent-demo

---

## 📄 License

MIT License
