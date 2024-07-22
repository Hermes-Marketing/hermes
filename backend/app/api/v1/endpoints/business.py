"""
    app.api.v1.endpoints.business
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Defines all available endpoints for the business resource
"""

from fastapi import APIRouter, status, Depends
from fastapi_pagination import Page
from app.schemas.business import Business
from app.core.business import BuisnessRepository
from app.database.config import get_db

router = APIRouter()



@router.get("/business/{collection_name}", status_code=status.HTTP_200_OK, response_model=Page[Business])
async def get_all_businesses(collection_name: str, db_session=Depends(get_db)):
    """
    Get all businesses from the specified collection

    - Args: collection_name: str

    - Returns:
        Paged list of all businesses in the specified collection
    """
    return BuisnessRepository(db_session).get_all_businesses(collection_name)