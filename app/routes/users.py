from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from crud.user import create_user, delete_user, get_user_by_id, get_users, update_user
from db import get_db
from schemas.user import UserCreate, UserRead, UserUpdate

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("", response_model=UserRead, status_code=status.HTTP_201_CREATED, summary="Create a user")
def create_user_endpoint(payload: UserCreate, db: Session = Depends(get_db)) -> UserRead:
    return create_user(db, payload)


@router.get("", response_model=list[UserRead], summary="List all users")
def list_users(db: Session = Depends(get_db)) -> list[UserRead]:
    return get_users(db)


@router.get("/{user_id}", response_model=UserRead, summary="Get user by ID")
def get_user_endpoint(user_id: int, db: Session = Depends(get_db)) -> UserRead:
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.patch("/{user_id}", response_model=UserRead, summary="Update user by ID")
def update_user_endpoint(user_id: int, payload: UserUpdate, db: Session = Depends(get_db)) -> UserRead:
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return update_user(db, user, payload)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete user by ID")
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)) -> None:
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    delete_user(db, user)
