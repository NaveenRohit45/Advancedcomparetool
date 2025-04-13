from utils.text_extraction import extract_text_from_pdf, extract_text_from_docx, extract_metadata

def process_file(file):
    if file.name.endswith(".pdf"):
        return extract_text_from_pdf(file), extract_metadata(file)
    elif file.name.endswith(".docx"):
        return extract_text_from_docx(file), extract_metadata(file)
    return "", {}
