from resume_optimizer import optimize_resume

# Test with a real resume file
result = optimize_resume(
    resume_file     = "2301641520169.pdf",
    job_description = "Python developer with FastAPI and SQL skills"
)

print("Original ATS Score :", result["original_ats_score"])
print("Optimized ATS Score:", result["optimized_ats_score"])
print("Improvement        :", result["score_improvement"])
print("Optimized Resume   :", result["optimized_resume"][:200])
print("DOCX saved at      :", result["optimized_resume_path"])
