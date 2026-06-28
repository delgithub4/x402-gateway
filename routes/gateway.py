from fastapi import APIRouter

router = APIRouter(
    prefix="/gateway",
    tags=["Gateway"]
)


@router.get("/")
def gateway():

    return {

        "message": "Gateway ready"

    }
