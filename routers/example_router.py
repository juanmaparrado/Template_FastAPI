from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from configuration.logger_config import logger
from configuration.limiter_config import limiter

example_router = APIRouter(prefix="/example", tags=["Example"])

@example_router.get("/check", summary="Check the example endpoint")
@limiter.limit("5/minute")
async def checking_example(request : Request):
    logger.info("Example endpoint check is correct")
    return JSONResponse("Example endpoint check is active")
