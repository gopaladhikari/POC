from pydantic import BaseModel, field_validator


class LocationResponse(BaseModel):
    status: str = "success"
    pincode: str
    city: str
    state: str
    district: str


class BulkLocationRequest(BaseModel):
    pincodes: list[str]

    @field_validator("pincodes")
    @classmethod
    def validate_pincodes(cls, pincodes: list[str]):
        for pincode in pincodes:
            if len(pincode) != 6 or not pincode.isdigit():
                raise ValueError("Pincode must be 6 digits long")
        return pincodes


class BulkLocationResponse(BaseModel):
    status: str = "success"
    found: int
    not_found: int
    results: list[LocationResponse]
    missing: list[str]
