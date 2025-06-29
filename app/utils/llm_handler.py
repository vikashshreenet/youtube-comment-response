from openai import OpenAI
import app.config

client = OpenAI(api_key=app.config.OPENAI_API_KEY)

def classify_and_generate(comment: str) -> str:
    prompt = f"""
    You are a helpful assistant that processes user comments.

    User comment:
    "{comment}"

    Tasks:
    1. Classify the intent of the comment as either "content request" or "general".
    2. If the intent is "content request", reply:
    Intent: content request
    Response: Sure! Here's something you might like: <VIDEO_URL_PLACEHOLDER>
    3. If the intent is "general", reply:
    Intent: general
    Response: Thanks for your comment.

    Respond in this exact format.
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content