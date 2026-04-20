# brain.py
from openai import OpenAI

# Ollama runs locally on port 11434
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama" # This is a placeholder; Ollama doesn't check keys
)

def ask_ai(user_prompt):
    response = client.chat.completions.create(
        model="llama3.2",
        messages=[
            {"role": "system", "content": "You are a helpful local assistant."},
            {"role": "user", "content": user_prompt}
        ]
    )
    # This safer way works for both dictionaries and objects
    return response.choices[0].message.content
