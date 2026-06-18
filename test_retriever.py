from ingestion.parser import extract_text
from ingestion.chunker import split_text
from ingestion.embeddings import create_vector_store
from ingestion.retriever import search

pdf = "documents/GST_ACT.pdf"

text = extract_text(pdf)
chunks = split_text(text)

index, embeddings = create_vector_store(chunks)

query = "What is GST?"

results = search(query, index, chunks)

print("\nQuestion:")
print(query)

print("\nTop Results:\n")

for i, result in enumerate(results, 1):
    print(f"Result {i}")
    print("-" * 50)
    print(result[:500])
    print()