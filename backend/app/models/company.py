"""
    app.models.company
    ~~~~~~~~~~~~~~~~~~~
    Defines the Pydantic model for the Business resource
"""

from pydantic import BaseModel
from typing import Optional


class Company(BaseModel):
    firestore_id: str
    category: str
    sub_category: Optional[str] = None
    description: str
    first_name: str
    last_name: str
    email_address: str
    phone_number: str
    brothers_role: Optional[str] = None
    business_name: str
    business_location: str
    website: Optional[str] = None
    chapter_affiliation: Optional[str] = None
    university_affiliation: Optional[str] = None
    street_address: str
    city: str
    state: str
    zip_code: Optional[str] = None
    country: str
    deleted_at: Optional[str] = None 
        
    class Config:
        orm_mode = True