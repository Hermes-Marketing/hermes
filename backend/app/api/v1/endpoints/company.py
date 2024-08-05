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


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[Company]
)
async def get_all_companies(db_session=Depends(get_db)):
    """
    Get all company records from the company collection

    - Args: collection_name: str

    - Returns:
        list of all the company object within the collection companies
    """

    return CompanyRepository(db_session).get_all_companies()


@router.get(
    "/state/{state}",
    status_code=status.HTTP_200_OK,
    response_model=List[Company],
)
async def get_companies_by_state(state: str, db_session=Depends(get_db)):
    """
    Get all company records from the company collection by the given state

    - Args: state (str)
        The state to filter the companies by

    - Returns:
            List[Company]: A list of all companies in the company collection filtered by the given state
    """

    return CompanyRepository(db_session).get_by_state(state)


@router.get(
    "/category/{category}",
    status_code=status.HTTP_200_OK,
    response_model=List[Company],
)
async def get_by_category(category: str, db_session=Depends(get_db)):
    """
    Get all company records from the company collection

    - Args:
        category(str): the category of the company

    - Returns:
        list of all the company object within the collection companies by category
    """

    return CompanyRepository(db_session).get_by_category(category)


@router.get(
    "/id/{id}", status_code=status.HTTP_200_OK, response_model=Company
)
async def get_company_by_id(id: str, db_session=Depends(get_db)):
    """
    Get a single company record from the company collection by its document id

    - Args: id(str): The document id of the company to retrieve

    - Returns:
        Returns a single company object from the collection companies
    """

    return CompanyRepository(db_session).get_single(id)


@router.delete("/id/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_company(id: str, db_session=Depends(get_db)):
    """
    Delete a single company record from the company collection by its document id

    - Args: id(str): The document id of the company to delete

    - Returns:
        Returns a 204 status code if the company was successfully deleted
    """

    return CompanyRepository(db_session).delete_company(id)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=Company
)
async def create_company(company: Company, db_session=Depends(get_db)):
    """
    Create a new company record in the company collection

    - Args: company (Company): The company object to create

    - Returns:
        Returns the newly created company object
    """

    return CompanyRepository(db_session).create_company(company)



@router.put("/id/{id}", status_code=status.HTTP_200_OK)
async def update_company(id: str, company: Company, db_session=Depends(get_db)):
    """
    Update a single company record from the company collection by its document id

    - Args:
        id(str): The document id of the company to update
        company(Company): The updated company object

    - Returns:
        Returns the updated company object 
    """

    return CompanyRepository(db_session).update_company(id, company)