# /database/config.py
import firebase_admin
from firebase_admin import credentials, firestore
import logging
import os
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def initialize_firebase():
    """
    Initializes the Firebase app with credentials from environment variables
    and returns a Firestore client.
    """
    if 'ENV' not in os.environ:
        raise ValueError("ENV not set")

    env = os.getenv('ENV')
    logging.info(f"Environment: {env}")

    env_firebase_cred_dict = {
        "type": os.getenv('ACCOUNT_TYPE'),
        "project_id": os.getenv(f'{env.upper()}_PROJECT_ID'),
        "private_key_id": os.getenv(f'{env.upper()}_PRIVATE_KEY_ID'),
        "private_key": os.getenv(f'{env.upper()}_PRIVATE_KEY').replace("\\n", "\n"),
        "client_email": os.getenv(f'{env.upper()}_CLIENT_EMAIL'),
        "client_id": os.getenv(f'{env.upper()}_CLIENT_ID'),
        "auth_uri": os.getenv('FIREB_AUTH_URI'),
        "token_uri": os.getenv('FIREB_TOKEN_URI'),
        "auth_provider_x509_cert_url": os.getenv('FIREB_AUTH_PROVIDER_X509_CERT_URL'),
        "client_x509_cert_url": os.getenv(f'{env.upper()}_CLIENT_X509_CERT_URL'),
        "universe_domain": os.getenv('FIREB_UNIVERSE_DOMAIN'),
    }

    try:
        logging.info("Attempting to initialize Firebase app with provided credentials.")
        cred = credentials.Certificate(env_firebase_cred_dict)
        firebase_admin.initialize_app(cred)
        logging.info("Firebase app initialized successfully.")
        return firestore.client()
    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
    except firebase_admin.exceptions.FirebaseError as fe:
        logging.error(f"FirebaseError: {fe}")
    except Exception as e:
        logging.error(f"Failed to initialize Firebase app: {e}")

def get_db():
    """
    Returns a Firestore client. Initializes the Firebase app if necessary.
    """
    if not firebase_admin._apps:
        return initialize_firebase()
    else:
        return firestore.client()