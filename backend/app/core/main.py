"""
    app.core.main
    ~~~~~~~~~~~~~~
    Defines abstract classes to handle logic and database layer
"""

from sqlalchemy.orm import Session

class DBSessionContext(object):
    def __init__(self, db: Session = None):
        self.db = db

class AppService(DBSessionContext):
    pass

class AppRepository(DBSessionContext):
    model = None

    def create(self, data: dict):
        """
            Generic method to create a single record
            depending of the model assigned to the repository

            - Args: data: dict

            - Returns:
                The created record
        """
        object = None
        try:
            for key,value in data.items():
                if(hasattr(self.model, key) and value is not None):
                    setattr(object, key, value)
            self.db.add(self.model)
            self.db.commit()

            object = self.db.refresh(self.model)
        except Exception as e:
            self.db.rollback()
            raise e
        return object