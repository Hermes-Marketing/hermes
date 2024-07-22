"""
app.api.v1.api
~~~~~~~~~~~~~~~~
This module implements the API endpoints for the v1 API.
"""

import app.api.v1.endpoints as ep
from fastapi import APIRouter

router = APIRouter()

router.include_router(ep.business.router, prefix="/business", tags=["business"])