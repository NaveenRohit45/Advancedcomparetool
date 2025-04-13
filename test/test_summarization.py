# tests/test_summarization.py

from unittest.mock import patch
from document_comparator.summarization import generate_summary

def test_generate_summary_with_mock():
    text = "This is a sample document about AI."

    with patch('document_comparator.summarization.generate_summary') as mock_summary:
        mock_summary.return_value = "This is a short AI summary."

        summary = generate_summary(text)

        assert summary == "This is a short AI summary.", "Mocked summary does not match!"
