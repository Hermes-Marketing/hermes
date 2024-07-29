"""
    app.core.company
    ~~~~~~~~~~~~~~~~~~

    Defines the company repository class, which operates on the companies collection in Firestore
"""

from typing import List
from app.core.main import AppRepository
from app.models.company import Company
from google.cloud.firestore_v1 import FieldFilter
from app.config.settings import get_settings
from fastapi import HTTPException, status, Response
import logging
from datetime import datetime

settings = get_settings()


class CompanyRepository(AppRepository):
    def get_single(self, id: str) -> Company:
        """
        Returns a single company record from the company collection by its document id

        Args:
            id (str): The document id of the company to retrieve

        Returns:
            Company: The company object from the collection companies

        Raises:
            Exception: If the company does not exist
        """
        doc = (
            self.db.collection(settings.COMPANY_COLLECTION)
            .document(id)
            .get()
        )
        if not doc.exists:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Company not found",
            )
        return Company(
            firestore_id=doc.id,
            category=doc.get("category"),
            sub_category=doc.get("subcategory"),
            description=doc.get("description"),
            first_name=doc.get("first_name"),
            last_name=doc.get("last_name"),
            email_address=doc.get("email_address"),
            phone_number=doc.get("phone_number"),
            brothers_role=doc.get("brothers_role"),
            business_name=doc.get("business_name"),
            business_location=doc.get("business_location"),
            website=doc.get("website"),
            chapter_affiliation=doc.get("chapter_affiliation"),
            university_affiliation=doc.get("university_affiliation"),
            street_address=doc.get("street_address"),
            city=doc.get("city"),
            state=doc.get("state"),
            zip_code=doc.get("zip_code"),
            country=doc.get("country"),
            deleted_at=doc.get("deleted_at"),
        )

    def get_all_companies(self) -> List[Company]:
        """
        Get all companies from the specified collection.

        Args:
            collection_name (str): The name of the collection to query.

        Returns:
            List[Company]: A list of all companies in the company collection
        """
        companies = []
        try:
            docs = self.db.collection(
                settings.COMPANY_COLLECTION
            ).stream()
            for doc in docs:
                company_data = doc.to_dict()
                company = Company(
                    firestore_id=doc.id,
                    category=company_data.get("category"),
                    sub_category=company_data.get("subcategory"),
                    description=company_data.get("description"),
                    first_name=company_data.get("first_name"),
                    last_name=company_data.get("last_name"),
                    email_address=company_data.get("email_address"),
                    phone_number=company_data.get("phone_number"),
                    brothers_role=company_data.get("brothers_role"),
                    business_name=company_data.get("business_name"),
                    business_location=company_data.get(
                        "business_location"
                    ),
                    website=company_data.get("website"),
                    chapter_affiliation=company_data.get(
                        "chapter_affiliation"
                    ),
                    university_affiliation=company_data.get(
                        "university_affiliation"
                    ),
                    street_address=company_data.get("street_address"),
                    city=company_data.get("city"),
                    state=company_data.get("state"),
                    zip_code=company_data.get("zip_code"),
                    country=company_data.get("country"),
                    deleted_at=company_data.get("deleted_at"),
                )
                companies.append(company)
        except Exception as e:
            logging.error("Error: %s", e)
            raise e

        return companies

    def get_by_state(self, state: str) -> List[Company]:
        """
        Get all companies from the specified collection by the given state.

        Args:
            state (str): The state to filter by.

        Returns:
            List[Company]: A list of all companies in the company collection

        Raises:
            Exception: If no companies are found in the given state
        """
        companies = []
        try:
            docs = list(
                self.db.collection(settings.COMPANY_COLLECTION)
                .where(filter=FieldFilter("state", "==", state))
                .stream()
            )
            if not docs:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"No companies found in {state}",
                )
            for doc in docs:
                company_data = doc.to_dict()
                logging.info("Company Data: %s", company_data)
                company = Company(
                    firestore_id=doc.id,
                    category=company_data.get("category"),
                    sub_category=company_data.get("subcategory"),
                    description=company_data.get("description"),
                    first_name=company_data.get("first_name"),
                    last_name=company_data.get("last_name"),
                    email_address=company_data.get("email_address"),
                    phone_number=company_data.get("phone_number"),
                    brothers_role=company_data.get("brothers_role"),
                    business_name=company_data.get("business_name"),
                    business_location=company_data.get(
                        "business_location"
                    ),
                    website=company_data.get("website"),
                    chapter_affiliation=company_data.get(
                        "chapter_affiliation"
                    ),
                    university_affiliation=company_data.get(
                        "university_affiliation"
                    ),
                    street_address=company_data.get("street_address"),
                    city=company_data.get("city"),
                    state=company_data.get("state"),
                    zip_code=company_data.get("zip_code"),
                    country=company_data.get("country"),
                    deleted_at=company_data.get("deleted_at"),
                )
                companies.append(company)
        except HTTPException as http_exc:
            logging.error("HTTP error occurred: %s", http_exc.detail)
            raise http_exc
        except Exception as e:
            logging.error(
                "An unexpected error occurred while fetching companies for state '%s': %s",
                state,
                e,
            )
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"An unexpected error occurred while fetching companies in state: {state}",
            )

        return companies

    def get_by_category(self, category: str) -> List[Company]:
        """
        Get all companies from the specified collection by category.

        Args:
            category (str): The category of the company to query.

        Returns:
            List[Company]: A list of all companies in the company collection by category

        Raises:
            Exception(404): An error occurred while fetching the companies
        """
        companies = []
        try:
            docs = list(
                self.db.collection("companies")
                .where(filter=FieldFilter("category", "==", category))
                .stream()
            )
            if not docs:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"No companies found for category: {category}",
                )
            for doc in docs:
                company_data = doc.to_dict()
                company = Company(
                    firestore_id=doc.id,
                    category=company_data.get("category"),
                    sub_category=company_data.get("subcategory"),
                    description=company_data.get("description"),
                    first_name=company_data.get("first_name"),
                    last_name=company_data.get("last_name"),
                    email_address=company_data.get("email_address"),
                    phone_number=company_data.get("phone_number"),
                    brothers_role=company_data.get("brothers_role"),
                    business_name=company_data.get("business_name"),
                    business_location=company_data.get(
                        "business_location"
                    ),
                    website=company_data.get("website"),
                    chapter_affiliation=company_data.get(
                        "chapter_affiliation"
                    ),
                    university_affiliation=company_data.get(
                        "university_affiliation"
                    ),
                    street_address=company_data.get("street_address"),
                    city=company_data.get("city"),
                    state=company_data.get("state"),
                    zip_code=company_data.get("zip_code"),
                    country=company_data.get("country"),
                    deleted_at=company_data.get("deleted_at"),
                )
                companies.append(company)
        except HTTPException as http_exc:
            logging.error("HTTP error occurred: %s", http_exc.detail)
            raise http_exc
        except Exception as e:
            logging.error(
                "An unexpected error occurred while fetching companies for category '%s': %s",
                category,
                e,
            )
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="An unexpected error occurred while fetching companies",
            )

        return companies
    
    def delete_company(self, id: str) -> None:
        """
        Delete a single company record from the company collection by its document id

        Args:
            id (str): The document id of the company to delete

        Returns:
            Response: Returns a 204 status code if the company was successfully deleted
        """
        company = self.get_single(id)
        company.deleted_at = datetime.now() 

        try:
            self.db.collection(settings.COMPANY_COLLECTION).document(id).set(company.dict())

        except Exception:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"An unexpected error occurred while deleting company: {id}",
            )
        return Response(status_code=status.HTTP_204_NO_CONTENT)
