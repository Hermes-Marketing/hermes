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

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=Company)
async def get_company_by_id(id: str, db_session=Depends(get_db)):
    """
    Get a single company record from the company collection by its document id

    - Args: id(str): The document id of the company to retrieve

    - Returns:
        Returns a single company object from the collection companies
    """
    
    return CompanyRepository(db_session).get_single(id)
