# brain.py
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load the keys from the .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def ask_ai(user_prompt):
    """Sends the user prompt to the LLM and returns the text response."""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response.choices.message.content
