"""
    app.api.v1.endpoints.business
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Defines all available endpoints for the business resource
"""

from fastapi import APIRouter, status, Depends
from app.schemas.business import Business
from app.core.business import BusinessRepository
from app.database.config import get_db
from typing import List


router = APIRouter()


@router.get("/{collection_name}", status_code=status.HTTP_200_OK, response_model=List[Business])
async def get_all_businesses(collection_name: str, db_session=Depends(get_db)):
    """
    Get all businesses from the specified collection

    - Args: collection_name: str

    - Returns:
        Paged list of all businesses in the specified collection
    """
    
    return BusinessRepository(db_session).get_all_businesses(collection_name)
