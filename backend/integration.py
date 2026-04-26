from flask import Flask,request,jsonify,send_file
from io import BytesIO
from docx import Document
from flask_cors import CORS
from extractor import extract_resume_data,extract_text
from project1 import recommend_from_skills
from resume_optimizer.core.optimizer import run_optimizer_agent
app=Flask(__name__)
CORS(app)
@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files.get("resume")

    if not file:
        return jsonify({"error": "No file uploaded"}), 400
    text=extract_text(file)
    extracted_skills=extract_resume_data(file)
    jobs_recommended=recommend_from_skills(extracted_skills)
    final_output={
        "skills":extracted_skills["skills"],
        "jobs":[]
    }

    for cur in jobs_recommended:
      cur.update(run_optimizer_agent(text,cur["description"]))
      final_output["jobs"].append(cur)
    return jsonify(final_output)
@app.route('/download', methods=["POST"])
def get_optimized_resume():
    optimized_text = request.json["text"]
    doc = Document()
    for line in optimized_text.split('\n'):
        doc.add_paragraph(line)
    target_stream = BytesIO()
    doc.save(target_stream)
    target_stream.seek(0)  
    return send_file(
        target_stream,
        as_attachment=True,
        download_name='optimized_resume.docx',
        mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )

if __name__=="__main__":
    app.run(debug=True)
