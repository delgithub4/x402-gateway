from pydantic import BaseModel
from typing import Any


class GatewayRequest(BaseModel):
    route: str
    payload: dict[str, Any] = {}


class GatewayResponse(BaseModel):
    success: bool
    message: str
    data: Any | None = None
