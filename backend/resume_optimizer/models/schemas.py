from pydantic import BaseModel
from typing import List, Optional

class ATSScoreDetail(BaseModel):
    ats_score: float
    matched_keywords: List[str]
    missing_keywords: List[str]
    total_jd_keywords_checked: int

class SectionSuggestions(BaseModel):
    summary: Optional[str]
    experience: Optional[str]
    skills: Optional[str]
    education: Optional[str]
    formatting: Optional[str]

class LLMSuggestions(BaseModel):
    overall_feedback: Optional[str]
    ats_improvement_tips: Optional[List[str]]
    section_suggestions: Optional[SectionSuggestions]
    keywords_to_inject: Optional[List[str]]
    missing_sections: Optional[List[str]]

class OptimizerResponse(BaseModel):
    original_ats_score: float
    optimized_ats_score: float
    score_improvement: float
    matched_keywords: List[str]
    still_missing: List[str]
    suggestions: LLMSuggestions
    optimized_resume: str