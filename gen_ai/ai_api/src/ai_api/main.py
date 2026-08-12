from dotenv import load_dotenv
from rich import print

# from .openai import openai
# from .gemini import google_genai

# from .prompts.chain_of_thought import cot
from .prompts.structure_output import generate_user

load_dotenv()


def main():

    response = generate_user()

    print(response.output_text)


if __name__ == "__main__":
    main()
