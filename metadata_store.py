import json

def save_metadata(metadata):


    with open(
    "vector_db/metadata.json",
    "w",
    encoding="utf-8"
) as f:

        json.dump(
        metadata,
        f,
        ensure_ascii=False,
        indent=4
    )

