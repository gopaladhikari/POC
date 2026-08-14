from google import genai
from google.genai import types
import requests

client = genai.Client()

system_instruction = """
You are a highly analytical Weather Assistant. Extract the city from the user, use the get_weather tool, and return a friendly summary.
"""


def get_weather(city: str) -> str:
    """
    Retrieves the current live weather conditions and temperature for a given city or location.

    Args:
        city: The name of the city/location to check the weather for (e.g., "London", "Goa").
    """
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return f"Error: Weather service returned status code {response.status_code}"
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error: Failed to connect to weather service. Details: {str(e)}"


def main():

    chat = client.chats.create(
        model="gemini-3.6-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=0.5,
            tools=[get_weather],
        ),
    )

    print("Weather Assistant is live! (Type 'quit' to exit)")

    while True:
        user_query = input("\nYou: ")

        # Add an exit condition
        if user_query.lower() in ["quit", "exit"]:
            print("Goodbye!")
            break

        try:

            response = chat.send_message(user_query)

            print(f"Gemini: {response.text}")

        except Exception as e:
            print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
