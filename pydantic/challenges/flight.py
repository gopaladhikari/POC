from pydantic import BaseModel, model_validator
from typing import Optional


class FlightTicket(BaseModel):
    passenger_name: str
    departure_city: str
    destination_city: str
    ticket_class: Optional[str] = "Economy"

    @model_validator(mode="after")
    def check_destination(cls, values):
        if values["departure_city"] == values["destination_city"]:
            raise ValueError("Departure and destination cities cannot be the same.")
        return values
