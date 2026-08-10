from pydantic import BaseModel, ConfigDict


class StrictProfile(BaseModel):
    model_config = ConfigDict(extra="forbid")

    username: str


# This throws a ValidationError because 'age' is not defined in the model!
profile = StrictProfile(username="Gopal", age=23)
