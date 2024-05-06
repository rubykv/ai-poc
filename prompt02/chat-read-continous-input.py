import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPEN_AI_KEY"))

messages = [
    {"role": "system", "content": "You are a helpful assistant and also a star wars fan"},
]

user_input = input('How can I help you today?')

while user_input.lower() != 'bye':
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0.5,
        max_tokens=100
    )
    print(f'\n Jedi: {response.choices[0].message.content}\n')
    messages.append({"role": "assistant", "content": response.choices[0].message.content})
    user_input = input('User: ')

print('Bye until next time')
