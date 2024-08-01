"""
    app.schemas.company
    ~~~~~~~~~~~~~~~~~~~~~~
    Defines all the Pydantic schemas related to company resource

"""

from pydantic import BaseModel
from typing import Optional

class Company(BaseModel):
    category: Optional[str] = None
    sub_category: Optional[str] = None
    description: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email_address: Optional[str] = None
    phone_number: Optional[str] = None
    brothers_role: Optional[str] = None
    business_name: Optional[str] = None
    business_location: Optional[str] = None
    website: Optional[str] = None
    chapter_affiliation: Optional[str] = None
    university_affiliation: Optional[str] = None
    street_address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None
    country: Optional[str] = None
    deleted_at: Optional[str] = None

