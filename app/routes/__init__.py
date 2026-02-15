from .auth import router as auth_router
from .categories import router as categories_router
from .posts import router as posts_router
from .users import router as users_router

__all__ = ["users_router", "posts_router", "categories_router", "auth_router"]
