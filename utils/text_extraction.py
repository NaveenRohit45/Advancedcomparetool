import fitz  # PyMuPDF
import docx

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    return "\n".join(page.get_text() for page in doc)

def extract_text_from_docx(file):
    d = docx.Document(file)
    return "\n".join(p.text for p in d.paragraphs)

def extract_metadata(file):
    # Return dummy metadata for now
    return {"Filename": file.name, "Type": file.type}

def compare_metadata(meta1, meta2):
    return {key: (meta1.get(key), meta2.get(key)) for key in set(meta1) | set(meta2)}
