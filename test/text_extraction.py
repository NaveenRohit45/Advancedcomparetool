# tests/test_text_extraction.py

from document_comparator.text_extraction import extract_text_from_pdf

def test_extract_text_from_pdf():
    # Simulate a PDF path (replace with an actual file or mock in real tests)
    pdf_path = "tests/sample_document.pdf"
    
    # Expected output (this should be based on a known content of your sample PDF)
    expected_text = "This is a sample document."

    extracted_text = extract_text_from_pdf(pdf_path)

    # Check if the expected text is in the extracted text
    assert expected_text in extracted_text, "Text extraction failed!"
