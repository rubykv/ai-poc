from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPEN_AI_KEY"))

with client.audio.speech.with_streaming_response.create(
    model="tts-1",
    voice="alloy",
    input="Hello world! This is a streaming test.",
) as response:
    response.stream_to_file("output.mp3")