from load_chunks import load_chunks
from bm25_search import create_bm25
from bm25_search import bm25_search

chunks = load_chunks()

print("Chunks Loaded:", len(chunks))

bm25 = create_bm25(chunks)

query = "Section 29"

results = bm25_search(
    query,
    bm25,
    chunks
)

print("\nRESULTS\n")

for i, result in enumerate(results):

    print(f"\n--- Result {i+1} ---\n")

    print(result[:1000])