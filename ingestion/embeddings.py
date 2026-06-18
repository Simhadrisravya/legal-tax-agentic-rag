from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_vector_store(chunks, batch_size=64):
    embeddings = model.encode(
        chunks,
        batch_size=batch_size,
        show_progress_bar=True,
        convert_to_numpy=True
    ).astype("float32")

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    return index, embeddings