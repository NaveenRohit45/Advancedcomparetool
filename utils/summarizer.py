import openai

def generate_summary(text1, text2):
    prompt = f"Compare these documents:\n\nDoc 1:\n{text1}\n\nDoc 2:\n{text2}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content.strip()
