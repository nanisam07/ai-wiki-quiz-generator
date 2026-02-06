import google.generativeai as genai
import os

# Configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ✅ UPDATED MODEL NAME (THIS FIXES THE ERROR)
model = genai.GenerativeModel("models/gemini-1.5-flash")

def generate_quiz(text: str):
    prompt = f"""
You are an educational quiz generator.

Based strictly on the Wikipedia content below, generate:
- 5 to 10 multiple choice questions
- Each question must have:
  - Question text
  - 4 options
  - Correct answer
  - Difficulty (easy/medium/hard)
  - Short explanation
- Also suggest 3 related Wikipedia topics.

Return the output in a clear JSON-like format.

CONTENT:
{text}
"""
    response = model.generate_content(prompt)
    return response.text
