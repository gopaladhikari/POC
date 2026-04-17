from pydantic import BaseModel, Field, computed_field


class Booking(BaseModel):
    userId: int
    roomId: int
    nights: int = Field(..., ge=1)
    ratePerNight: int

    @computed_field
    @property
    def totalAmount(self):
        return self.nights * self.ratePerNight
