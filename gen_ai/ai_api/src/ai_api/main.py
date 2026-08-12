from dotenv import load_dotenv
from rich import print

# from .openai import openai
# from .gemini import google_genai

# from .prompts.chain_of_thought import cot
# from .prompts.structure_output import generate_user
# from .prompts.auto_cot import chat
# from .prompts.ask_ai import ask_ai
# from .prompts.persona_prompting import persona_prompting


# from pydantic import BaseModel

from .prompts.gkp_prompting import generated_knowledge

load_dotenv()


def main():

    topic = input("Enter a topic: ")

    user_question = input("Enter a question: ")

    response = generated_knowledge(user_question, topic)

    print(response.output_text)


if __name__ == "__main__":
    main()
