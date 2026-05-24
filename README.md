# 🎯 AI Scenario Writer

An AI-powered tool that generates **realistic workplace scenarios** to help you practice any professional skill. Built with React and FastAPI.

## 📸 Project Demo

| Backend Running | Frontend Running |
|----------------|------------------|
| `http://127.0.0.1:8000` | `http://localhost:3000` |
| API server ready | UI ready to use |

## 🌐 Local Host URLs

After starting the application, access these URLs:

| Service | URL | Description |
|---------|-----|-------------|
| **Frontend** | http://localhost:3000 | Main user interface |
| **Backend API** | http://127.0.0.1:8000 | API server |
| **API Documentation** | http://127.0.0.1:8000/docs | Auto-generated API docs |
| **Health Check** | http://127.0.0.1:8000/health | Server status |

## ✨ Features

- ✅ Works for **ANY** skill you want to practice
- ✅ **Two user types**: High Wage (Tech) & Low Wage (Service)
- ✅ **7 difficulty levels**: M01 (Beginner) to M07 (Expert)
- ✅ **Dual language**: English & Hindi
- ✅ **Realistic scenarios** with specific locations, characters, and tension
- ✅ **Actionable strategies** with explanations

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | React 18 |
| Backend | FastAPI (Python) |
| AI | Groq (Llama 3.3 70B) |
| Styling | CSS3 |

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Node.js 14 or higher
- Groq API Key (free)

### 1. Clone the Repository

```bash
git clone https://github.com/ParidhiGoel26/scenario-writer-ai.git
cd scenario-writer-ai
```

### 2. Install Backend Dependencies
```bash
pip install groq python-dotenv fastapi uvicorn
```
### 3. Install Frontend Dependencies
```bash
cd frontend
npm install
cd ..
```

### 4. Set Up API Key
Create a .env file in the root folder:
env
GROQ_API_KEY=your_groq_api_key_here

Get your free API key: 
```bash
https://console.groq.com/keys
```

### 5. Run the Application
Terminal 1 - Start Backend
```bash
python api.py
```

Terminal 2 - Start Frontend
```bash
cd frontend
npm start
```


