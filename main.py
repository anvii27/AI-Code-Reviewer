import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="AI Code Reviewer Sentinel")
client = genai.Client(api_key="AIzaSyB9O_nogGiL3N65xydhIC2K7HFAekc6YR0")

class CodeSnippet(BaseModel):
    code: str
    language: str = "python"

SYSTEM_PROMPT = """
You are a Senior Lead Developer. Review this code for:
1. Logic Bugs 2. Security Risks 3. Efficiency 4. Clean Code.
Format: Markdown.
"""

@app.post("/review")
async def review_code(snippet: CodeSnippet):
    try:
        # The new simple way to talk to Gemini
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"{SYSTEM_PROMPT}\n\nCode:\n{snippet.code}"
        )
        return {"review": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def home():
    return {"message": "AI Code Reviewer is Live! Go to /docs to test it."}