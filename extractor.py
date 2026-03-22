import fitz  # PyMuPDF
import spacy
import re
import json

# -----------------------------
# 0️⃣ DEBUG: Start fresh run
# -----------------------------
print("DEBUG: Starting new run of Smith Resume parser")

# -----------------------------
# 1️⃣ LOAD TRAINED SPACY MODEL
# -----------------------------
nlp = spacy.load("skill_model")  # your trained spaCy model

# -----------------------------
# 2️⃣ OPEN PDF AND EXTRACT TEXT
# -----------------------------
fname = "data/test/Resume(current).pdf"  # path to Smith resume
print(f"Processing file: {fname}")

doc_pdf = fitz.open(fname)

text = ""
for page in doc_pdf:
    text += page.get_text()

# -----------------------------
# 3️⃣ RUN SPACY MODEL
# -----------------------------
doc_spacy = nlp(text)

model_skills = []
designation = []

for ent in doc_spacy.ents:
    label = ent.label_.upper()
    if label == "SKILL":
        model_skills.append(ent.text.strip())
    elif label == "DESIGNATION":
        designation.append(ent.text.strip())

# -----------------------------
# 4️⃣ SECTION BASED EXTRACTION
# -----------------------------
lines = text.split("\n")

skill_headers = [
    "skills",
    "technical skills",
    "professional skills",
    "core competencies",
    "tech stack",
    "key skills"
]

section_skills = []
capture = False
count = 0

for line in lines:
    clean_line = line.strip().lower()

    # detect heading
    if any(header in clean_line for header in skill_headers):
        capture = True
        count = 0
        continue

    # stop if new section appears (all uppercase and short)
    if capture and line.isupper() and len(line) < 30:
        break

    # capture next few lines
    if capture:
        count += 1
        section_skills.extend(re.split(",|•|-", line))
        if count >= 5:  # read next 4-5 lines
            break

# clean extracted skills
section_skills = [skill.strip() for skill in section_skills if skill.strip() != ""]

# -----------------------------
# 5️⃣ COMBINE RESULTS
# -----------------------------
all_skills = list(set(model_skills + section_skills))
designation = list(set(designation))  # remove duplicates

# -----------------------------
# 6️⃣ PRINT RESULTS (JSON FORMAT)
# -----------------------------
result = {
    "designation": designation,
    "skills_from_model": model_skills,
    "skills_from_section": section_skills,
    "all_skills": all_skills
}

print(json.dumps(result, indent=2))