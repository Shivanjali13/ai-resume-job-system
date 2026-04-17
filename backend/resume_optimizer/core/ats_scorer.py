import re
from collections import Counter

def extract_keywords(text: str) -> list:
    words = re.findall(r'\b[a-zA-Z][a-zA-Z+#.]{2,}\b',text.lower())
    stopwords= {"and","the","for","with","are","has","was","that","this","have","from"}
    return [w for w in words if w not in stopwords]

def calculate_ats_score(resume_text:str, job_description:str) ->dict:
    resume_keywords =set(extract_keywords(resume_text))
    jd_keywords = extract_keywords(job_description)
    jd_freq = Counter(jd_keywords)
    
    top_jd_keywords = [kw for kw, _ in jd_freq.most_common(30)]
    
    matched = [kw for kw in top_jd_keywords if kw in resume_keywords]
    missing = [kw for kw in top_jd_keywords if kw not in resume_keywords]
    
    score= round((len(matched)/len(top_jd_keywords))*100,1)
    
    return {
        "ats_score": score,
        "matched_keywords":matched,
        "missing_keywords":missing,
        "total_jd_keywords_checked":len(top_jd_keywords)
    }