from bm25_search import bm25_search
from ingestion.retriever import search


def hybrid_search(
    query,
    bm25,
    index,
    chunks
):

    bm25_results = bm25_search(
        query,
        bm25,
        chunks,
        top_k=20
    )

    vector_results = search(
        query,
        index,
        chunks
    )

    print("\n========== BM25 RESULTS ==========") 
    
    for i, result in enumerate(bm25_results[:5]): 
        print(f"\nBM25 {i+1}") 
        print(result[:300]) 
    print("\n========== VECTOR RESULTS ==========") 
    for i, result in enumerate(vector_results[:5]): 
        print(f"\nVECTOR {i+1}") 
        print(result[:300])

    combined = []

    for result in bm25_results:
        if result not in combined:
            combined.append(result)

    for result in vector_results:
        if result not in combined:
            combined.append(result)

    return combined[:5]