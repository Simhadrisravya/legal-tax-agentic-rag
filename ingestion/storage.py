import faiss
import numpy as np

def load_vector_store():
    index = faiss.read_index(
        "vector_db/legal_index.faiss"
    )
    embeddings = np.load(
        "vector_db/legal_embeddings.npy"
    )
    return index, embeddings


def save_vector_store(index, embeddings):
    faiss.write_index(
        index,
        "vector_db/legal_index.faiss"
    )
    np.save(
        "vector_db/legal_embeddings.npy",
        embeddings
    )