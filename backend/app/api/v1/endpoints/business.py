"""
    app.api.v1.endpoints.business
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Defines all available endpoints for the business resource
"""

from fastapi import APIRouter, status, Depends
from fastapi_pagination import Page
from app.schemas.business import Business
from app.core.business import BusinessRepository
from app.database.config import get_db
import logging
router = APIRouter()

logging.basicConfig(level=logging.INFO)




@router.get("/{collection_name}", status_code=status.HTTP_200_OK, response_model=Page[Business])
async def get_all_businesses(collection_name: str, db_session=Depends(get_db)):
    """
    Get all businesses from the specified collection

    - Args: collection_name: str

    - Returns:
        Paged list of all businesses in the specified collection
    """
    print("here")
    logging.info("Collection name: %s", collection_name)
    logging.info("DB Session: %s", db_session)
    return BusinessRepository(db_session).get_all_businesses(collection_name)
