# Corrected import statement without trailing comma
from fastapi import APIRouter
from app.api.v1.core import get_document_from_db, update_document_in_db, delete_document_from_db, valid_collection_name

# Create a new APIRouter instance
router = APIRouter()

@router.delete("/document/{collection_name}/{document_id}")
def delete_document(collection_name: str, document_id: str):
    """
    Delete a document from a collection 
    using the collection name and document ID
    """
    if not valid_collection_name(collection_name):
        return {"error": "Invalid collection name"}, 400
    
    try:
        document = get_document_from_db(collection_name, document_id)

        if document is None:
            return {"error": "Document not found"}, 404
        else:
            delete_document_from_db(collection_name, document_id)
            return {"message": "Document deleted"}
    except Exception as e:
        return {"error": str(e)}, 500
    
    pass




    #endpoint passes to data to core function

    #function executes and returns response
    #put or patch
    
    #return response

  
