"""
    app.models.company
    ~~~~~~~~~~~~~~~~~~~
    Defines the Pydantic model for the Company resource
"""

from pydantic import BaseModel
from typing import Optional


class Company(BaseModel):
    firestore_id: str
    category: str
    subcategory: Optional[str]
    description: str
    first_name: str
    last_name: str
    email_address: str
    phone_number: str
    brothers_role: Optional[str] 
    business_name: str
    business_location: str
    website: Optional[str] 
    chapter_affiliation: Optional[str] 
    university_affiliation: Optional[str] 
    street_address: str
    city: str
    state: str
    zip_code: Optional[str] 
    country: str
    deleted_at: Optional[str] 
        
    class Config:
        orm_mode = True