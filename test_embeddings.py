from ingestion.parser import extract_text
from ingestion.chunker import split_text
from ingestion.embeddings import create_vector_store

pdf = "documents/GST_ACT.pdf"

text = extract_text(pdf)
chunks = split_text(text)

index, embeddings = create_vector_store(chunks)

print("Chunks:", len(chunks))
print("Embedding Shape:", embeddings.shape)
print("Vectors Stored:", index.ntotal)