# tests/test_entity_analysis.py

import spacy
from document_comparator.entity_analysis import analyze_entities

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def test_analyze_entities():
    text = "Alice, an engineer, lives in New York."

    # Process text using spaCy
    doc = nlp(text)

    # Expected entities
    expected_entities = {"Alice": "PERSON", "New York": "GPE"}

    entities = analyze_entities(doc)  # Assuming analyze_entities returns a dict

    # Check if the extracted entities match expected
    for entity, label in expected_entities.items():
        assert entity in entities, f"Entity '{entity}' not found!"
        assert entities[entity] == label, f"Entity '{entity}' has wrong label!"
