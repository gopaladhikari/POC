from google import genai

google_client = genai.Client()


def cot():
    """Enhancing the reasoning abilities of LLMs by breaking down complex tasks into simpler sub-steps. This encourages the model to reason through a problem step-by-step to arrive at a logical conclusion."""

    system_rules = """
    You are a meticulous problem solver. You must use Chain-of-Thought reasoning.
    Before you provide the final answer, you must break down the problem step-by-step.
    
    Structure your response exactly like this:
    Step 1: [Your first calculation]
    Step 2: [Your next calculation]
    ...
    Final Answer: [Your conclusive answer]
    """

    # user_input = input("Enter your prompt: ")

    user_puzzle = "A snail is at the bottom of a 20-foot well. Each day, it climbs up 5 feet, but at night, it slips back down 4 feet. How many days will it take for the snail to reach the top of the well?"

    interaction = google_client.interactions.create(
        model="gemini-3.6-flash",
        input=user_puzzle,
        system_instruction=system_rules,
    )

    return interaction


# Output


# Step 1: Calculate the net daily progress of the snail for standard days. The snail climbs 5
# feet during the day and slips back 4 feet at night, resulting in a net progress of 5 - 4 = 1
# foot per day.
# Step 2: Determine the height required before the final climb. Since the snail climbs 5 feet
# on the final day to reach the top (20 feet) and won't slip back once it reaches the top, we
# subtract the last day's climb from the total height: 20 feet - 5 feet = 15 feet.
# Step 3: Calculate the number of full days needed to reach 15 feet. At a rate of 1 foot per
# day, it takes 15 days for the snail to reach a height of 15 feet at the end of the night.
# Step 4: Add the final day. On the 16th day, starting at 15 feet, the snail climbs 5 feet
# during the day to reach 15 + 5 = 20 feet, reaching the top of the well.

# Final Answer: 16 days
