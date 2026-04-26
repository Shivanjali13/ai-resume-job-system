# CVerify✅
An AI powered resume optimizer and job recommendation system

An intelligent system that parses resumes, scores them against job descriptions using ATS logic, suggests LLM-powered improvements, and recommends matching job listings.

This group project was built by a four-person team. It helps the users by:
-> **Parsing** their resume(PDF or DOCX)
-> **Scoring** it against a target job description(ATS Score)
-> **Suggesting improvements** using an LLM(Large Language Model)
-> **Recommending relevant jobs** based on extracted skills and experience

Each team member owns one module. All modules communicate via REST APIs and are integrated into a unified frontend.

Project structure:

CVerify/
│
├── (module_1)resume_optimizer/       # ATS scoring + LLM suggestions (Shivanjali)\
|   ├──api/\
|      ├── routes.py\
|      ├── __init__.py \
|   ├──core\
|      ├── __init__.py \
│      ├── parser.py\
│      ├── ats_scorer.py\
│      ├── prompt_builder.py\
│      ├── optimizer.py\
│   ├──models\
│      ├── schemas.py\
|   ├──.env.example\
|   ├──requirements.txt\
│   └── main.py
│\
├── module_2_resume_scanner/     # Resume parsing & extraction\
│\
├── module_3_job_recommender/    # Job matching & recommendations\
│\
├── module_4_frontend/           # React + Tailwind UI\
│\
├──.env.example\
├──.gitignore\
└── README.md\


**MODULES OVERVIEW**

      Module           |           Description                                       |    Owner
_____________________________________________________________________________________________________
1  | Resume Optimizer  | Parses resume, calculates ATS  score vs job description, uses Groq LLM to suggest improvements                                                                |  Shivanjali   |
                        
                                                
2  | Resume Scanner    | Extracts structured data from uploaded resume files        |  Srishti      |
                         

3  | Job Recommender   | Matches extracted skills to job listings                   |  Muskan       |
                         

4  | Frontend          | React based UI unifying all modules                        |   Nain        |
                         
_____________________________________________________________________________________________________
