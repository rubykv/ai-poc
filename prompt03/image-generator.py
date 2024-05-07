import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPEN_AI_KEY"))

response = client.images.generate(
    model='dall-e-3',
    prompt='I NEED to test how the tool works with extremely simple prompts. DO NOT add any detail, just use it '
           'AS-IS: an image of an aeroplane hanging from a cloth hanger',
    size='1024x1024',
    quality='standard',
    n=1
)

print(response.data[0])
