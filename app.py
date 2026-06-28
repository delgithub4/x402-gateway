from fastapi import FastAPI

from routes.gateway import router as gateway_router
from routes.health import router as health_router

app = FastAPI(
    title="x402-gateway",
    version="1.0.0"
)

app.include_router(gateway_router)
app.include_router(health_router)


@app.get("/")
def home():

    return {

        "service": "x402-gateway",

        "status": "running"

    }
