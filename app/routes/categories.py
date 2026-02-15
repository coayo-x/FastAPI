from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from crud.category import create_category, delete_category, get_categories, get_category_by_id, update_category
from db import get_db
from schemas.category import CategoryCreate, CategoryRead, CategoryUpdate

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post("", response_model=CategoryRead, status_code=status.HTTP_201_CREATED, summary="Create category")
def create_category_endpoint(payload: CategoryCreate, db: Session = Depends(get_db)) -> CategoryRead:
    return create_category(db, payload)


@router.get("", response_model=list[CategoryRead], summary="List categories")
def list_categories(db: Session = Depends(get_db)) -> list[CategoryRead]:
    return get_categories(db)


@router.get("/{category_id}", response_model=CategoryRead, summary="Get category by ID")
def get_category_endpoint(category_id: int, db: Session = Depends(get_db)) -> CategoryRead:
    category = get_category_by_id(db, category_id)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return category


@router.patch("/{category_id}", response_model=CategoryRead, summary="Update category by ID")
def update_category_endpoint(category_id: int, payload: CategoryUpdate, db: Session = Depends(get_db)) -> CategoryRead:
    category = get_category_by_id(db, category_id)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return update_category(db, category, payload)


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete category by ID")
def delete_category_endpoint(category_id: int, db: Session = Depends(get_db)) -> None:
    category = get_category_by_id(db, category_id)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    delete_category(db, category)
