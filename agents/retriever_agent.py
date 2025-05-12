from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import faiss
from sentence_transformers import SentenceTransformer
import numpy as np

app = FastAPI(title="Retriever Agent")

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# In-memory store (for demo); replace with persistent DB in production
corpus = []
index = None

class IndexRequest(BaseModel):
    documents: List[str]

class QueryRequest(BaseModel):
    query: str
    top_k: int = 3

@app.post("/index_documents")
def index_documents(request: IndexRequest):
    global index, corpus
    corpus = request.documents
    embeddings = model.encode(corpus, convert_to_numpy=True)
    
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    
    return {"status": "indexed", "num_documents": len(corpus)}

@app.post("/query")
def query_documents(request: QueryRequest):
    if index is None:
        return {"error": "No documents indexed yet"}
    
    query_embedding = model.encode([request.query], convert_to_numpy=True)
    distances, indices = index.search(query_embedding, request.top_k)
    
    results = [corpus[i] for i in indices[0]]
    return {"query": request.query, "top_k_results": results}
