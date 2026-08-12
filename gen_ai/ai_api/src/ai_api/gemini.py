from google import genai

google_client = genai.Client()


def google_genai():

    user_input = input("Enter your prompt: ")

    interaction = google_client.interactions.create(
        model="gemini-3.5-flash",
        input=user_input,
        system_instruction="You are an expert AI software engineer. Explain concepts clearly and concisely.",
    )

    return interaction
