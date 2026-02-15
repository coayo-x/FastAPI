from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from models.post import Post
from schemas.post import PostCreate, PostUpdate


def create_post(db: Session, payload: PostCreate, owner_id: int) -> Post:
    post = Post(**payload.model_dump(), owner_id=owner_id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


def get_posts(db: Session) -> list[Post]:
    stmt = select(Post).options(joinedload(Post.owner), joinedload(Post.category)).order_by(Post.id)
    return list(db.scalars(stmt).unique().all())


def get_post_by_id(db: Session, post_id: int) -> Post | None:
    stmt = select(Post).options(joinedload(Post.owner), joinedload(Post.category)).where(Post.id == post_id)
    return db.scalar(stmt)


def update_post(db: Session, post: Post, payload: PostUpdate) -> Post:
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(post, field, value)

    db.commit()
    db.refresh(post)
    return post


def delete_post(db: Session, post: Post) -> None:
    db.delete(post)
    db.commit()
