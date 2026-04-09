import fitz  # PyMuPDF
import spacy
import re
import os

# 1. LOAD THE MODEL
# We load it outside the function so it stays in memory and runs fast
try:
    nlp = spacy.load("skill_model")
except:
    # Fallback in case the custom model folder is missing
    print("Warning: skill_model folder not found. Using base model.")
    nlp = spacy.load("en_core_web_sm")

def extract_resume_data(pdf_path):
    """
    This function is the bridge to the Flask app.
    It takes the path of the uploaded PDF and returns 
    a single string of all identified skills.
    """
    if not os.path.exists(pdf_path):
        return "Error: File path does not exist."

    # 2. OPEN PDF AND EXTRACT TEXT
    doc_pdf = fitz.open(pdf_path)
    text = ""
    for page in doc_pdf:
        text += page.get_text()
    doc_pdf.close()

    # 3. RUN SPACY MODEL
    doc_spacy = nlp(text)
    model_skills = []
    for ent in doc_spacy.ents:
        label = ent.label_.upper()
        if label == "SKILL":
            model_skills.append(ent.text.strip())

    # 4. SECTION BASED EXTRACTION (Your logic)
    lines = text.split("\n")
    skill_headers = [
        "skills", "technical skills", "professional skills", 
        "core competencies", "tech stack", "key skills"
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

        # stop if new section appears
        if capture and line.isupper() and len(line) < 30:
            break

        # capture next lines
        if capture:
            count += 1
            section_skills.extend(re.split(",|•|-", line))
            if count >= 5:
                break

    # Clean extracted skills
    section_skills = [skill.strip() for skill in section_skills if skill.strip() != ""]

    # 5. COMBINE RESULTS & CONVERT TO STRING
    # Using 'set' removes any duplicates between model and section
    all_skills_list = list(set(model_skills + section_skills))
    
    # This is the 'Handshake': Converting the list to a single string for her model
    final_skills_string = ", ".join(all_skills_list)
    
    return final_skills_string