# Chat with PDF — RAG Chatbot

Ask questions from any PDF using AI.

## How it works

1. PDF se text nikalta hai
2. Text ko chunks mein todta hai
3. Chunks ko embeddings mein convert karta hai
4. ChromaDB mein store karta hai
5. User ka sawaal search karta hai relevant chunks ke liye
6. Claude AI answer deta hai

## Tech Stack

- Anthropic Claude (claude-haiku)
- ChromaDB (vector database)
- SentenceTransformers (embeddings)
- pypdf (PDF parsing)

## Setup

pip install anthropic pypdf sentence-transformers chromadb python-dotenv

Add your API key in .env:
ANTHROPIC_API_KEY=your-key-here

## Run

python3 chat_pdf_final.py
