from flask import Flask, request, render_template
import anthropic, os, chromadb
from dotenv import load_dotenv
from pypdf import PdfReader

load_dotenv()

anthropic_client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
chroma_client = chromadb.Client()
collection = None
model = None

app = Flask(__name__)

def get_model():
    global model
    if model is None:
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer('all-MiniLM-L6-v2')
    return model

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    global collection
    pdf = request.files["pdf"]
    reader = PdfReader(pdf)

    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text()

    chunks = []
    for i in range(0, len(full_text), 400):
        chunks.append(full_text[i:i+500])

    m = get_model()
    collection = chroma_client.get_or_create_collection(name="pdf_chunks")
    for i, chunk in enumerate(chunks):
        embedding = m.encode(chunk).tolist()
        collection.add(documents=[chunk], embeddings=[embedding], ids=[f"chunk_{i}"])

    return render_template("index.html", message=f"PDF upload ho gayi! {len(chunks)} chunks ready.")

@app.route("/ask", methods=["POST"])
def ask():
    global collection
    if not collection:
        return render_template("index.html", answer="Pehle PDF upload karo!")

    question = request.form["question"]
    m = get_model()
    query_embedding = m.encode(question).tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=2)

    context = "".join(results['documents'][0])
    response = anthropic_client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{"role": "user", "content": f"Context:\n{context}\n\nSawaal: {question}"}]
    )

    return render_template("index.html", answer=response.content[0].text)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)