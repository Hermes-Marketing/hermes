# Corrected import statement without trailing comma
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.api.v1.core import get_document_from_db, update_document_in_db, delete_document_from_db, valid_collection_name

# Create a new APIRouter instance
router = APIRouter()
#async calls to db
#promise object
@router.delete("/document/{collection_name}/{document_id}")
async def delete_document(collection_name: str, document_id: str):
    """
    Delete a document from a collection using the collection name and document ID.
    - **collection_name**: Unique identifier for the collection.
    - **document_id**: Unique identifier for the document within the collection.
    """
    if not valid_collection_name(collection_name):
        raise HTTPException(status_code=400, detail="Invalid collection name")    
    try:
        document = await get_document_from_db(collection_name, document_id)
        if document is None:
            raise HTTPException(status_code=404, detail="Document not found")
        
        await delete_document_from_db(collection_name, document_id)
        return JSONResponse(status_code=200, content={"message": "Document deleted"})
    except Exception as e:
        return HTTPException(detail=str(e))


  
