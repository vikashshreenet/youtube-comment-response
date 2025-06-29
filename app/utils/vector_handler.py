import chromadb
from openai import OpenAI
import pandas as pd
import app.config

client_model = OpenAI(api_key=app.config.OPENAI_API_KEY)
client_db = chromadb.PersistentClient(path=app.config.VECTOR_STORE_PATH)
collection = client_db.get_or_create_collection(app.config.CHROMA_COLLECTION_NAME)

def get_openai_embeddings(texts: list[str]) -> list[list[float]]:
    response = client_model.embeddings.create(
        model="text-embedding-3-small",
        input=texts
    )
    
    return [item.embedding for item in response.data]

def load_and_embed_data():
    df = pd.read_json(app.config.JSON_DATA_PATH)
    titles = df["title"].tolist()
    video_ids = df["videoId"].tolist()
    embeddings = get_openai_embeddings(titles)

    collection.add(
        ids=[str(i) for i in range(len(titles))],
        documents=titles,
        embeddings=embeddings,
        metadatas=[{"videoId": vid} for vid in video_ids]
    )

def search_video(query: str, threshold: float = 1) -> str:
    print(f"Record count: {collection.count()}")
    emb = get_openai_embeddings([query])[0]
    results = collection.query(query_embeddings=[emb], n_results=1)
    score = results['distances'][0][0]
    print(f"Title: {results['documents'][0][0]}")
    print(f"videoId: {results['metadatas'][0][0]['videoId']}")
    print(f"Score: {results['distances'][0][0]}")
    if score < threshold:
        return f"https://youtube.com/watch?v={results['metadatas'][0][0]['videoId']}"
    return ""
