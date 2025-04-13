import streamlit as st
from dotenv import load_dotenv
import os
from utils import (
    file_handler, text_extraction, ocr, text_comparison,
    entity_analysis, table_extraction, summarizer,
    voice_tone, exporter
)


load_dotenv()  # load environment variables from .env

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Document Comparison Tool")

# Upload Section
file1 = st.file_uploader("Upload Document 1", type=["pdf", "docx"])
file2 = st.file_uploader("Upload Document 2", type=["pdf", "docx"])

if file1 and file2:
    text1, meta1 = file_handler.process_file(file1)
    text2, meta2 = file_handler.process_file(file2)

    # Display metadata comparison
    st.subheader("Metadata Comparison")
    st.json(text_extraction.compare_metadata(meta1, meta2))

    # OCR fallback
    if not text1:
        text1 = ocr.ocr_pdf(file1)
    if not text2:
        text2 = ocr.ocr_pdf(file2)

    # Text Comparison
    st.subheader("Text Differences")
    diffs = text_comparison.get_differences(text1, text2)
    st.markdown(diffs, unsafe_allow_html=True)

    # Entity Analysis
    st.subheader("Entity Differences")
    entities = entity_analysis.compare_entities(text1, text2)
    st.json(entities)

    # Table Comparison
    st.subheader("Table Differences")
    table_diffs = table_extraction.compare_tables(file1, file2)
    st.json(table_diffs)

    # Voice Tone
    st.subheader("Voice Tone Comparison")
    tones = voice_tone.compare_tones(text1, text2)
    st.json(tones)

    # Summary
    st.subheader("AI Summary")
    summary = summarizer.generate_summary(text1, text2)
    st.write(summary)

    # Export
    if st.button("Export Results"):
        docx_file = exporter.export_to_docx(diffs, entities, table_diffs, tones, summary)
        st.download_button("Download Report", docx_file, "comparison_report.docx")
