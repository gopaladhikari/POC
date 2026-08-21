from fastapi import FastAPI, Path
from .exceptions import (
    PincodeNotFound,
    InValidPincodeError,
    invalid_pincode_handler,
    pincode_not_found_handler,
)
from .data import pincode_db
from .models import (
    BulkLocationRequest,
    BulkLocationResponse,
    LocationResponse,
)

app = FastAPI(
    title="Pincode Lookup",
    description="Autofill city and state from pincode during checkout",
    version="1.0.0",
)

app.add_exception_handler(PincodeNotFound, pincode_not_found_handler)  # type: ignore
app.add_exception_handler(InValidPincodeError, invalid_pincode_handler)  # type: ignore


@app.get("/")
def root():
    return {"Hello": "World"}


@app.get("/pincodes", response_model=list[LocationResponse])
def get_pincodes():
    return [
        LocationResponse(status="success", **pincode) for pincode in pincode_db.values()
    ]


@app.get("/pincode/{pincode}", response_model=LocationResponse)
async def get_pincode(
    pincode: str = Path(..., min_length=6, max_length=6, description="6 digit pincode")
):
    if pincode not in pincode_db:
        raise PincodeNotFound(pincode)
    return LocationResponse(status="success", **pincode_db[pincode])


@app.post("/bulk", response_model=BulkLocationResponse)
async def get_bulk_pincode(bulk_pincode_request: BulkLocationRequest):

    missing = []
    results = []

    for pincode in bulk_pincode_request.pincodes:
        if pincode in pincode_db:
            results.append(pincode_db[pincode])
        else:
            missing.append(pincode)

    return BulkLocationResponse(
        status="success",
        found=len(results),
        not_found=len(missing),
        results=results,
        missing=missing,
    )
