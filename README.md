# **Multi-Agent Financial Assistant with Voice Interaction**

This project implements a multi-agent financial assistant designed to provide market insights and analysis via voice interaction. The system includes several agents for tasks such as portfolio analysis, web scraping, financial analysis, language processing, and voice recognition. The assistant uses a **Streamlit** front-end, **FastAPI** for each agent, and integrates **Whisper** for speech-to-text (STT) and **pyttsx3** for text-to-speech (TTS).

---

## 🚀 **Features**

- **Voice Input**: Allows users to ask financial questions using voice (e.g., "What's the risk exposure in Asia tech stocks today?").
  

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







## 🧪 Run Agents Individually 

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




## 📄 License

MIT License. See [LICENSE](LICENSE) for more.

---

## 📬 Contact

For questions or suggestions, please open an issue or contact the maintainer.




