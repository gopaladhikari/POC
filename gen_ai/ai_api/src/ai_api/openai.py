from openai import OpenAI

openai_client = OpenAI()


def openai():
    response = openai_client.responses.create(
        model="gpt-4o-mini",
        input="Write a one-sentence bedtime story about a unicorn",
    )

    return response
