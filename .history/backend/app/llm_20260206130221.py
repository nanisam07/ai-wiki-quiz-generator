import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def generate_quiz(text):
    prompt = f"""
You are an educational quiz generator.

Generate a quiz strictly based on the Wikipedia content below.

Return JSON-like output containing:
- questions
- options
- correct answers
- difficulty
- explanation
- related topics

CONTENT:
{text}
"""
    response = model.generate_content(prompt)
    return response.text
