from load_metadata import load_metadata


def metadata_search(query, document):

    metadata = load_metadata()

    filtered_chunks = []

    for item in metadata:

        if item["document"] == document:

            filtered_chunks.append(
                item["text"]
            )

    return filtered_chunks