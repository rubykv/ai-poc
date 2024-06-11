from openai import OpenAI
import os
import numpy as np

client = OpenAI(api_key=os.environ.get("OPEN_AI_KEY"))

response1 = client.embeddings.create(
    input="cat is a pet animal",
    model="text-embedding-3-large"
)
embedding1 = response1.data[0].embedding

response2 = client.embeddings.create(
    input="cat drinks milk",
    model="text-embedding-3-large"
)
embedding2 = response2.data[0].embedding

response3 = client.embeddings.create(
    input="rose is a flower",
    model="text-embedding-3-large"
)
embedding3 = response3.data[0].embedding

print("euclidean distance between 1 and 2")
print(np.linalg.norm(np.array(embedding1) - np.array(embedding2)))
print("euclidean distance between 1 and 3")
print(np.linalg.norm(np.array(embedding1) - np.array(embedding3)))
