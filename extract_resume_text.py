from pdfminer.high_level import extract_text

def extract_resume_text(pdf_path):
    try:
        text = extract_text(pdf_path)
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""
        
# Example usage:
if __name__ == "__main__":
    pdf_file = "sample_resume.pdf"  # Replace with your file name
    resume_text = extract_resume_text(pdf_file)
    print(resume_text[:1000])  # Print first 1000 characters
