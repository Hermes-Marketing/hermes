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
        try:
            self.verify_data(data)
            self.commit_to_db()
            return self.refresh_model()
        except Exception as e:
            self.db.rollback()
            raise e

    def verify_data(self, data: dict):
        """
            Verifies and sets the data to the model

            - Args: data: dict
        """
        for key, value in data.items():
            if hasattr(self.model, key) and value is not None:
                setattr(self.model, key, value)

    def commit_to_db(self):
        """
            Commits the model to the database
        """
        self.db.add(self.model)
        self.db.commit()

    def refresh_model(self):
        """
            Refreshes the model from the database

            - Returns:
                The refreshed model
        """
        return self.db.refresh(self.model)