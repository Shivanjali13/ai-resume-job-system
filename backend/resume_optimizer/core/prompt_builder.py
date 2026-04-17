def build_suggestion_prompt(resume_text:str, job_description:str, missing_keywords:list) -> str:
    return f"""
You are an expert ATS resume coach and career consultant.

A candidate has provided their resume and is applying for the following job.
Your task is to analyze the resume against the job descriptionand provide specific, actionable, section-by-setion 
improvement suggestionsto maximize the ATS score.
---
JOB DESCRIPTION:
{job_description}

---
CANDIDATE RESUME:
{resume_text}

---
MISSING KEYWORDS DETECTED:
{', '.join(missing_keywords)}

---
YOUR TASK:
Provide detailed suggestions in the following JSON format ONLY.
Do not provide any explanation outside the JSON.
    
{{
  "overall_feedback": "2-3 sentence summary of resume quality vs this job",
  "ats_improvement_tips": ["tip1", "tip2", "tip3"],
  "section_suggestions": {{
    "summary": "Rewrite suggestion for the summary/objective section",
    "experience": "Specific bullet point improvements with STAR format examples",
    "skills": "Which skills to add, reorder, or highlight",
    "education": "Any certifications or coursework to highlight",
    "formatting": "ATS formatting fixes if needed"
  }},
  "keywords_to_inject": ["keyword1", "keyword2", "keyword3"],
  "missing_sections": ["section that is absent but important for this role"]
}}
"""

def build_optimizer_prompt(resume_text: str, job_description: str, suggestions: dict) -> str:
    return f"""
You are an expert resume writer specializing in ATS optimization.

Using the original resume, the job description, and the improvement suggestions below,
rewrite the COMPLETE resume to maximize ATS score for this specific job.

Rules:
- Do NOT fabricate experience, skills, or qualifications
- Naturally inject missing keywords where they genuinely fit
- Rewrite bullet points using STAR format (Situation, Task, Action, Result)
- Add measurable metrics wherever possible (e.g., "improved performance by 30%")
- Ensure all critical job description keywords appear at least once
- Keep the resume truthful and professional

---
ORIGINAL RESUME:
{resume_text}

---
JOB DESCRIPTION:
{job_description}

---
IMPROVEMENT SUGGESTIONS:
{suggestions}

---
OUTPUT:
Return ONLY the full rewritten resume text. No explanations, no commentary.
"""