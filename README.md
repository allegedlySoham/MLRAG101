# MLRAG101
# chat-with-my-notes

A RAG (Retrieval-Augmented Generation) project that lets you ask questions
over your own PDFs: class notes, papers, any documents — and get answers
grounded in that content instead of a generic LLM response.

Built from scratch as a learning project. No AI-generated code, every
line is written and understood by me, step by step.

## What this does

1. Extracts text from a set of PDFs
2. Splits the text into overlapping chunks
3. Embeds each chunk into a vector using a local embedding model
4. Stores the vectors in a local vector database (ChromaDB)
5. On a question: embeds the question, retrieves the most relevant chunks,
   and passes them to an LLM to generate a grounded answer
6. Serves this through a simple chat interface

## Why RAG

An LLM only "knows" its training data plus whatever text is in its prompt.
It hasn't read my notes, and a whole PDF is too big to paste into a single
prompt. RAG solves this by finding only the relevant paragraphs first,
then feeding just those into the LLM instead of fine-tuning a model or
dumping an entire document in.

## Tech stack

| Piece | Tool |
|---|---|
| PDF text extraction | `pypdf` |
| Chunking | custom (fixed-size, with overlap) |
| Embeddings | `sentence-transformers` (`all-MiniLM-L6-v2`), local, no API key |
| Vector DB | ChromaDB (local) |
| LLM for answering | Gemini API (free tier) |
| Interface | CLI first, then Streamlit |

## Project status

Building over 21 days, starting Sept 23, 2026.

- [ ] Phase 1 — Understand the problem RAG solves
- [ ] Phase 2 — Embeddings/cosine similarity intuition (hand exercise)
- [ ] Phase 3 — Environment setup
- [ ] Phase 4 — PDF text extraction
- [ ] Phase 5 — Chunking
- [ ] Phase 6 — Generate embeddings
- [ ] Phase 7 — Store in ChromaDB
- [ ] Phase 8 — Retrieval
- [ ] Phase 9 — LLM Q&A
- [ ] Phase 10 — Streamlit interface
- [ ] Phase 11 — Testing, tuning, edge cases

## Setup

_(to be filled in once the environment and dependencies are in place)_

```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Usage

_(to be filled in once the CLI/Streamlit interface exists)_

## Notes

This repo is a learning log as much as a project, commits will track
progress phase by phase rather than arriving as one finished dump.