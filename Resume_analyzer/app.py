from flask import Flask, request, render_template
import os
from resume_parser import extract_text_from_pdf
from analyzer import analyze_resume

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        file = request.files["resume"]
        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)
            text = extract_text_from_pdf(filepath)
            result = analyze_resume(text)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
