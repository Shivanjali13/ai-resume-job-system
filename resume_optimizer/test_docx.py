from resume_optimizer import optimize_resume
import os

result = optimize_resume(
    resume_file     = "trial.pdf",
    job_description = "Python developer with FastAPI and SQL skills"
)

docx_path = result["optimized_resume_path"]

# Check file exists
if os.path.exists(docx_path):
    print(f"✅ DOCX created successfully!")
    print(f"   Saved at: {docx_path}")
    print(f"   ATS Score: {result['original_ats_score']} → {result['optimized_ats_score']}")
else:
    print("❌ DOCX file was not created")