import os
import tempfile
from core.resume_builder import build_resume_docx
from core.parser import parse_resume
from core.optimizer import run_optimizer_agent
from dotenv import load_dotenv

load_dotenv()

def optimize_resume(resume_file, job_description: str) -> dict:
    """
    Main function for ATS optimizaton.
    Parameters:
    resume_file    :file-like object or file path(PDF or DOCX)
    job_description:string containing the job description
    
    Returns:
    dict with:
       - original_ats_score
       - optimized_ats_score
       - score_improvement
       - matched_keywords
       - still_missing
       - suggestions
       -optimized resume(plain text)
       - optimized resume_path (path to.docx file)
    """
    
    #File input
    temp_dir = tempfile.gettempdir()
    
    if isinstance(resume_file, str):
        file_path = resume_file
        
    else:
        filename = getattr(resume_file, 'filename', 'resume.pdf')
        file_path = os.path.join(temp_dir, filename)
        resume_file.save(file_path)
        
    resume_text = parse_resume(file_path)
    
    result = run_optimizer_agent(resume_text, job_description)
    
    output_path = os.path.join(temp_dir, "optimized_resume.docx")
    build_resume_docx(result["optimized_resume"], output_path)
    result["optimized_resume_path"] = output_path
    
    return result
       
