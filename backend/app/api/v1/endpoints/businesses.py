# Corrected import statement without trailing comma
from fastapi import APIRouter

router = APIRouter()

@router.get("/document/{collection_name}/{document_id}")
def get_document(collection_name: str, document_id: str):
    # Your endpoint logic here
    pass
