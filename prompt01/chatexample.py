import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPEN_AI_KEY"))

response = client.chat.completions.create(
    model="gpt-4",
    messages=[

        {"role": "system", "content": "Helping user start with python"},
        {"role": "system", "content": "what does getenv do"}
    ],
    temperature=0.5,
    max_tokens=1024

)

print(response)