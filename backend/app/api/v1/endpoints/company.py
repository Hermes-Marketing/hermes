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
@router.get("/{state}", status_code=status.HTTP_200_OK, response_model=List[Company])
async def get_companies_by_state(state: str,db_session=Depends(get_db)):
    """
    Get all company records from the company collection by the given state

    - Args: state (str) 
        The state to filter the companies by

    - Returns:
            List[Company]: A list of all companies in the company collection filtered by the given state
    """
    
    return CompanyRepository(db_session).get_by_state(state)
