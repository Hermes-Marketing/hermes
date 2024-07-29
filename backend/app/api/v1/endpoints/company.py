"""
    app.api.v1.endpoints.company
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Defines all available endpoints for the company resource
"""
from datetime import datetime
from fastapi import APIRouter, status, Depends, HTTPException
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

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=Company)
async def get_company_by_id(id: str, db_session=Depends(get_db)):
    """
    Get a single company record from the company collection by its document id

    - Args: id(str): The document id of the company to retrieve

    - Returns:
        Returns a single company object from the collection companies
    """
    
    return CompanyRepository(db_session).get_single(id)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_company(id: str, db_session=Depends(get_db)):
    """
    Delete a single company record from the company collection by its document id

    - Args: id(str): The document id of the company to delete

    - Returns:
        Returns a single company object from the collection companies
    """
        
    return CompanyRepository(db_session).delete_company(id)
    