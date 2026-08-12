from dotenv import load_dotenv
from rich import print

# from .openai import openai
from .gemini import google_genai

load_dotenv()


def main():
    # response = openai()

    interaction = google_genai()

    # print(response.output_text)

    print(interaction.output_text)


if __name__ == "__main__":
    main()
