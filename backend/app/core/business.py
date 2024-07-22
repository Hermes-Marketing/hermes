"""
    app.core.business
    ~~~~~~~~~~~~~~~~~
    Defines all functions that operate on the "business" collection in the database

"""
import logging
from fastapi_pagination.ext.sqlalchemy import paginate
from app.core.main import AppRepository
from app.models.business import Business
from fastapi_pagination import Page

class BusinessRepository(AppRepository):
    def get_all_businesses(self, collection_name: str) -> Page[Business]:
        """
        Get all businesses from the specified collection

        - Args: collection_name: str

        - Returns:
            Paged list of all businesses in the specified collection
        """
        logging.info("Collection name: %s", collection_name)
        logging.info("DB Session: %s", self.db)

        # Access the collection
        collection_ref = self.db.collection(collection_name)
        
        # Query the collection (no direct equivalent to SQL query here)
        docs = collection_ref.stream()
        
        # Convert Firestore documents to Business instances
        businesses = [Business(**doc.to_dict()) for doc in docs]

        # Paginate the results (assuming you have a way to handle pagination for Firestore)
        return paginate(businesses)
