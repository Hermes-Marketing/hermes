# Corrected import statement without trailing comma
from fastapi import APIRouter

router = APIRouter()

@router.get("/document/{collection_name}/{document_id}")
def get_document(collection_name: str, document_id: str):
    # Your endpoint logic here
    if not valid_collection_name(collection_name):
        return {"error": "Invalid collection name"}, 400
    
    try:
        document = get_document_from_db(collection_name, document_id)

        if document is None:
            return {"error": "Document not found"}, 404
        else:
            return document
    except Exception as e:
        return {"error": str(e)}, 500
    
    pass

    #endpoint passes to data to core function

    #function executes and returns response
    #put or patch
    
    #return response
    
  
