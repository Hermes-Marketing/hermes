from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.v1.api import router as api_router
import uvicorn

app = FastAPI(
    title="Hermes API",
    version="1.0.0",
    docs_url="/docs",
)

app.mount("/", StaticFiles(directory="../frontend/dist", html=True), name="static")

# Include the API router from v1
app.include_router(api_router, prefix="/v1")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)