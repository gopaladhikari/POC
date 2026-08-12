from google import genai

google_client = genai.Client()


def zero_shot_prompt():
    """Asking thee model to perform a task without providing any prior examples or guidance, relying entirely on the AI's prtrained knowledge."""

    user_input = input("Enter your prompt: ")

    interaction = google_client.interactions.create(
        model="gemini-pro-latest",
        input=user_input,
    )

    return interaction
