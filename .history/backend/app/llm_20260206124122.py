import google.generativeai as genai
import json
import os

# Configure Gemini (set your API key in environment variable)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def generate_quiz(text):
    prompt = f"""
You are an educational quiz generator.

Based strictly on the Wikipedia content below, generate:
- 5 to 10 multiple choice questions
- Each question must include:
  - question
  - 4 options
  - correct answer
  - difficulty (easy/medium/hard)
  - short explanation
- Suggest 3 related Wikipedia topics

Return ONLY valid JSON.

CONTENT:
{text}
"""
    response = model.generate_content(prompt)
    return json.loads(response.text)
