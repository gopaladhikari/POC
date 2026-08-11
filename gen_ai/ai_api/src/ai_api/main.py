from openai import OpenAI
from google import genai
from dotenv import load_dotenv

load_dotenv()

openai_client = OpenAI()

google_client = genai.Client()


print("Hello from python main file")


def main():
    response = openai_client.responses.create(
        model="gpt-4o-mini",
        input="Write a one-sentence bedtime story about a unicorn.",
    )

    interaction = google_client.interactions.create(
        model="gemini-3.6-flash", input="Explain how AI works in a few words"
    )

    print(response.output_text)

    print(interaction.output_text)


if __name__ == "__main__":
    main()
