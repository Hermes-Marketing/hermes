"""
    app.models.business
    ~~~~~~~~~~~~~~~~~~~
    Defines the business model for the application
"""
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Business(Base):
    __tablename__ = 'businesses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String)
    sub_category = Column(String, nullable=True)  
    description = Column(String, nullable=True)  
    first_name = Column(String)
    last_name = Column(String)
    email_address = Column(String, nullable=True)  
    phone_number = Column(String, nullable=True)  
    brothers_role = Column(String)
    business_name = Column(String)
    business_location = Column(String)
    website = Column(String, nullable=True)  
    chapter_affiliation = Column(String, nullable=True)  
    university_affiliation = Column(String, nullable=True)  
    street_address = Column(String)
    city = Column(String)
    state = Column(String)
    zip_code = Column(String)
    country = Column(String)
    deleted_at = Column(String, nullable=True)