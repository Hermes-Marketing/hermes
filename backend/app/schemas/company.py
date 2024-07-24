"""
    app.schemas.company
    ~~~~~~~~~~~~~~~~~~~~~~
    Defines all the Pydantic schemas related to businesses

"""

from pydantic import BaseModel
from typing import Optional

class Company(BaseModel):
    category: str
    sub_category: str
    description: str
    first_name: str
    last_name: str
    email_address: str
    phone_number: str
    brothers_role: str
    business_name: str
    business_location: str
    website: str
    chapter_affiliation: str
    university_affiliation: str
    street_address: str
    city: str
    state: str
    zip_code: str
    country: str
    deleted_at: Optional[str]

   