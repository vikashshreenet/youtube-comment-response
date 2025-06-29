from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.utils.llm_handler import classify_and_generate
from app.utils.vector_handler import search_video, load_and_embed_data


app = FastAPI(title="YouTube Comment Response API", version="1.0")

class CommentRequest(BaseModel):
    comment: str

@app.get("/health")
def health_check():
    return {"status": "ok"}
  
@app.post("/load_and_embed_data")
def load_data_oai():
    try:
        load_and_embed_data()
        return JSONResponse(content={"message": "Data loaded and embedded successfully."})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/process_comment")
def process_comment(data: CommentRequest):
    try:
        response = classify_and_generate(data.comment)
        if "Intent: content request" in response:
            video_url = search_video(data.comment)
            response = response.replace("<VIDEO_URL_PLACEHOLDER>", video_url or "No relevant video found.")
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))