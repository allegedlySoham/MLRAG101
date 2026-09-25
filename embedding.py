from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2');

def embed(a):
    embeddedChunk = model.encode(a);
    return embeddedChunk;