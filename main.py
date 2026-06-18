from fastapi import FastAPI

from ingestion.storage import load_vector_store
from load_chunks import load_chunks
from load_metadata import load_metadata

from bm25_search import create_bm25
from hybrid_search import hybrid_search

from ingestion.generator import generate_answer

from query_router import route_query
from section_search import get_section
from multi_section_search import get_sections

from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")

# =====================================
# LOAD COMPONENTS
# =====================================

print("Loading Vector Store...")
index,_ = load_vector_store()

print("Loading Chunks...")
chunks = load_chunks()

print("Loading Metadata...")
metadata = load_metadata()

print("Creating BM25...")
bm25 = create_bm25(chunks)

print("System Ready!")

# =====================================
# HOME
# =====================================

@app.get("/")
def home():

    return {
        "message": "Legal Tax Agentic RAG Running"
    }

# =====================================
# ASK
# =====================================

@app.get("/ask")
def ask(query: str):

    try:

        print("\n================================")
        print("STEP 1: Request Received")
        print("Query:", query)

        # ==========================
        # QUERY ROUTER
        # ==========================

        route = route_query(query)

        target_doc = route.get("document")

        target_section = route.get("section")

        target_sections = route.get("sections")

        print("Target Document:", target_doc)

        # =====================================
        # MULTI SECTION MODE
        # =====================================

        if target_sections:

            print(
                "MULTI SECTION MODE:",
                target_sections
            )

            section_data = get_sections(
                target_doc,
                target_sections
            )

            context = []

            for item in section_data:

                context.append(
                    item["text"]
                )

            answer = generate_answer(
                query,
                context
            )

            print("STEP 2: Multi Section Retrieval")
            print("Sections Retrieved:", len(context))

            print("================================\n")

            return {
                "question": query,
                "document": target_doc,
                "sections": target_sections,
                "answer": answer,
                "sources": context
            }

        # =====================================
        # SINGLE SECTION MODE
        # =====================================

        if target_section:

            print(
                "DIRECT SECTION MODE:",
                target_section
            )

            section_data = get_section(
                target_doc,
                target_section
            )

            if section_data:

                answer = generate_answer(
                    query,
                    [section_data["text"]]
                )

                print(
                    "STEP 2: Direct Section Retrieval"
                )

                print("================================\n")

                return {
                    "question": query,
                    "document": target_doc,
                    "section": target_section,
                    "answer": answer,
                    "sources": [
                        section_data["text"]
                    ]
                }

        # =====================================
        # HYBRID SEARCH FALLBACK
        # =====================================

        print("HYBRID SEARCH MODE")

        results = hybrid_search(
            query,
            bm25,
            index,
            chunks
        )

        print(
            "STEP 2: Hybrid Search Completed"
        )

        print(
            "Results Found:",
            len(results)
        )

        answer = generate_answer(
            query,
            results
        )

        print(
            "STEP 3: Answer Generated"
        )

        print("================================\n")

        return {
            "question": query,
            "document": target_doc,
            "answer": answer,
            "sources": results
        }

    except Exception as e:

        import traceback

        print(
            traceback.format_exc()
        )

        return {
            "question": query,
            "error": str(e)
        }
