import streamlit as st
from utils import (
    text_extraction,
    table_comparison,
    text_comparison,
    entity_analysis,
    summarizer,
    file_exporter
)
from config import OPENAI_API_KEY

# Example usage
st.title("📝 Document Comparator")

# File uploads
old_file = st.file_uploader("Upload Old Document", type=["docx", "pdf"])
new_file = st.file_uploader("Upload New Document", type=["docx", "pdf"])

if old_file and new_file:
    # Extract text
    old_text = text_extraction.extract_text(old_file)
    new_text = text_extraction.extract_text(new_file)

    # Show diff
    text_comparison.compare_side_by_side(old_text, new_text)

    # Table comparisons, summaries, etc.
