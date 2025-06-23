import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from pdfminer.high_level import extract_text
from score_resume import score_resume  # your custom function

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        role = request.form.get('role')
        file = request.files.get('resume')

        if not role or not file or not allowed_file(file.filename):
            return render_template("index.html", error="Please select a valid PDF resume and role.")

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Extract text and score resume
        resume_text = extract_text(filepath)
        score, matched, missing = score_resume(resume_text, role)

        return render_template(
            "result.html",
            score=score,
            matched_keywords=matched,
            missing_keywords=missing,
            role=role
        )

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
