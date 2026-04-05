import anthropic          # Anthropic SDK library load karo
import os                 # Environment variables padhne ke liye
from dotenv import load_dotenv          # .env file padhne ke liye
from pypdf import PdfReader             # PDF padhne ke liye
from sentence_transformers import SentenceTransformer  # Text ko numbers mein convert karne ke liye
import chromadb           # Vector database

load_dotenv()             # .env file se API key lo
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))  # Claude ka middleman banao
model = SentenceTransformer('all-MiniLM-L6-v2')  # Embedding model load karo

reader = PdfReader("Claude.pdf")   # PDF kholo
full_text = ""                     # Khali string shuru karo
for i in range(len(reader.pages)): # Har page pe loop
    full_text += reader.pages[i].extract_text()  # Page ka text add karo

chunks = []                        # Khali list
for i in range(0, len(full_text), 400):          # Har 400 character pe
    chunks.append(full_text[i:i+500])            # 500 char ka chunk list mein daalo

chroma_client = chromadb.Client()               # ChromaDB start karo
collection = chroma_client.create_collection(name="pdf_chunks")  # Folder banao
for i, chunk in enumerate(chunks):             # Har chunk pe loop
    embedding = model.encode(chunk).tolist()   # Chunk ko numbers mein convert karo
    collection.add(documents=[chunk], embeddings=[embedding], ids=[f"chunk_{i}"])  # Store karo

while True:                        # Hamesha chalta rahe
    query = input("Sawaal: ")      # User se sawaal lo
    if query.lower() == "exit":    # Agar "exit" likha
        break                      # Loop band karo

    query_embedding = model.encode(query).tolist()  # Sawaal ko numbers mein convert karo
    results = collection.query(query_embeddings=[query_embedding], n_results=2)  # Similar chunks dhundho

    context = ""                   # Khali context
    for chunk in results['documents'][0]:   # Mile hue chunks pe loop
        context += chunk + "\n"    # Context mein add karo

    response = client.messages.create(     # Claude ko bhejo
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{"role": "user", "content": f"Context:\n{context}\n\nSawaal: {query}"}]
    )

    print(response.content[0].text)  # Answer print karo