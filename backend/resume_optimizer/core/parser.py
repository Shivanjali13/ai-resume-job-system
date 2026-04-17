import pdfplumber
from docx import Document

def extract_text_from_pdf(file_path: str)->str:
    with pdfplumber.open(file_path) as pdf:
        return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    
def extract_text_from_docx(file_path: str)->str:
    doc = Document(file_path)
    return "\n".join(para.text for para in doc.paragraphs if para.text.strip())

def parse_resume(file_path:str) ->str:
    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file format. Use PDF or DOCX.")
        