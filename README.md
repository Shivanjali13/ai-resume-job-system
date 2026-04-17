🚀 AI Resume Analyzer & Job Recommender

An intelligent full-stack application that analyzes resumes, extracts skills, recommends relevant jobs, and optimizes resumes using AI to improve ATS (Applicant Tracking System) scores.

✨ Features
📄 Upload resume (PDF/DOCX)
🧠 Extract skills using NLP
💼 Get job recommendations based on skills
🤖 AI-powered resume optimization
📊 ATS score improvement analysis
⬇️ Download optimized resume in Word format
⚡ Fast and interactive UI
🏗️ Tech Stack
Frontend
React.js
Tailwind CSS
Backend
Flask
Python
AI / ML
SpaCy (NLP for skill extraction)
LLM via Groq (LLaMA 3.1)
Custom ATS scoring system
📁 Project Structure
ai-resume-job-system/
│
├── backend/
│   ├── integration.py
│   ├── extractor.py
│   ├── project1.py
│   └── resume_optimizer/
│
├── frontend/
│   └── React App
│
├── data/
├── skill_model/
└── README.md
⚙️ Setup Instructions
🔹 1. Clone the Repository
git clone https://github.com/your-username/ai-resume-job-system.git
cd ai-resume-job-system
🔹 2. Backend Setup
cd backend
python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt
🔹 3. Environment Variables

Create a .env file inside backend/:

GROQ_API_KEY=your_api_key_here
🔹 4. Run Backend
python integration.py

Server runs on:

http://127.0.0.1:5000
🧠 How It Works
1. Upload Resume
2. Extract Skills (NLP)
3. Recommend Jobs
4. Optimize Resume using AI
5. Improve ATS Score
6. Download Optimized Resum
🔐 Security Note
API keys are stored in .env and not pushed to GitHub
Sensitive data is protected using environment variables
🚧 Future Improvements
🔍 Better job matching using embeddings
📊 Advanced ATS scoring model
🧾 Speed and Scalability
☁️ Deployment (AWS / Vercel)
