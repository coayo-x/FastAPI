from pydantic import BaseModel, ConfigDict, Field

from schemas.category import CategoryRead
from schemas.user import UserRead


class PostBase(BaseModel):
    title: str = Field(min_length=3, max_length=120)
    content: str = Field(min_length=1)
    category_id: int


class PostCreate(PostBase):
    pass


class PostUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=3, max_length=120)
    content: str | None = Field(default=None, min_length=1)
    category_id: int | None = None


class PostRead(PostBase):
    id: int
    owner_id: int
    owner: UserRead
    category: CategoryRead

    model_config = ConfigDict(from_attributes=True)
