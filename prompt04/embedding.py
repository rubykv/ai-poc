from openai import OpenAI
import os
import numpy as np
from numpy.linalg import norm

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

cosine1 = np.dot(embedding1, embedding2) / (norm(embedding1) * norm(embedding2))
print(cosine1)

cosine2 = np.dot(embedding1, embedding3) / (norm(embedding1) * norm(embedding3))
print(cosine2)

