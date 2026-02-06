import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

def generate_quiz(text):
    prompt = f"""
You are an educational quiz generator.

Generate a quiz STRICTLY based on the Wikipedia content below.

Return ONLY valid JSON with:
- quiz: list of questions
- related_topics: list of strings

CONTENT:
{text}
"""
    response = model.generate_content(prompt)

    # IMPORTANT: return raw text to avoid JSON parsing errors
    return response.text
