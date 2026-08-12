from typing import TypeVar, Type
from pydantic import BaseModel
from google import genai

client = genai.Client()

T = TypeVar("T", bound=BaseModel)


def ask_ai(prompt: str, schema_class: Type[T]) -> T:
    """
    A reusable wrapper that handles the messy JSON schema
    configuration and returns a fully parsed Pydantic object.
    """
    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=prompt,
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": schema_class.model_json_schema(),
        },
    )

    return schema_class.model_validate_json(interaction.output_text)  # type: ignore
