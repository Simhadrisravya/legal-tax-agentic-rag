import json

def load_metadata():

    with open(
        "vector_db/metadata.json",
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)