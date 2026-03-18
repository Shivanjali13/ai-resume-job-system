from fastapi import APIRouter, UploadFile, File, Form
from core.parser import parse_resume
from core.optimizer import run_optimizer_agent
import shutil, os, tempfile

router = APIRouter()

@router.post("/optimize-resume")
async def optimize_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    
    temp_dir = tempfile.gettempdir()
    temp_path = os.path.join(temp_dir, resume.filename)

    with open(temp_path, "wb") as f:
        shutil.copyfileobj(resume.file, f)

    
    resume_text = parse_resume(temp_path)
    os.remove(temp_path)

    
    result = run_optimizer_agent(resume_text, job_description)
    return result