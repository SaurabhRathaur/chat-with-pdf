from pypdf import PdfReader

reader = PdfReader("Claude.pdf")

'''print(f"Total pages: {len(reader.pages)}")

for i in range(0,len(reader.pages)):
   page = reader.pages[i] 
   text = page.extract_text() 
   print(text)'''

full_text = ""
for i in range(len(reader.pages)):
    page = reader.pages[i]
    full_text += page.extract_text()

print(len(full_text))

chunk_size = 500
chunks = []

for i in range(0, len(full_text), chunk_size):
    chunk = full_text[i:i+chunk_size]
    chunks.append(chunk)

print(f"Total chunks: {len(chunks)}")
print(f"Pehla chunk:\n{chunks[0]}")
print(f"\nDoosra chunk:\n{chunks[1]}")

from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

embedding = model.encode(chunks[0])

print(f"Embedding size: {len(embedding)}")
print(f"Pehle 5 numbers: {embedding[:5]}")

import chromadb

chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="pdf_chunks")

for i, chunk in enumerate(chunks):
    embedding = model.encode(chunk).tolist()
    collection.add(
        documents=[chunk],
        embeddings=[embedding],
        ids=[f"chunk_{i}"]
    )

print(f"Total chunks stored: {collection.count()}")

query = "What is a skill?"
query_embedding = model.encode(query).tolist()

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=2
)

print(results['documents'])

import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

context = results['documents'][0][0] + results['documents'][0][1]

response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": f"Context:\n{context}\n\nSawaal: What is a skill?"
    }]
)

print(response.content[0].text)

query = input(f"user: ")
query_embedding = model.encode(query).tolist()

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=2
)

while True:
    query = input("Sawaal (exit likh ke bahar niklo): ")

    if query.lower() == "exit":
        print("Goodbye bhai 👋")
        break

    # Query ka embedding
    query_embedding = model.encode(query).tolist()

    # ChromaDB se relevant chunks nikaalo
    results = collection.query(query_embeddings=[query_embedding], n_results=2)

    # Context banaao
    context = ""
    for chunk in results['documents'][0]:
        context += chunk + "\n"

    # Claude ko bhejne ke liye prompt
    messages = [
        {
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion:\n{query}"
        }
    ]

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=messages
    )

    # Answer print karo
    print("\nAnswer:")
    print(response.content[0].text)
    print("-" * 50)