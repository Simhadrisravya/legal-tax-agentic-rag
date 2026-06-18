from ingestion.parser import extract_text
from ingestion.chunker import split_text
from ingestion.embeddings import create_vector_store
from ingestion.storage import save_vector_store, load_vector_store

pdf = "documents/GST_ACT.pdf"

text = extract_text(pdf)
chunks = split_text(text)

index, embeddings = create_vector_store(chunks)

save_vector_store(index, embeddings)

loaded_index, loaded_embeddings = load_vector_store()

print("Original vectors :", index.ntotal)
print("Loaded vectors   :", loaded_index.ntotal)
print("Embedding shape  :", loaded_embeddings.shape)