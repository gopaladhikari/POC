from google import genai
from pydantic import BaseModel

client = genai.Client()


def generated_knowledge(user_question: str, topic: str):

    knowledge_prompt = f"Generate 4 foundational, highly accurate facts about: {topic}"

    knowledge_interaction = client.interactions.create(
        model="gemini-3.6-flash", input=knowledge_prompt
    )

    generated_facts = knowledge_interaction.output_text
    print("--- Generated Knowledge ---")
    print(generated_facts)
    print("---------------------------\n")

    final_prompt = f"""
    Use the following verified facts to answer the user's question accurately.
    
    Verified Facts:
    {generated_facts}
    
    User Question: {user_question}
    """

    final_interaction = client.interactions.create(
        model="gemini-3.6-flash", input=final_prompt
    )

    return final_interaction
