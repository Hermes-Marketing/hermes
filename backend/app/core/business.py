"""
    app.core.business
    ~~~~~~~~~~~~~~~~~~

    Defines the business repository class, which operates on the business collection in Firestore
"""

import logging
from typing import List
from app.core.main import AppRepository
from app.models.business import Business


logging.basicConfig(level=logging.INFO)

class BusinessRepository(AppRepository):
    def get_all_businesses(self, collection_name: str) -> List[Business]:
        """
        Get all businesses from the specified collection.

        Args:
            collection_name (str): The name of the collection to query.

        Returns:
            List[Business]: A list of all businesses in the specified collection.
        """
        businesses = []
        try:
            docs = self.db.collection(collection_name).stream()
            for doc in docs:
                business_data = doc.to_dict()
                business = Business(
                    firestore_id=doc.id,
                    category=business_data.get('category'),
                    sub_category=business_data.get('subcategory'),
                    description=business_data.get('description'),
                    first_name=business_data.get('first_name'),
                    last_name=business_data.get('last_name'),
                    email_address=business_data.get('email_address'),
                    phone_number=business_data.get('phone_number'),
                    brothers_role=business_data.get('brothers_role'),
                    business_name=business_data.get('business_name'),
                    business_location=business_data.get('business_location'),
                    website=business_data.get('website'),
                    chapter_affiliation=business_data.get('chapter_affiliation'),
                    university_affiliation=business_data.get('university_affiliation'),
                    street_address=business_data.get('street_address'),
                    city=business_data.get('city'),
                    state=business_data.get('state'),
                    zip_code=business_data.get('zip_code'),
                    country=business_data.get('country'),
                    deleted_at=business_data.get('deleted_at')
                )
                businesses.append(business)
        except Exception as e:
            logging.error("Error: %s", e)
            raise e

        return businesses