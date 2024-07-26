"""
    app.core.company
    ~~~~~~~~~~~~~~~~~~

    Defines the company repository class, which operates on the companies collection in Firestore
"""
from typing import List
from app.core.main import AppRepository
from app.models.company import Company
from google.cloud.firestore_v1.base_query import FieldFilter
import logging
from fastapi import HTTPException, status


class CompanyRepository(AppRepository):
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
            docs = self.db.collection('companies').stream()
            for doc in docs:
                company_data = doc.to_dict()
                company = Company(
                    firestore_id=doc.id,
                    category=company_data.get('category'),
                    sub_category=company_data.get('subcategory'),
                    description=company_data.get('description'),
                    first_name=company_data.get('first_name'),
                    last_name=company_data.get('last_name'),
                    email_address=company_data.get('email_address'),
                    phone_number=company_data.get('phone_number'),
                    brothers_role=company_data.get('brothers_role'),
                    business_name=company_data.get('business_name'),
                    business_location=company_data.get('business_location'),
                    website=company_data.get('website'),
                    chapter_affiliation=company_data.get('chapter_affiliation'),
                    university_affiliation=company_data.get('university_affiliation'),
                    street_address=company_data.get('street_address'),
                    city=company_data.get('city'),
                    state=company_data.get('state'),
                    zip_code=company_data.get('zip_code'),
                    country=company_data.get('country'),
                    deleted_at=company_data.get('deleted_at')
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
            docs = list(self.db.collection('companies').where(filter=FieldFilter('state', '==', state)).stream())
            if not docs:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"No companies found in {state}"
                )
            for doc in docs:
                company_data = doc.to_dict()
                logging.info("Company Data: %s", company_data)
                company = Company(
                    firestore_id=doc.id,
                    category=company_data.get('category'),
                    sub_category=company_data.get('subcategory'),
                    description=company_data.get('description'),
                    first_name=company_data.get('first_name'),
                    last_name=company_data.get('last_name'),
                    email_address=company_data.get('email_address'),
                    phone_number=company_data.get('phone_number'),
                    brothers_role=company_data.get('brothers_role'),
                    business_name=company_data.get('business_name'),
                    business_location=company_data.get('business_location'),
                    website=company_data.get('website'),
                    chapter_affiliation=company_data.get('chapter_affiliation'),
                    university_affiliation=company_data.get('university_affiliation'),
                    street_address=company_data.get('street_address'),
                    city=company_data.get('city'),
                    state=company_data.get('state'),
                    zip_code=company_data.get('zip_code'),
                    country=company_data.get('country'),
                    deleted_at=company_data.get('deleted_at')
                )
                companies.append(company)
        except Exception as e:
            logging.error("Error: %s", e)
            raise e

        return companies