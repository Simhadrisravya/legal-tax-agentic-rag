import os
import sys
import json
import faiss
import numpy as np

print("--> Script started executing successfully...")

try:
    print("--> Attempting to load ingestion modules...")
    # This is the most common place where silent failures occur due to heavy ML libraries
    from ingestion.embeddings import create_vector_store
    print("--> Ingestion modules loaded perfectly.")
except Exception as e:
    print(f"\n❌ CRITICAL ERROR: Failed to import ingestion embeddings!")
    print(f"Error Details: {e}")
    sys.exit(1)


def get_query_embedding(query_text):
    """Converts text query into a vector using your store logic."""
    try:
        # Pass query as a single-element list to your existing vector store logic
        _, embeddings = create_vector_store([query_text])
        return embeddings.astype("float32")
    except Exception as e:
        print(f"\n❌ ERROR during embedding generation: {e}")
        raise


def search_with_metadata_filter(query_text, target_document=None, top_k=3):
    """Searches the FAISS index and enforces strict metadata filtering."""
    # 1. Verification of DB Files
    if not os.path.exists("vector_db/legal_index.faiss"):
        print("❌ ERROR: 'vector_db/legal_index.faiss' does not exist!")
        return []
    if not os.path.exists("vector_db/metadata.json"):
        print("❌ ERROR: 'vector_db/metadata.json' does not exist!")
        return []

    print("--> Loading FAISS Index and Metadata JSON...")
    index = faiss.read_index("vector_db/legal_index.faiss")
    with open("vector_db/metadata.json", "r", encoding="utf-8") as f:
        metadata = json.load(f)
        
    print(f"--> Database loaded. Total vectors in index: {index.ntotal}")

    # 2. Embedding Generation
    print(f"--> Generating embedding for query: '{query_text}'")
    query_vector = get_query_embedding(query_text)
    
    # 3. FAISS Retrieval
    print("--> Scanning FAISS index space...")
    distances, indices = index.search(query_vector, top_k * 15)
    
    filtered_chunks = []
    
    # 4. Metadata Extraction
    for idx in indices[0]:
        if idx == -1 or idx >= len(metadata):
            continue
            
        meta_item = metadata[idx]
        
        if target_document and meta_item["document"] != target_document:
            continue
            
        filtered_chunks.append({
            "document": meta_item["document"],
            "section": meta_item.get("section", "N/A"),
            "text": meta_item["text"]
        })
        
        if len(filtered_chunks) == top_k:
            break
            
    return filtered_chunks


# =====================================================================
# MAIN RUNNER
# =====================================================================
if __name__ == "__main__":
    print("\n=========================================")
    print("       RUNNING DIAGNOSTIC SEARCH         ")
    print("=========================================\n")
    
    test_query = "What is Section 80C?"
    test_doc = "Income_Tax_Act.pdf" 
    
    try:
        results = search_with_metadata_filter(test_query, target_document=test_doc)
        
        print(f"\n--> Search completed. Found {len(results)} matches.\n")
        
        if not results:
            print("⚠️ No matching segments found for this document filtering constraint.")
            
        for i, res in enumerate(results, 1):
            print(f"[Match {i}] Doc: {res['document']} | Section: {res['section']}")
            print(f"Context snippet:\n{res['text'][:250]}...\n")
            print("-" * 50)
            
    except Exception as global_error:
        print(f"\n❌ RUNTIME CRASH: {global_error}")
        
    print("\n=========================================")