from pydantic import BaseModel


class ArticleRequest(BaseModel):
    topic: str


class ArticleResponse(BaseModel):
    article: str