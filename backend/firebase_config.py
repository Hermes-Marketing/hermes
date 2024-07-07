import firebase_admin
from firebase_admin import credentials, firestore
import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

'''
Environment Global Var 
'''

if 'ENV' not in os.environ:
    raise ValueError("ENV not set")

env = os.getenv("ENV")
logging.info(f"Environment: {env}")

firebase_cred_dict = {
    "type": os.getenv(f'{env.upper()}_TYPE'),
    "project_id": os.getenv(f'{env.upper()}_PROJECT_ID'),
    "private_key_id": os.getenv(f'{env.upper()}_PRIVATE_KEY_ID'),
    "private_key": os.getenv(f'{env.upper()}_PRIVATE_KEY').replace("\\n", "\n"),
    "client_email": os.getenv(f'{env.upper()}_CLIENT_EMAIL'),
    "client_id": os.getenv(f'{env.upper()}_CLIENT_ID'),
    "auth_uri": os.getenv(f'{env.upper()}_AUTH_URI'),
    "token_uri": os.getenv(f'{env.upper()}_TOKEN_URI'),
    "auth_provider_x509_cert_url": os.getenv(f'{env.upper()}_AUTH_PROVIDER_X509_CERT_URL'),
    "client_x509_cert_url": os.getenv(f'{env.upper()}_CLIENT_X509_CERT_URL')
}

try:
    logging.info("Attempting to initialize Firebase app with provided credentials.")
    cred = credentials.Certificate(firebase_cred_dict)
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
