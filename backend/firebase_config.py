import firebase_admin
from firebase_admin import credentials, firestore
import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Determine environment mode
env_mode = os.getenv("ENV_MODE", "dev")  # Default to 'dev' if ENV_MODE is not set
logging.info(f"Environment mode: {env_mode}")

# Define environment-specific configurations
def get_cred_dict(env_mode):
    if env_mode == "dev":
        return {
            "type": os.getenv("DEV_TYPE"),
            "project_id": os.getenv("DEV_PROJECT_ID"),
            "private_key_id": os.getenv("DEV_PRIVATE_KEY_ID"),
            "private_key": os.getenv("DEV_PRIVATE_KEY").replace("\\n", "\n"),
            "client_email": os.getenv("DEV_CLIENT_EMAIL"),
            "client_id": os.getenv("DEV_CLIENT_ID"),
            "auth_uri": os.getenv("DEV_AUTH_URI"),
            "token_uri": os.getenv("DEV_TOKEN_URI"),
            "auth_provider_x509_cert_url": os.getenv("DEV_AUTH_PROVIDER_X509_CERT_URL"),
            "client_x509_cert_url": os.getenv("DEV_CLIENT_X509_CERT_URL")
        }
    elif env_mode == "prod":
        return {
            "type": os.getenv("PROD_TYPE"),
            "project_id": os.getenv("PROD_PROJECT_ID"),
            "private_key_id": os.getenv("PROD_PRIVATE_KEY_ID"),
            "private_key": os.getenv("PROD_PRIVATE_KEY").replace("\\n", "\n"),
            "client_email": os.getenv("PROD_CLIENT_EMAIL"),
            "client_id": os.getenv("PROD_CLIENT_ID"),
            "auth_uri": os.getenv("PROD_AUTH_URI"),
            "token_uri": os.getenv("PROD_TOKEN_URI"),
            "auth_provider_x509_cert_url": os.getenv("PROD_AUTH_PROVIDER_X509_CERT_URL"),
            "client_x509_cert_url": os.getenv("PROD_CLIENT_X509_CERT_URL")
        }
    else:
        raise ValueError("Invalid ENV_MODE specified")

cred_dict = get_cred_dict(env_mode)

try:
    logging.info("Attempting to initialize Firebase app with provided credentials.")
    cred = credentials.Certificate(cred_dict)
    app = firebase_admin.initialize_app(cred)
    logging.info("Firebase app initialized successfully.")
    
    # Get a Firestore client
    db = firestore.client()
    
    

    # Reference to the document in the 'test' collection
    doc_ref = db.collection('test').document('test_doc')

    # Attempt to get the document
    try:
        doc = doc_ref.get()
        if doc.exists:
            print("Document data:", doc.to_dict())
        else:
            print("No such document!")
    except Exception as e:
        logging.error(f"Failed to retrieve document: {e}")
except ValueError as ve:
    logging.error(f"ValueError: {ve}")
except firebase_admin.exceptions.FirebaseError as fe:
    logging.error(f"FirebaseError: {fe}")
except Exception as e:
    logging.error(f"Failed to initialize Firebase app or interact with Firestore: {e}")
