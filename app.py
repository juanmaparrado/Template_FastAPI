import os
from fastapi.responses import JSONResponse
import uvicorn
from configuration.logger_config import logger
from fastapi import FastAPI, Request
from fastapi.concurrency import asynccontextmanager
from routers.example_router import example_router
from slowapi import _rate_limit_exceeded_handler
from configuration.limiter_config import limiter

environment = os.getenv("APP_ENVIRONMENT", None)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Started App")
    yield
    logger.info("Stopped App")



app = FastAPI(
    title = "Example APP",
    root_path = "/example",
    docs_url="/docs",
    lifespan=lifespan,
    openapi_url="/openapi.json"
)

app.state.limiter = limiter
app.add_exception_handler(429, _rate_limit_exceeded_handler)

@app.get("/")
@limiter.limit("2/minute")
async def root(request : Request):
  return {
    "message": "Your FastAPI App is UP.",
    "appEnvironment" : environment
  }

# -------------------------------------------
#                 ROUTERS
# -------------------------------------------

app.include_router(example_router, tags=["Example"])


if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)