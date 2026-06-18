from load_chunks import load_chunks
from bm25_search import create_bm25
from hybrid_search import hybrid_search

from ingestion.storage import load_vector_store

chunks = load_chunks()

index, _ = load_vector_store()

bm25 = create_bm25(chunks)

query = "What is cancellation of registration?"

results = hybrid_search(
    query,
    bm25,
    index,
    chunks
)

print()

for i, result in enumerate(results):

    print(f"\n--- Result {i+1} ---\n")

    print(result[:800])