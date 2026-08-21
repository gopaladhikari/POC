from fastapi.responses import JSONResponse
from fastapi import Request


# Custom Exceptions
class PincodeNotFound(Exception):
    def __init__(self, pincode: str):
        self.pincode = pincode


class InValidPincodeError(Exception):
    def __init__(self, pincode: str, reason: str):
        self.pincode = pincode
        self.reason = reason


# Custom Handler


async def pincode_not_found_handler(request: Request, exc: PincodeNotFound):
    return JSONResponse(
        status_code=404, content={"message": f"Pincode {exc.pincode} not found"}
    )


async def invalid_pincode_handler(request: Request, exc: InValidPincodeError):
    return JSONResponse(
        status_code=400,
        content={"message": f"Pincode {exc.pincode} is invalid. {exc.reason}"},
    )
