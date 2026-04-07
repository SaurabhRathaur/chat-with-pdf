import anthropic
import os
import chromadb
from dotenv import load_dotenv
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from rank_bm25 import BM25Okapi

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
model = SentenceTransformer('all-MiniLM-L6-v2')

# PDF padhna
reader = PdfReader("Claude.pdf")
full_text = ""
for page in reader.pages:
    full_text += page.extract_text()

# Chunking — 500 chars, 100 overlap
chunks = []
for i in range(0, len(full_text), 400):
    chunks.append(full_text[i:i+500])

# BM25 ke liye chunks tokenize karo
tokenized_chunks = [chunk.lower().split() for chunk in chunks]
bm25 = BM25Okapi(tokenized_chunks)

# ChromaDB mein store
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="pdf_chunks")
for i, chunk in enumerate(chunks):
    embedding = model.encode(chunk).tolist()
    collection.add(documents=[chunk], embeddings=[embedding], ids=[f"chunk_{i}"])

print(f"✅ {len(chunks)} chunks store ho gaye!")

def hybrid_search(query, n_results=2):
    # BM25 search
    tokenized_query = query.lower().split()
    bm25_scores = bm25.get_scores(tokenized_query)
    top_bm25_indices = sorted(range(len(bm25_scores)), key=lambda i: bm25_scores[i], reverse=True)[:n_results]
    bm25_chunks = [chunks[i] for i in top_bm25_indices]
    
    # Vector search
    query_embedding = model.encode(query).tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=n_results)
    vector_chunks = results['documents'][0]
    
    # Combine — duplicates hatao
    seen = set()
    combined = []
    for chunk in bm25_chunks + vector_chunks:
        if chunk not in seen:
            seen.add(chunk)
            combined.append(chunk)
    
    return combined

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
    context = "\n".join(relevant_chunks)

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{"role": "user", "content": f"Context:\n{context}\n\nSawaal: {query}"}]
    )

    print(f"\nAnswer:\n{response.content[0].text}")
    print("-" * 50)