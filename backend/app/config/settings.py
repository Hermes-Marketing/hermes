# All Constants defined here

from pydantic import BaseSettings


class Settings(BaseSettings):
    # Collections
    COMPANY_COLLECTION: str = "companies"

def get_settings():
    return Settings()