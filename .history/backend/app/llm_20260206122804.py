from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    temperature=0.3
)

prompt = PromptTemplate(
    input_variables=["content"],
    template="""
Generate a quiz strictly based on the content below.

Requirements:
- 5 to 10 MCQs
- 4 options each
- correct answer
- difficulty (easy/medium/hard)
- short explanation
- suggest 3 related wikipedia topics

Return valid JSON only.

CONTENT:
{content}
"""
)

def generate_quiz(text):
    response = llm.invoke(prompt.format(content=text))
    return response.content
