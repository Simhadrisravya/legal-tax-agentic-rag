# Legal Tax Agentic RAG

An agentic Retrieval-Augmented Generation (RAG) system for answering questions about Indian legal and tax documents (e.g. the Income Tax Act, GST Act). It combines hybrid retrieval (BM25 + FAISS vector search) with query routing to specific Acts/sections, and uses an LLM to generate grounded answers with cited sources. The backend is served via FastAPI, with a Next.js (TypeScript) frontend for interacting with it.

## Features

- **Query routing** — detects whether a question targets a specific document, a single section, or multiple sections, and retrieves directly instead of always falling back to full semantic search.
- **Hybrid search** — combines BM25 keyword search with FAISS dense vector search for queries that aren't mapped to a specific section.
- **Multi-section retrieval** — handles questions that span several sections of a document.
- **Grounded answer generation** — retrieved context is passed to an LLM (via LangChain/LangGraph + OpenAI) to produce an answer along with its sources.
- **FastAPI backend** exposing a simple `/ask` endpoint.
- **Next.js frontend** for a chat-style UI on top of the API.

## How it works

1. On startup, `main.py` loads the FAISS vector store, document chunks, metadata, and builds a BM25 index from the chunks.
2. An incoming question to `/ask` is passed to `query_router.route_query`, which determines whether it maps to a specific document/section, multiple sections, or neither.
3. Based on the route:
   - **Multi-section mode** → `multi_section_search.get_sections`
   - **Single section mode** → `section_search.get_section`
   - **Fallback** → `hybrid_search.hybrid_search` (BM25 + FAISS)
4. The retrieved text is passed to `ingestion/generator.py`, which calls the LLM to generate an answer grounded in that context.
5. The API returns the answer along with the source text it was generated from.

## Project structure

```
.
├── documents/              # Source legal/tax documents used for ingestion
├── frontend/                # Next.js (TypeScript) client UI
├── ingestion/               # Document loading, chunking, vector store (FAISS), and answer generation
├── main.py                  # FastAPI app entry point (/ask endpoint)
├── query_router.py          # Routes a query to a document/section
├── document_router.py       # Document-level routing helpers
├── section_search.py        # Direct single-section retrieval
├── multi_section_search.py  # Multi-section retrieval
├── bm25_search.py            # BM25 keyword index/search
├── hybrid_search.py          # Combined BM25 + vector search
├── load_chunks.py / load_metadata.py / metadata_store.py / metadata_search.py / save_index.py
│                             # Data loading and indexing utilities
├── inspect_*.py / find_*.py  # One-off scripts used to explore document/section structure during development
├── test_*.py                 # Test scripts for the components above
└── requirements.txt          # Python dependencies
```

## Setup

### Prerequisites

- Python 3.10+
- Node.js (for the frontend)
- An OpenAI API key

### Backend

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

pip install -r requirements.txt
```

Create a `.env` file in the project root (already excluded from git via `.gitignore`):

```
OPENAI_API_KEY=your_key_here
```

Build the index/vector store from your source documents (check `save_index.py` / `ingestion/` for the exact ingestion script and expected document format), then start the API:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`. Visit `/docs` for interactive Swagger docs, or query directly:

```
GET /ask?query=What does Section 80C of the Income Tax Act cover?
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Example response

Query: `GET /ask?query=What is Section 80C?`

```json
{
  "question": "What is Section 80C?",
  "document": "Income_Tax_Act.pdf",
  "section": "80C",
  "answer": "Section 80C is a provision in the Income-tax Act that allows for deductions in respect of various payments or deposits made by an assessee, being an individual or a Hindu undivided family (HUF). Specifically, it allows for the deduction of the whole amount paid or deposited in the previous year, subject to a maximum limit of one hundred and fifty thousand rupees. These deductible sums include, but are not limited to: life insurance premia, contributions to provident funds, subscriptions to certain equity shares or debentures, tuition fees for full-time education of children, repayment of housing loan principal, contributions to approved superannuation funds, subscriptions to certain savings certificates and deposit schemes, investments in unit-linked insurance plans and mutual funds, term deposits with scheduled banks for a fixed period of not less than five years, and investments in the Senior Citizens Savings Scheme and Post Office Time Deposit.",
  "sources": ["80C. Deduction in respect of life insurance premia, deferred annuity, contributions to provident fund, subscription to certain equity shares or debentures, etc. ..."]
}
```

## Notes

- `.env`, `venv/`, generated vector index files (`vector_db/`, `*.faiss`, `*.npy`), and `node_modules/` are git-ignored — never commit API keys or generated indexes.
- The `test_*.py`, `inspect_*.py`, and `find_*.py` scripts were used during development to validate chunking, section parsing, and retrieval; they aren't required to run the API itself.

---

*This README was generated from the repository's file structure and dependencies — adjust the setup steps, environment variable names, and example queries to match your actual ingestion workflow if they differ.*
