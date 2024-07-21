from backend.app.database.config import get_db

import json

def main():
    db = get_db()
    doc_ref = db.collection('test').document('test_doc')
    doc = doc_ref.get()
    if doc.exists:
        print(f"Document data:\n{json.dumps(doc.to_dict(), indent=4)}")
    else:
        print("No such document!")

if __name__ == "__main__":
    main()
