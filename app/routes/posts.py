from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from crud.category import get_category_by_id
from crud.post import create_post, delete_post, get_post_by_id, get_posts, update_post
from db import get_db
from dependencies import get_current_user
from models.user import User
from schemas.post import PostCreate, PostRead, PostUpdate

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.post("", response_model=PostRead, status_code=status.HTTP_201_CREATED, summary="Create post (auth required)")
def create_post_endpoint(
    payload: PostCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> PostRead:
    category = get_category_by_id(db, payload.category_id)
    if not category:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Category does not exist")

    post = create_post(db, payload, current_user.id)
    return get_post_by_id(db, post.id)  # type: ignore[return-value]


@router.get("", response_model=list[PostRead], summary="List posts")
def list_posts(db: Session = Depends(get_db)) -> list[PostRead]:
    return get_posts(db)


@router.get("/{post_id}", response_model=PostRead, summary="Get post by ID")
def get_post_endpoint(post_id: int, db: Session = Depends(get_db)) -> PostRead:
    post = get_post_by_id(db, post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post


@router.patch("/{post_id}", response_model=PostRead, summary="Update post (auth required)")
def update_post_endpoint(
    post_id: int,
    payload: PostUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> PostRead:
    post = get_post_by_id(db, post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to edit this post")

    if payload.category_id is not None and not get_category_by_id(db, payload.category_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Category does not exist")

    updated = update_post(db, post, payload)
    return get_post_by_id(db, updated.id)  # type: ignore[return-value]


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete post (auth required)")
def delete_post_endpoint(
    post_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> None:
    post = get_post_by_id(db, post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to delete this post")
    delete_post(db, post)
