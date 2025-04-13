def analyze_tone(text):
    # Basic tone estimation using keyword heuristics
    if "urgent" in text.lower():
        return "Urgent"
    return "Neutral"

def compare_tones(text1, text2):
    return {
        "Doc1 Tone": analyze_tone(text1),
        "Doc2 Tone": analyze_tone(text2),
    }
