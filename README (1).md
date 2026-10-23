# Legal & Tax Assistant (Agentic RAG for Indian Tax Law)

Ask questions about the **Income Tax Act** and **GST Act** and get answers grounded in the actual statute text, with sources.

**Live demo:** https://legal-tax-agentic-rag.vercel.app
(The first request after a quiet period can take up to a minute while the backend wakes up.)

![Screenshot](docs/screenshot.png)

## What it does
- Answers questions on the Income Tax Act, GST Act and GST Rules
- Recognises section-specific questions ("What does Section 16 say...") and looks the section up directly
- Uses hybrid retrieval (BM25 keyword search + FAISS vector search) for open questions
- Returns the answer together with the source text it was based on
- Declines questions the documents don't cover instead of guessing

## How it works
1. **Query router** detects the target act and any section number
2. **Retrieval:** direct section lookup, or hybrid BM25 + FAISS search (sentence-transformers `all-MiniLM-L6-v2`)
3. **Generation:** Google Gemini answers using only the retrieved text
4. **API + UI:** FastAPI backend, Next.js frontend

## Tech stack
Python, FastAPI, FAISS, BM25, sentence-transformers, Google Gemini API, Next.js, Docker, Google Cloud Run, Vercel

## Run locally
1. `git clone https://github.com/Simhadrisravya/legal-tax-agentic-rag`
2. `python -m venv venv` and activate it, then `pip install -r requirements.txt`
3. Create `.env` with `GEMINI_API_KEY=your_key`
4. `python save_index.py` to build the search index
5. `uvicorn main:app --reload`, then open http://127.0.0.1:8000/docs
6. Frontend: `cd frontend`, `npm install`, `npm run dev`

## Deployment
Backend runs in Docker on Google Cloud Run; frontend is deployed on Vercel.

## Disclaimer
For information only. Not legal or tax advice.
