import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    return [(ent.text, ent.label_) for ent in nlp(text).ents]

def compare_entities(text1, text2):
    ents1 = set(extract_entities(text1))
    ents2 = set(extract_entities(text2))
    return {
        "Only in Doc 1": list(ents1 - ents2),
        "Only in Doc 2": list(ents2 - ents1),
    }
