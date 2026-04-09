from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import FileResponse
from core.parser import parse_resume
from core.optimizer import run_optimizer_agent
from core.resume_builder import build_resume_docx
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

@router.post("/download-optimized-resume")
async def download_optimized_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    temp_dir  = tempfile.gettempdir()
    temp_path = os.path.join(temp_dir, resume.filename)

    with open(temp_path, "wb") as f:
        shutil.copyfileobj(resume.file, f)

    resume_text = parse_resume(temp_path)
    os.remove(temp_path)

    # Run optimizer
    result = run_optimizer_agent(resume_text, job_description)

    # Convert to .docx
    output_path = os.path.join(tempfile.gettempdir(), "optimized_resume.docx")
    build_resume_docx(result["optimized_resume"], output_path)

    # Return as downloadable file
    return FileResponse(
        path        = output_path,
        filename    = "optimized_resume.docx",
        media_type  = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )