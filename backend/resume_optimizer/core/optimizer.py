import os
import json
from groq import Groq
from dotenv import load_dotenv
from resume_optimizer.core.prompt_builder import build_suggestion_prompt, build_optimizer_prompt 
from resume_optimizer.core.ats_scorer import calculate_ats_score

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def call_llm(prompt: str, temperature: float = 0.4) -> str:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature
    )
    return response.choices[0].message.content

def run_optimizer_agent(resume_text: str, job_description: str) -> dict:

    # Step 1: ATS pre-score
    ats_report = calculate_ats_score(resume_text, job_description)

    # Step 2: Get LLM suggestions
    suggestion_prompt = build_suggestion_prompt(
        resume_text, job_description, ats_report["missing_keywords"]
    )
    raw_suggestions = call_llm(suggestion_prompt, temperature=0.3)

    try:
        # Clean response before parsing
        cleaned = raw_suggestions.strip()
        if cleaned.startswith("```"):
            cleaned = cleaned.split("```")[1]
            if cleaned.startswith("json"):
                cleaned = cleaned[4:]
        suggestions = json.loads(cleaned.strip())
    except json.JSONDecodeError:
        suggestions = {"raw": raw_suggestions}

    # Step 3: Rewrite resume using suggestions
    optimizer_prompt = build_optimizer_prompt(resume_text, job_description, suggestions)
    optimized_resume = call_llm(optimizer_prompt, temperature=0.5)

    # Step 4: Re-score the optimized resume
    new_ats_report = calculate_ats_score(optimized_resume, job_description)

    return {
        "original_ats_score": ats_report["ats_score"],
        "optimized_ats_score": new_ats_report["ats_score"],
        "score_improvement": round(new_ats_report["ats_score"] - ats_report["ats_score"], 1),
        "matched_keywords": new_ats_report["matched_keywords"],
        "still_missing": new_ats_report["missing_keywords"],
        "suggestions": suggestions,
        "optimized_resume": optimized_resume
    }