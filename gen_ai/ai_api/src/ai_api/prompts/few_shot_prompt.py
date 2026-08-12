from google import genai

google_client = genai.Client()


def few_shot_prompt():
    """Including a small number of examples within the prompt to demonstrate the task, helping the model learn in context before generating the desired output."""

    system_instruction = """
    You are an expert Python code reviewer.
    Review the user's code and output exactly three bullet points of feedback.
    Do not be polite; just give the technical facts.

    Examples:

    User: def add(a, b): return a + b
    Assistant: - The function `add` takes two arguments `a` and `b` and returns their sum.

    User: def subtract(a, b): return a - b
    Assistant: - The function `subtract` takes two arguments `a` and `b` and returns their difference.

    User: def multiply(a, b): return a * b
    Assistant: - The function `multiply` takes two arguments `a` and `b` and returns their product.
    """

    user_input = input("Enter your prompt: ")

    interaction = google_client.interactions.create(
        model="gemini-pro-latest",
        input=user_input,
        system_instruction=system_instruction,
    )

    return interaction
