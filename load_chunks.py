def load_chunks():

    with open(
        "vector_db/chunks.txt",
        "r",
        encoding="utf-8"
    ) as f:

        data = f.read()

    chunks = data.split("<<END_CHUNK>>")

    chunks = [
        chunk.strip()
        for chunk in chunks
        if chunk.strip()
    ]

    return chunks