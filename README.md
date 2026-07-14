# 🔮 AI Powered Astrology Services

An AI-powered Astrology Services platform that transforms traditional astrology calculations into personalized, conversational experiences using **FastAPI**, **React**, **OpenAI**, **AI Agents**, and a scalable AI architecture.

The platform enhances existing astrology services by combining astrology calculations with AI-generated interpretations, allowing users to receive detailed, personalized, and human-friendly astrology reports.

---

# 🚀 Features

- AI-powered Horoscope Matching
- Personalized astrology interpretations
- Marriage Compatibility Analysis
- AI-generated relationship insights
- Horoscope Matching Report
- Kundali Matching Report
- South Indian (Tamil) Porutham Analysis
- AI-generated compatibility summaries
- PDF report generation
- Email report workflow (ready for integration)
- REST APIs using FastAPI
- Interactive React frontend
- Modular AI Agent architecture
- Production-ready backend design

---

# 🎯 Project Objective

Traditional astrology tools usually return static reports generated from predefined templates.

This project introduces an AI interpretation layer that transforms those static astrology results into personalized, conversational, and user-friendly reports while preserving the original astrology calculations.

Instead of replacing astrology logic, AI enhances the user experience by explaining the results in natural language and providing contextual recommendations.

---

# 🏗 Architecture

```text
                   +-------------------------+
                   |      React Frontend     |
                   +-----------+-------------+
                               |
                        REST API Requests
                               |
                               ▼
                  +---------------------------+
                  |      FastAPI Backend      |
                  +------------+--------------+
                               |
        +----------------------+-----------------------+
        |                      |                       |
        ▼                      ▼                       ▼
 Horoscope APIs         AI Agent Layer         Report Generator
 (Astrology Logic)      (OpenAI GPT)          (PDF / Email)
        |                      |                       |
        |                      ▼
        |            Personalized Interpretation
        |                      |
        ▼                      ▼
 Astrology Response      AI Enhanced Report
```

---

# 🤖 AI Workflow

```text
User Input
(Name, DOB, Time, Birth Place)

            │

            ▼

Astrology Calculation Engine
(Nakshatra, Rasi, Lagna,
Compatibility Score)

            │

            ▼

AI Compatibility Agent

            │

            ▼

Personalized Horoscope Report

            │

            ▼

React UI + PDF Report
```

---

# 📂 Project Structure

```text
AI_Astrology_Services/

backend/
│
├── agents/
│   ├── compatibility_agent.py
│   ├── prediction_agent.py
│   └── naming_agent.py
│
├── models/
│   └── schemas.py
│
├── prompts/
│   ├── horoscope_prompt.py
│   ├── birthstar_prompt.py
│   └── naming_prompt.py
│
├── routes/
│   ├── compatibility.py
│   ├── prediction.py
│   └── naming.py
│
├── services/
│   ├── openai_service.py
│   ├── orchestrator.py
│   └── astroved_service.py
│
├── app.py
├── config.py
├── .env
└── requirements.txt

frontend/

├── src/
│   ├── api/
│   ├── pages/
│   ├── assets/
│   ├── App.jsx
│   ├── main.jsx
│   └── index.css
│
└── package.json
```

---

# ⚙️ Tech Stack

## Frontend

- React
- HTML5
- CSS3
- JavaScript

## Backend

- Python
- FastAPI
- Pydantic
- Requests

## AI

- OpenAI GPT
- Prompt Engineering
- AI Agents
- RAG-Ready Architecture

## Report Generation

- jsPDF

## API Documentation

- Swagger UI

---

# 🧠 AI Agent Architecture

Each astrology module is designed as an independent AI agent responsible for generating contextual and personalized interpretations.

### Current Agents

- Compatibility Agent
- Prediction Agent
- Naming Agent

This modular approach allows additional astrology services to be integrated without affecting the existing system.

---

# 🔮 Astrology Modules

## Matching & Compatibility

- Horoscope Matching
- Kundali Matching
- Marriage Compatibility
- Love Calculator
- Birth Date Compatibility
- Nakshatra Porutham

---

## Personality & Prediction

- Birthstar Quiz
- Daily Horoscope
- Tarabalam

---

## Baby & Naming

- Baby Name Finder

---

# 📊 Horoscope Matching Workflow

```text
User Inputs

↓

Birth Details Validation

↓

Astrology Calculation API

↓

Compatibility Analysis

↓

AI Interpretation

↓

Horoscope Matching Report

↓

Kundali Matching Report

↓

PDF Report Generation
```

---

# ✨ AI Enhancement

Instead of returning predefined astrology descriptions, the AI generates:

- Personalized compatibility analysis
- Emotional compatibility insights
- Relationship strengths
- Communication patterns
- Long-term marriage outlook
- Practical relationship guidance
- Human-friendly explanations

Each report is generated dynamically based on the astrology calculation results.

---

# 📄 Report Features

The generated report includes:

- Horoscope Matching Report
- Kundali Matching Analysis
- South Indian Porutham Results
- Compatibility Score
- AI Personalized Summary
- Marriage Recommendation
- Downloadable PDF Report

---

# 🚀 Future Enhancements

- RAG-based Astrology Knowledge Base
- Redis Response Caching
- Multi-Agent Orchestration
- Voice-based Astrology Assistant
- AI Chat Support
- Personalized Daily Horoscope
- WhatsApp Report Delivery
- Premium Report Generation
- Multi-language Support
- Email Automation
- Analytics Dashboard

---

# 📖 API Documentation

After running the backend:

```text
http://localhost:8000/docs
```

Interactive Swagger UI is available for testing all APIs.

---

# ▶️ Running Locally

## Clone Repository

```bash
git clone https://github.com/yuzvendhrachahal-dev/AI_Astrology_Services.git

cd AI_Astrology_Services
```

---

## Backend Setup

Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Create `.env`

```env
OPENAI_API_KEY=

MODEL_NAME=gpt-4o-mini
```

Run Backend

```bash
uvicorn app:app --reload
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

---

# 📌 Current APIs

```text
POST /horoscope-match
```

Generates an AI-powered Horoscope Matching report.

Additional astrology modules will be exposed through dedicated REST APIs.

---

# 🏆 Key Concepts Demonstrated

- AI Application Development
- Agentic AI Architecture
- FastAPI Development
- React Frontend Development
- Prompt Engineering
- REST API Design
- AI-powered Report Generation
- Modular Software Architecture
- PDF Generation
- Production-ready Project Structure
- AI Systems Engineering

---

# 👨‍💻 Author

**Nivash R N**

- GitHub: https://github.com/RNNivash
- LinkedIn: https://linkedin.com/in/nivash-r-n
- Portfolio: https://rnnivash.github.io/My_Port/

---

## ⭐ Project Status

🚧 **Active Development**

This project is being developed as an enterprise AI solution to modernize traditional astrology services by integrating Large Language Models, AI agents, and intelligent report generation while maintaining compatibility with existing astrology calculation systems.
