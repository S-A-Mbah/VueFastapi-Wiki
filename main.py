from typing import Optional, Dict
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create the Article class
class Article(BaseModel):
    name: str
    description: Optional[str] = None


articles = {
    'Story1': {'name': 'Story1', 'description': 'How I grew up in Nigeria'},
    'Story2': {'name': 'Story2', 'description': 'How I moved to Canada'}
}

# Create a Root endpoint
@app.get("/")
def read_root():
    return {"Hello": "My name is Somto, nice to meet you"}


@app.get("/articles/")
def get_articles():
    return articles


@app.put("/articles/{article_name}")
def store_article(article_name: str, article: Article , response_model=Article):
    if article_name not in articles:
        articles[article_name] = article
        raise HTTPException(status_code=201)
    else:
        articles[article_name] = article

    return {"article_name": article_name}



@app.get("/articles/{article_name}")
def read_article(article_name: str):
    if article_name not in articles:
        raise HTTPException(status_code=404, detail="Article Not Found")

    return {article_name: articles[article_name]}

if __name__ == '__main__':
    uvicorn.run(app)
