from pydantic import BaseModel, computed_field, Field


class Product(BaseModel):
    name: str
    price: float
    quantity: int

    @computed_field
    @property
    def total(self):
        return self.price * self.quantity


class Booking(BaseModel):
    userId: int
    roomId: int
    nights: int = Field(..., ge=1)
    ratePerNight: int

    @computed_field
    @property
    def totalAmount(self):
        return self.nights * self.ratePerNight


booking = Booking(userId=1, roomId=1, nights=2, ratePerNight=100)


print(booking.totalAmount)
