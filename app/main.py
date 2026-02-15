from fastapi import FastAPI

from db import Base, engine
from routes import auth_router, categories_router, posts_router, users_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Learning FastAPI - Rubric Project",
    description="Backend API with users, posts, categories, and JWT auth",
    version="1.0.0",
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(posts_router)
app.include_router(categories_router)


@app.get("/", tags=["Health"], summary="Health check")
def root() -> dict[str, str]:
    return {"message": "FastAPI project is running"}
