# chat-with-my-notes

A RAG (Retrieval-Augmented Generation) project that lets you ask questions
over your own PDFs — class notes, papers, any documents — and get answers
grounded in that content instead of a generic LLM response.

Built from scratch as a learning project. No AI-generated code — every
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
prompt — and even when it fits, models are worse at using facts buried in
a huge wall of text than a short, focused one. RAG solves this by finding
only the relevant paragraphs first, then feeding just those into the LLM.

## Tech stack

| Piece | Tool |
|---|---|
| PDF text extraction | `pypdf` |
| Chunking | custom (fixed-size, with overlap) |
| Embeddings | `sentence-transformers` (`all-MiniLM-L6-v2`), local, no API key |
| Vector DB | ChromaDB (local) |
| LLM for answering | Gemini API (free tier) |
| Interface | CLI first, then Streamlit |

## Project structure

```
MLRAG101/
  textExtraction.py   # extraction(pdfname) -> full text from a PDF, all pages
  chunking.py          # chunking(text) -> list of overlapping text chunks
  main.py               # wires extraction -> chunking together
  requirements.txt
```

## Project status

Building over 21 days, started Sept 23, 2026.

- [x] Phase 1 — Understand the problem RAG solves
- [x] Phase 2 — Embeddings/cosine similarity intuition (hand exercise)
- [x] Phase 3 — Environment setup
- [x] Phase 4 — PDF text extraction (all pages, via `pypdf`)
- [x] Phase 5 — Chunking (fixed-size, overlap, verified against real notes)
- [ ] Phase 6 — Generate embeddings
- [ ] Phase 7 — Store in ChromaDB
- [ ] Phase 8 — Retrieval
- [ ] Phase 9 — LLM Q&A
- [ ] Phase 10 — Streamlit interface
- [ ] Phase 11 — Testing, tuning, edge cases

## Setup

```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Usage

```bash
python3 main.py
```

Currently prints the number of chunks extracted from a given PDF for
inspection. Q&A interface comes in later phases.

## Notes

This repo is a learning log as much as a project — commits track progress
phase by phase rather than arriving as one finished dump.

Known gotchas hit so far:
- A corrupted virtual environment (`activate` script accidentally
  overwritten by a misused `script` command) — fixed by deleting and
  recreating the `venv` folder.
- One source PDF turned out to be structurally corrupted (bad xref table,
  failed decompression) — pypdf couldn't parse it; swapped in a clean PDF
  rather than fighting the broken file.