from pydantic import BaseModel, Field


class WeatherResponse(BaseModel):
    city_detected: str = Field(description="The city the user asked about")
    raw_temperature: str = Field(
        description="The exact temperature returned by the tool"
    )
    friendly_summary: str = Field(
        description="A polite 1-sentence summary for the user"
    )
    is_raining: bool = Field(
        description="True if the condition includes rain, showers, or drizzle"
    )
