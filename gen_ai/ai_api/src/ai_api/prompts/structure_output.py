from google import genai
from pydantic import BaseModel

client = genai.Client()


class UserProfile(BaseModel):
    first_name: str
    last_name: str
    age: int
    hobbies: list[str]
    is_active: bool


def generate_user():
    system_rules = "You are a creative data generator. Create a fictional user profile."

    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        system_instruction=system_rules,
        input="Generate a profile for a 28-year-old software engineer who loves the outdoors.",
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": UserProfile.model_json_schema(),
        },
    )

    return interaction


# Output

# {
#   "first_name": "Elena",
#   "last_name": "Rostova",
#   "age": 28,
#   "hobbies": [
#     "Trail Running",
#     "Rock Climbing",
#     "Open Source Contributing",
#     "Backpacking",
#     "Landscape Photography"
#   ],
#   "is_active": true
# }
