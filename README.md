# YouTube Comment Response

This project provides an API for processing YouTube comments using OpenAI's language models and semantic search. It can classify comment intent and recommend relevant YouTube videos from a dataset.

## Features

- **Comment Intent Classification:** Distinguishes between "content request" and "general" comments.
- **Automated Responses:** Generates context-aware replies for each comment.
- **Video Recommendation:** Suggests the most relevant YouTube video for content requests using vector search.
- **Data Embedding:** Loads and embeds video metadata for efficient semantic search.

## Project Structure
. ├── app/ │ 
    ├── __init__.py │ 
    ├── api.py │ 
    ├── config.py │ 
    └── utils/ │ 
            ├── __init__.py │ 
            ├── llm_handler.py │ 
            └── vector_handler.py 
  ├── data/ │ 
        └── yt.json 
  ├── requirements.txt 
  ├── README.md 
  └── .gitignore



## Setup Instructions

### 1. Clone the Repository

```sh
git clone <repo-url>
cd youtube-comment-response

2. Install Dependencies
It's recommended to use a virtual environment:

python3 -m venv venv
source venv/bin/activate
pip install -r [requirements.txt]

3. Configure API Keys
Edit app/config.py and set your OpenAI API key: 
python OPENAI_API_KEY = "sk-your-key-here"

4. Prepare Data
Ensure data/yt.json contains your YouTube video metadata.

5. Load and Embed Data
Start the API server (see below), then call the /load_and_embed_data endpoint once to embed your video data:

curl -X POST http://127.0.0.1:8000/load_and_embed_data

6. Run the API Server

uvicorn app.api:app --reload

The API will be available at http://127.0.0.1:8000.

API Endpoints:
1. Health Check
    GET /health
2. Load and Embed Data
    POST /load_and_embed_data
3. Process Comment
    POST /process_comment
        Request Body:
        {
             "comment": "Your comment text here"
        }

        Response:
        {
            "response": "Intent: ...\nResponse: ..."
        }

Notes
1. The first call to /load_and_embed_data must be made before using /process_comment.
2. The project uses OpenAI's GPT and embedding models, so API usage may incur costs.


License
MIT License

