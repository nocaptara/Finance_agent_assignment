# **Multi-Agent Financial Assistant with Voice Interaction**

This project implements a multi-agent financial assistant designed to provide market insights and analysis via voice interaction. The system includes several agents for tasks such as portfolio analysis, web scraping, financial analysis, language processing, and voice recognition. The assistant uses a **Streamlit** front-end, **FastAPI** for each agent, and integrates **Whisper** for speech-to-text (STT) and **pyttsx3** for text-to-speech (TTS).

---

## 🚀 **Features**

- **Voice Input**: Allows users to ask financial questions using voice (e.g., "What's the risk exposure in Asia tech stocks today?").
- **Voice Output**: Provides market briefs and insights as spoken responses.
- **Modular Architecture**: Uses FastAPI microservices to separate concerns (API, analysis, scraping, etc.).
- **Customizable Configurations**: Uses MCP (Model-Config-Parameter) for dynamic configurations of agents and models.
- **Market Insights**: Integrates with financial data APIs like Yahoo Finance for real-time data.

---

## 🛠️ **Tech Stack**

- **Backend**: 
  - FastAPI for building microservices for each agent.
  - Uvicorn for serving FastAPI apps.
- **Frontend**: 
  - Streamlit for the web UI.
- **Voice**: 
  - Whisper for speech-to-text (STT).
  - pyttsx3 for text-to-speech (TTS).
- **Data**:
  - BeautifulSoup for web scraping.
  - Pandas and Numpy for data processing.
  - yfinance for financial data.
- **Containerization**: 
  - Docker for deployment.

---

## 📁 Project Structure

```
multi-agent-financial-assistant/
├── agents/
│   ├── voice_agent/
│   ├── orchestrator/
│   ├── analysis_agent/
│   ├── scraping_agent/
│   ├── retriever_agent/
│   └── language_agent/
├── streamlit_app/
│   ├── app.py
│   └── config.yaml
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## 🏗️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/multi-agent-financial-assistant.git
cd multi-agent-financial-assistant
```

### 2. Install Dependencies

It's recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate  # For Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not provided, install manually:

```bash
pip install fastapi uvicorn requests pandas numpy yfinance beautifulsoup4 pyttsx3 transformers sentence-transformers faiss-cpu streamlit mcp
```

---

## ⚙️ Configuration

Create a `config.yaml` file in `streamlit_app/`:

```yaml
voice_agent:
  port: 8005
  model: "base"
  tts_engine: "pyttsx3"

orchestrator:
  port: 8006
  api_endpoint: "http://localhost:8006"

analysis_agent:
  port: 8001
  model: "tech_exposure_model"

scraping_agent:
  port: 8004
  target_website: "https://example.com"

retriever_agent:
  port: 8002
  db_url: "mongodb://localhost:27017"

language_agent:
  port: 8003
  model: "sentence-transformers"
  api_key: "your-api-key"

streamlit_app:
  port: 8501
  session_timeout: 600
```

---

## 🐳 Run with Docker

### Build containers:

```bash
docker-compose build
```

### Run all services:

```bash
docker-compose up
```

This starts:

- Voice agent
- Orchestrator
- Analysis agent
- Scraping agent
- Retriever agent
- Language agent
- Streamlit frontend

---

## 🧪 Run Agents Individually (Optional)

In separate terminals:

```bash
uvicorn voice_agent:app --port 8005 --reload
uvicorn orchestrator:app --port 8006 --reload
uvicorn analysis_agent:app --port 8001 --reload
uvicorn scraping_agent:app --port 8004 --reload
uvicorn retriever_agent:app --port 8002 --reload
uvicorn language_agent:app --port 8003 --reload
streamlit run streamlit_app/app.py
```

---

## 🌐 Accessing the App

Visit [http://localhost:8501](http://localhost:8501) to use the voice assistant.

---

## 🧩 Configuration with MCP

MCP allows dynamic agent configuration via `config.yaml`.

Update parameters like this:

```yaml
language_agent:
  model: "new-model-v2"
  api_key: "your-new-api-key"
```

Then restart services to apply changes.

---

## 🧰 Troubleshooting

- **Port Conflicts**: Ensure ports are free or change them in `config.yaml`.
- **Dependencies**: Verify with `pip install -r requirements.txt`.
- **Docker**: Ensure containers are running with `docker ps`.

---

## 🚀 Deployment

To deploy:

- Use Docker in production.
- Set up Nginx or similar as a reverse proxy.
- Secure with HTTPS and proper API key management.

---

## 🤝 Contributing

Pull requests are welcome! Ideas for contribution:

- Improve voice recognition or language models.
- Add new financial data sources.
- Enhance UI and UX.
- Improve error handling/logging.

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for more.

---

## 📬 Contact

For questions or suggestions, please open an issue or contact the maintainer.




