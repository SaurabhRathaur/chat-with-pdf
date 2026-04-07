import anthropic
import os
import chromadb
from dotenv import load_dotenv
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer, CrossEncoder
from rank_bm25 import BM25Okapi

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
model = SentenceTransformer('all-MiniLM-L6-v2')
reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

# PDF padhna
reader = PdfReader("Claude.pdf")
full_text = ""
for page in reader.pages:
    full_text += page.extract_text()

# Chunking
chunks = []
for i in range(0, len(full_text), 400):
    chunks.append(full_text[i:i+500])

# BM25 index
tokenized_chunks = [chunk.lower().split() for chunk in chunks]
bm25 = BM25Okapi(tokenized_chunks)

# ChromaDB
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="pdf_chunks")
for i, chunk in enumerate(chunks):
    embedding = model.encode(chunk).tolist()
    collection.add(documents=[chunk], embeddings=[embedding], ids=[f"chunk_{i}"])

print(f"✅ {len(chunks)} chunks store ho gaye!")

def hybrid_search(query, n_results=2):
    tokenized_query = query.lower().split()
    bm25_scores = bm25.get_scores(tokenized_query)
    top_bm25_indices = sorted(range(len(bm25_scores)), key=lambda i: bm25_scores[i], reverse=True)[:n_results]
    bm25_chunks = [chunks[i] for i in top_bm25_indices]

    query_embedding = model.encode(query).tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=n_results)
    vector_chunks = results['documents'][0]

    seen = set()
    combined = []
    for chunk in bm25_chunks + vector_chunks:
        if chunk not in seen:
            seen.add(chunk)
            combined.append(chunk)

    return combined

def rerank(query, chunks):
    pairs = [[query, chunk] for chunk in chunks]
    scores = reranker.predict(pairs)
    ranked = sorted(zip(scores, chunks), reverse=True)
    return [chunk for _, chunk in ranked]

# Chat loop
while True:
    query = input("\nSawaal (exit ke liye 'exit'): ")

    if query.lower() == "exit":
        print("Goodbye! 👋")
        break

    if not query.strip():
        print("Kuch toh pooch!")
        continue

    relevant_chunks = hybrid_search(query)
    relevant_chunks = rerank(query, relevant_chunks)
    context = "\n".join(relevant_chunks)

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{"role": "user", "content": f"Context:\n{context}\n\nSawaal: {query}"}]
    )

    print(f"\nAnswer:\n{response.content[0].text}")
    print("-" * 50)