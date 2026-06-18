from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")


def search(query, index, chunks, top_k=3):
    query_embedding = model.encode([query]).astype("float32")

    distances, indices = index.search(
        np.array(query_embedding).astype("float32"),
        top_k
    )

    results = []

    for idx in indices[0]:
        results.append(chunks[idx])

    return results