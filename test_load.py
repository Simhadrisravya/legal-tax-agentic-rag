from ingestion.storage import load_vector_store
from load_chunks import load_chunks

index, _ = load_vector_store()

chunks = load_chunks()

print("Vectors :", index.ntotal)
print("Chunks  :", len(chunks))