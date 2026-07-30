# 🤖 AI Agents Collection with Agno

A collection of practical AI Agents built using **Agno Framework**, **Groq LLM**, and various tools to demonstrate real-world Agentic AI concepts such as tool calling, memory, and multi-agent collaboration.

This repository is designed for developers and students who want to learn how to build intelligent AI agents using Agno.

---

## 🚀 Features

This repository contains multiple AI agents demonstrating different Agentic AI capabilities.

### 🌍 Travel Assistant Agent
An AI travel assistant capable of searching the web and answering travel-related questions.

**Features**
- 🌐 Real-time web search
- ✈️ Travel recommendations
- 🛡️ Safety information
- 📅 Current date & time awareness
- 📝 Markdown formatted responses

**Tech Used**
- Agno
- Groq (GPT-OSS-120B)
- DuckDuckGo Search Tool

---

### 📈 Investment Analyst Agent

An AI financial assistant that researches stock market information and analyst recommendations.

**Features**
- 📊 Live stock prices
- 📈 Analyst recommendations
- 💰 Company fundamentals
- 🌐 Financial news search
- 📑 Markdown tables

**Tech Used**
- Agno
- Groq
- YFinance Tool
- DuckDuckGo Tool

---

### 🧠 Memory Agent

Demonstrates how AI agents can remember users across conversations using persistent memory.

**Features**
- 💾 Long-term memory
- 🗂️ SQLite database
- 🧑 Personalized conversations
- 📚 Conversation history
- 🔄 User-specific memories

**Tech Used**
- Agno
- Groq
- SQLite Database

---

### 👥 Multi-Agent Translation Team

A team of specialized AI agents working together to answer queries in multiple languages.

**Agents Included**

- 🇺🇸 English Agent
- 🇨🇳 Chinese Agent
- 🇹🇭 Thai Agent
- 🇮🇳 Hindi Agent

**Features**

- Multi-agent collaboration
- Automatic task delegation
- Parallel responses
- Team leader orchestration
- Multi-language output

---

# 🛠️ Tech Stack

- Python
- Agno Framework
- Groq LLM
- DuckDuckGo Search Tool
- Yahoo Finance Tool
- SQLite
- python-dotenv

---

# 📂 Project Structure

```text
AI-Agents/
│
├── travel_agent.py
├── investment_agent.py
├── memory_agent.py
├── translation_team.py
├── .env
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/yourusername/AI-Agents.git
```

```bash
cd AI-Agents
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Create a .env File

```env
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
```

---

## ▶️ Run the Agents

### Travel Agent

```bash
python travel_agent.py
```

### Investment Agent

```bash
python investment_agent.py
```

### Memory Agent

```bash
python memory_agent.py
```

### Translation Team

```bash
python translation_team.py
```

---

# 📸 Sample Use Cases

### 🌍 Travel Agent

```text
Is it safe to travel to UAE today?
```

---

### 📈 Investment Agent

```text
Share the MSFT stock price and analyst recommendations.
```

---

### 🧠 Memory Agent

```text
What is the capital of Australia?

What is the best time to visit it?
```

The agent remembers previous conversations automatically.

---

### 🌐 Translation Team

```text
What is the capital of India?
```

Output

- English
- Chinese
- Thai
- Hindi

---

# 🎯 Learning Objectives

This project demonstrates:

- AI Agents
- Tool Calling
- Long-Term Memory
- Conversation History
- Multi-Agent Systems
- Team Coordination
- Web Search Integration
- Financial Data Retrieval
- Agent Orchestration
- Prompt Engineering

---

# 📚 Requirements

- Python 3.10+
- Groq API Key
- Internet Connection

---

# 🤝 Contributing

Contributions are welcome!

If you have ideas for new AI agents or improvements, feel free to fork this repository and submit a pull request.

---

# ⭐ If you found this project useful

Give this repository a ⭐ on GitHub.

It motivates me to build more AI projects and share them with the community.

---

# 👨‍💻 Author

**Prince Yadav**

B.Tech Computer Science Engineering Student

Passionate about

- AI Agents
- Agentic AI
- Generative AI
- Machine Learning
- Full Stack Development

Connect with me on LinkedIn and feel free to explore my other projects.

---

## 📄 License

This project is intended for learning and educational purposes.

Feel free to use, modify, and build upon it.
