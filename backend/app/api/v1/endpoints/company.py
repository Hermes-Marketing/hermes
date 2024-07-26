"""
    app.api.v1.endpoints.company
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Defines all available endpoints for the company resource
"""

from fastapi import APIRouter, status, Depends
from app.schemas.company import Company
from app.core.company import CompanyRepository
from app.database.config import get_db
from typing import List


router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[Company])
async def get_all_companies(db_session=Depends(get_db)):
    """
    Get all company records from the company collection

    - Args: collection_name: str

    - Returns:
        list of all the company object within the collection companies
    """
    
    return CompanyRepository(db_session).get_all_companies()

@router.get("/{category}", status_code=status.HTTP_200_OK, response_model=List[Company])
async def get_by_category(category: str,db_session=Depends(get_db)):
    """
    Get all company records from the company collection

    - Args: 
        category(str): the category of the company

    - Returns:
        list of all the company object within the collection companies by category
    """
    
    return CompanyRepository(db_session).get_by_category(category)
