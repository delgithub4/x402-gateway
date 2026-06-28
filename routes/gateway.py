from fastapi import APIRouter

from services.gateway_service import GatewayService

router = APIRouter(
    prefix="/gateway",
    tags=["Gateway"]
)

gateway_service = GatewayService()


@router.get("/{service}")
def gateway(
    service: str
):

    return gateway_service.forward(
        service
    )
