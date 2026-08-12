from dotenv import load_dotenv
from rich import print

# from .openai import openai
# from .gemini import google_genai

# from .prompts.chain_of_thought import cot
# from .prompts.structure_output import generate_user
# from .prompts.auto_cot import chat

from pydantic import BaseModel
from .prompts.ask_ai import ask_ai

load_dotenv()


class UserProfile(BaseModel):
    name: str
    age: int


class MathAnswer(BaseModel):
    formula: str
    result: float


def main():

    user = ask_ai("Create a random user", UserProfile)
    print(user.name)

    math = ask_ai("What is 100 divided by 4?", MathAnswer)
    print(math.result)


if __name__ == "__main__":
    main()
