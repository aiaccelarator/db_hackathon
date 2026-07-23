import uuid

from fastapi import FastAPI
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from agent import article_writer
from models import ArticleRequest, ArticleResponse

from dotenv import load_dotenv

load_dotenv()


APP_NAME = "article-api"

app = FastAPI(title="Article API")

# Session service
session_service = InMemorySessionService()

# Runner
runner = Runner(
    app_name=APP_NAME,
    agent=article_writer,
    session_service=session_service,
)


@app.post("/article", response_model=ArticleResponse)
async def generate_article(request: ArticleRequest):

    user_id = "user1"
    session_id = str(uuid.uuid4())

    # Create session
    await session_service.create_session(
        app_name=APP_NAME,
        user_id=user_id,
        session_id=session_id,
    )

    message = types.Content(
        role="user",
        parts=[
            types.Part(text=request.topic)
        ],
    )

    article = ""

    async for event in runner.run_async(
        user_id=user_id,
        session_id=session_id,
        new_message=message,
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                article = "".join(
                    part.text
                    for part in event.content.parts
                    if part.text
                )

    return ArticleResponse(article=article)