📊 Trade Opportunities API – FastAPI + Local AI

This project analyzes Indian market sectors and returns AI-generated trade opportunity reports in Markdown format.

It uses:

FastAPI
JWT Authentication
Rate Limiting
Google News RSS for real-time data
Local AI via Ollama (Mistral model)
🛠️ System Requirements
| Tool | Version | | ------ | --------------------- | | Python | 3.10+ | | Git | Latest | | Ollama | Latest | | OS | Windows / Linux / Mac |

📥 Step 1 — Clone Repository
git clone https://github.com/<your-username>/trade-opportunities-api.git
cd trade-opportunities-api
🧪 Step 2 — Create Virtual Environment
python -m venv env
env\Scripts\activate      # Windows
source env/bin/activate   # Mac/Linux
📦 Step 3 — Install Dependencies

pip install -r requirements.txt
pip install feedparser python-dotenv httpx
🤖 Step 4 — Install Ollama (Local AI Engine)

Download and install from:

👉 https://ollama.com/download

After installation, open terminal and run:

ollama pull mistral
ollama serve
Leave this terminal running.

🔐 Step 5 — Configure Environment
Create .env file in root folder:

SECRET_KEY=a3be3b1beb3fbeef73652bf564190d30
🔑 Step 6 — Generate JWT Token
Run:

python app/create_token.py
It prints a token like:

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Copy this token.

▶ Step 7 — Start FastAPI Server
Open new terminal:

uvicorn app.main:app --reload
🌐 Step 8 — Open API Docs
Open browser:

http://127.0.0.1:8000/docs
Click Authorize 🔐 and paste your JWT token (without Bearer).

📈 Step 9 — Call API
Use endpoint:

GET /analyze/{sector}
Example:

/analyze/pharmaceuticals
/analyze/agriculture
/analyze/technology
🟢 Sample Output
# 📊 Trade Opportunity Report – Pharmaceuticals

## Market Overview
Indian pharmaceutical exports are growing...

## Key Opportunities
- API manufacturing
- Global supply contracts

## Risks
- Price regulation
- Compliance burden
🚦 Rate Limiting
Maximum:

5 requests per minute per user
🔐 Security
JWT based authentication
Rate-limiting via SlowAPI
In-memory session tracking
🏁 Done

Your AI Trade Opportunity API is now running locally.
