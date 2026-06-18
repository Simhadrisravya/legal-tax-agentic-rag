import os

def generate_metadata(filepath):

    filename = os.path.basename(filepath)

    return {
        "filename": filename,
        "document_type": "legal",
        "jurisdiction": "India"
    }