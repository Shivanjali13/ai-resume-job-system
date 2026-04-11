from pdfminer.high_level import extract_text
import spacy
import re
import json
from pdfminer.high_level import extract_text
import os

def extract_skills_from_pdf(pdf_path):
    return extract_text(pdf_path)

sample_text = extract_skills_from_pdf("your resume")
print(sample_text)
import re
def clean_text(text):
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r' +', ' ', text)
    return text.strip()
cleaned = clean_text(sample_text)
print(cleaned)
import spacy
nlp = spacy.load("en_core_web_sm")

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

name = extract_name(cleaned)
print(name)
import json
import re

SKILLS_DB = {

    # 💻 Programming Languages
    "python": ["python", "py"],
    "java": ["java"],
    "c++": ["c++", "cpp"],
    "c": ["c language", "c"],
    "javascript": ["javascript", "js"],
    "typescript": ["typescript", "ts"],

    # 🌐 Web Development
    "html": ["html", "html5"],
    "css": ["css", "css3"],
    "react": ["react", "reactjs", "react.js"],
    "node.js": ["node", "nodejs", "node.js"],
    "express.js": ["express", "expressjs"],
    "bootstrap": ["bootstrap"],

    # 🗄️ Databases
    "mysql": ["mysql"],
    "mongodb": ["mongodb", "mongo"],
    "postgresql": ["postgresql", "postgres"],

    # 🤖 AI / ML / Data
    "machine learning": ["machine learning", "ml"],
    "deep learning": ["deep learning", "dl"],
    "natural language processing": ["nlp", "natural language processing"],
    "data analysis": ["data analysis", "data analytics"],
    "data science": ["data science"],
    "pandas": ["pandas"],
    "numpy": ["numpy"],
    "tensorflow": ["tensorflow"],
    "pytorch": ["pytorch"],

    # ⚙️ Tools & Platforms
    "git": ["git"],
    "github": ["github"],
    "docker": ["docker"],
    "kubernetes": ["kubernetes", "k8s"],
    "linux": ["linux", "unix"],
    "aws": ["aws", "amazon web services"],
    "azure": ["azure", "microsoft azure"],

    # 📊 Business / Analyst Roles
    "excel": ["excel", "ms excel"],
    "power bi": ["power bi", "powerbi"],
    "tableau": ["tableau"],
    "sql": ["sql", "structured query language"],
    "business analysis": ["business analysis", "ba"],
    "financial analysis": ["financial analysis"],

    # 📢 Marketing / Non-Tech
    "digital marketing": ["digital marketing"],
    "seo": ["seo", "search engine optimization"],
    "content writing": ["content writing", "copywriting"],
    "social media marketing": ["smm", "social media marketing"],
    "email marketing": ["email marketing"],

    # 🧑‍💼 HR / Management
    "recruitment": ["recruitment", "talent acquisition"],
    "human resource management": ["hr", "human resource management"],
    "project management": ["project management"],
    "agile": ["agile"],
    "scrum": ["scrum"],

    # 🧠 Soft Skills (IMPORTANT for ATS)
    "communication": ["communication", "communication skills"],
    "teamwork": ["teamwork", "team player"],
    "leadership": ["leadership"],
    "problem solving": ["problem solving", "analytical thinking"],
    "time management": ["time management"],
    "adaptability": ["adaptability", "flexibility"],

    # 🎨 Design
    "photoshop": ["photoshop", "adobe photoshop"],
    "figma": ["figma"],
    "ui/ux design": ["ui ux", "ui/ux", "user experience design"],

}

def extract_skills(text, skills_db=SKILLS_DB):
    text = text.lower()
    found_skills = set()   # ✅ removes duplicates automatically

    for skill, keywords in skills_db.items():
        for keyword in keywords:
            # ✅ word boundary matching (avoids false matches)
            if re.search(r'\b' + re.escape(keyword) + r'\b', text):
                found_skills.add(skill)
                break

    return list(found_skills)


# Extract skills
skills = extract_skills(cleaned)

# Create final JSON output
output = {
    "name": name,
    "skills": skills
}

# Print JSON nicely
print(json.dumps(output, indent=4))




