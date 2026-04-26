from fastapi import FastAPI
from api.routes import router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Resume ATS Optimizer",
    description="AI agent that transforms resumes to maximize ATS score",
    version="1.0.0"
)

app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"status": "Resume Optimizer Agent is running"}