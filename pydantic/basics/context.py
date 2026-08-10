from pydantic import BaseModel, field_validator
from pydantic_core.core_schema import ValidationInfo


class Order(BaseModel):
    item_id: int

    @field_validator("item_id")
    def check_item_in_stock(cls, v: int, info: ValidationInfo):

        if not info.context:
            raise ValueError("Missing context")

        # Access the external dictionary we passed in
        db_connection = info.context.get("db")

        if not db_connection.is_in_stock(v):
            raise ValueError(f"Item {v} is out of stock")
        return v


# Mock database
class MockDB:
    def is_in_stock(self, item_id):
        return item_id == 1


db = MockDB()

# Pass the database connection into the validation process
order = Order.model_validate(
    {"item_id": 1}, context={"db": db}  # This gets passed to ValidationInfo
)
