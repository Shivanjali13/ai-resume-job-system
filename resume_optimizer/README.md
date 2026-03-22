# Resume Optimizer Module-CVerify

One of the key modules of this AI powere resumeparsing and job recommendation system
Owner-Shivanjali    Role-AI/Optimizer Developer

**Overview**
The Resume Optimizer Module is the AI backbone of the project. It accepts a parsed resume and a target job description, calculates an ATS (Applicant Tracking System) compatibility score, and uses an LLM-powered agent to generate tailored improvement suggestions — helping candidates significantly boost their chances of passing automated screening systems.
This module exposes a FastAPI REST interface that integrates with the Resume Scanner, Job Recommender, and Frontend modules via a shared API contract.


**Features**
-> Resume Parsing — Extracts text from .pdf and .docx resume files
-> ATS Scoring — Computes keyword overlap, section completeness, and formatting signals against a target job description
-> LLM-Powered Optimization — Sends structured prompts to Groq (llama-3.1-8b-instant) for contextual, role-specific improvement suggestions
-> Before/After Score Comparison — Returns both the original and projected improved ATS scores
-> RESTful API — Clean FastAPI endpoints ready for frontend and cross-module consumption

**Project module struncture**

resume-optimizer/

│
├── main.py               # FastAPI app entry point
├── routes.py             # API route definitions
├── schemas.py            # Pydantic request/response models
│
├── parser.py             # PDF & DOCX text extraction (pdfplumber, python-docx)
├── ats_scorer.py         # ATS compatibility scoring logic
├── prompt_builder.py     # Constructs structured prompts for the LLM
├── optimizer.py          # Calls Groq API and returns suggestions
│
├── requirements.txt      # Python dependencies
└── README.md             

**Tech Stack**
Layer                Technology
Framework             FastAPI
Language              Python 3.10+
LLM                   APIGroq — llama-3.1-8b-instant
PDF Parsing           pdfplumber
DOCX Parsing          python-docx
Validation            Pydantic (via FastAPI)
Server                Uvicorn

**How To Run The Module?**
1. Clone the repository and switch to the module branch

    git clone https://github.com/<Shivanjali13>/<repo-name>.git
    cd <repo-name>
    git checkout <shivanjali/resume_optimizer>

2. Create and activate a virtual environment

    Windows
    python -m venv venv
    venv\Scripts\activate

3. Install dependencies

    pip install -r requirements.txt

4. Set up environment variables
Create a .env file in the module root:
    GROQ_API_KEY=your_groq_api_key_here

(🔑 Get your free API key at https://console.groq.com)

5.  Run the server

uvicorn main:app --reload --port 8000
The API will be live at: http://localhost:8000
Interactive docs: http://localhost:8000/docs


API Endpoints
POST /optimize
Upload a resume file and provide a job description. Returns the ATS score, improvement suggestions, and projected score after applying suggestions.


**Requirements**
fastapi
uvicorn
pdfplumber
python-docx
groq
python-dotenv
pydantic
python-multipart

