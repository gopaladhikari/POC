from google import genai


client = genai.Client(api_key="")


response = client.responses.create(
    model="gpt-5.4", input="Write a one-sentence bedtime story about a unicorn."
)
