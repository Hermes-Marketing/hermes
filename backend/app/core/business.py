"""
    app.core.business
    ~~~~~~~~~~~~~~~~~
    Defines all functions that operate on the "business" collection in the database

"""
from fastapi_pagination.ext.sqlalchemy import paginate
from app.models.business import Business

class BusinessRepository:
    def get_all_businesses(self, collection_name: str):
        """
        Get all businesses from the specified collection

        - Args: collection_name: str

        - Returns:
            Paged list of all businesses in the specified collection
        """
        query = self.db_session.query(Business).filter_by(collection_name=collection_name)
        return paginate(query)        
    