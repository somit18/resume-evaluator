import streamlit as st
import nltk
from pdfminer.high_level import extract_text
from score_resume import score_resume

# Ensure NLTK models download on cloud
nltk.download('punkt')
nltk.download('stopwords')

st.set_page_config(page_title="Resume Evaluator", layout="centered")


st.title("📄 AI-Powered Resume Evaluator")
st.markdown("Upload your resume (PDF) and get a tailored score based on the selected job role.")

role = st.selectbox("🔍 Select Job Role", ["Data Analyst", "Web Developer", "Machine Learning Engineer"])
uploaded_file = st.file_uploader("📤 Upload Resume (PDF)", type="pdf")

if uploaded_file is not None:
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    resume_text = extract_text("temp_resume.pdf")

    with st.expander("📄 View Extracted Resume Text"):
        st.write(resume_text)

    score, matched, missing = score_resume(resume_text, role)

    st.markdown(f"### ✅ Resume Score for **{role}**: **{score}/100**")

    st.markdown("#### ✅ Matched Keywords:")
    st.markdown(", ".join(matched) if matched else "_None found_")

    st.markdown("#### ❌ Missing Keywords:")
    st.markdown(", ".join(missing) if missing else "_None missing_")

    # Prepare report content
    report = f"""Resume Evaluation Report
---------------------------
Role: {role}
Score: {score}/100

Matched Keywords:
{", ".join(matched)}

Missing Keywords:
{", ".join(missing)}

Tips:
- Add relevant skills from the missing list.
- Keep the formatting clean.
"""

    st.download_button(
        label="📥 Download Report",
        data=report,
        file_name="resume_report.txt",
        mime="text/plain"
    )
