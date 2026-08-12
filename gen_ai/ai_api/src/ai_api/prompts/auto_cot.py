from google import genai
from rich import print

google_client = genai.Client()


def chat():
    print("Chat started! (Type 'quit' to exit)")

    last_interaction_id = None

    system_instruction = """
    You are an expert analytical assistant that uses Chain-of-Thought (CoT) reasoning.
    
    For every question or problem presented by the user, you MUST format your response as follows:
    
    ### 🧠 Reasoning Steps
    1. **Understand the Request**: Identify what the user is asking and list key constraints/facts.
    2. **Step-by-Step Analysis**: Work through the logic, math, or structure step-by-step.
    
    ### 💡 Final Answer
    State the final conclusion or solution clearly and concisely based on your reasoning above.
    """

    while True:
        user_input = input("Enter your prompt: ")
        if user_input.lower() == "quit":
            break

        response = google_client.interactions.create(
            model="gemini-3.6-flash",
            input=user_input,
            system_instruction=system_instruction,
            previous_interaction_id=last_interaction_id,
        )

        last_interaction_id = response.id  # type: ignore
        print("You: ", user_input)
        print(f"Gemini: {response.output_text}")  # type: ignore
