import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPEN_AI_KEY"))

user_input = input('How can I help you today?')

response = client.chat.completions.create(
    model="gpt-4",
    messages=[

        {"role": "system", "content": "You are a helpful assistant and also a star wars fan"},
        {"role": "user", "content": user_input}
    ],
    temperature=0.5,
    max_tokens=100

)
print(response)