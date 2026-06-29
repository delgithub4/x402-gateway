from fastapi import FastAPI

from core.config import settings
from core.exceptions import register_exception_handlers
from core.lifespan import lifespan
from core.middleware import register_middleware

from routes.gateway import router as gateway_router
from routes.health import router as health_router


app = FastAPI(
    title=settings.APP_NAME,
    description=settings.SERVICE_DESCRIPTION,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
    lifespan=lifespan,
)

register_middleware(app)
register_exception_handlers(app)

app.include_router(
    health_router,
    prefix=settings.API_PREFIX,
)

app.include_router(
    gateway_router,
    prefix=settings.API_PREFIX,
)


@app.get("/", tags=["Root"])
async def root():

    return {
        "service": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
        "status": "running",
    }
