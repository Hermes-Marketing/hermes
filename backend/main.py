from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.v1.api import router as api_router
import uvicorn
import os

app = FastAPI(
    title="Hermes API",
    version="1.0.0",
    docs_url="/docs",
)

# Use a relative path for the Docker container
static_dir = "frontend/dist"
if not os.path.exists(static_dir):
    raise RuntimeError(f"Directory '{static_dir}' does not exist")

app.mount("/static", StaticFiles(directory=static_dir, html=True), name="static")

# Include the API router from v1
app.include_router(api_router, prefix="/v1")
for route in app.routes:
    print(f"path: {route.path}, name: {route.name}, methods: {getattr(route, 'methods', 'NONE')}")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
