"""
    app.models.business
    ~~~~~~~~~~~~~~~~~~~
    Defines the business model for the application
"""

from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Business(Base):
    __tablename__ = 'businesses'
    
    id = Column(String, primary_key=True, index=True)
    category = Column(String)
    sub_category = Column(String)
    description = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email_address = Column(String)
    phone_number = Column(String)
    brothers_role = Column(String)
    business_name = Column(String)
    business_location = Column(String)
    website = Column(String)
    chapter_affiliation = Column(String)
    university_affiliation = Column(String)
    street_address = Column(String)
    city = Column(String)
    state = Column(String)
    zip_code = Column(String)
    country = Column(String)
    deleted_at = Column(String, nullable=True)
