import firebase_admin
from firebase_admin import credentials, firestore
import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    # Use environment variables to create the credentials dictionary
    cred_dict = {
        "type": os.getenv("TYPE"),
        "project_id": os.getenv("PROJECT_ID"),
        "private_key_id": os.getenv("PRIVATE_KEY_ID"),
        "private_key": os.getenv("PRIVATE_KEY").replace('\\n', '\n'),
        "client_email": os.getenv("CLIENT_EMAIL"),
        "client_id": os.getenv("CLIENT_ID"),
        "auth_uri": os.getenv("AUTH_URI"),
        "token_uri": os.getenv("TOKEN_URI"),
        "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
        "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL")
    }
    cred = credentials.Certificate(cred_dict)
    # Initialize the app with Firestore
    app = firebase_admin.initialize_app(cred)
    logging.info("Firebase app initialized successfully.")
    
    # Get a Firestore client
    db = firestore.client()
    
    # Reference to the document in the 'test' collection
    doc_ref = db.collection('test').document('test_doc')
    
    # Attempt to get the document
    doc = doc_ref.get()
    if doc.exists:
        logging.info("Successfully retrieved document from Firestore.")
        doc_data = doc.to_dict()
        for key, value in doc_data.items():
            logging.info(f"{key}: {value}")
    else:
        logging.info("Document does not exist in Firestore.")
except ValueError:
    logging.error("No Firebase app has been initialized yet.")
except Exception as e:
    logging.error(f"Failed to initialize Firebase app or interact with Firestore: {e}")