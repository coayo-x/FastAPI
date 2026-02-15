# Planning Document

## 1) ERD (Markdown)

| Table | Key Fields | Relationships |
|---|---|---|
| `users` | `id (PK)`, `username (unique)`, `email (unique)`, `hashed_password` | One user has many posts |
| `categories` | `id (PK)`, `name (unique)`, `description` | One category has many posts |
| `posts` | `id (PK)`, `title`, `content`, `owner_id (FK->users.id)`, `category_id (FK->categories.id)` | Each post belongs to one user and one category |
| `token_blacklist` | `id (PK)`, `token (unique)` | Stores invalidated JWTs on logout |

### Relationship Summary
- `users (1) -> (many) posts`
- `categories (1) -> (many) posts`

## 2) Endpoint List

### Auth
- `POST /auth/login`
- `POST /auth/logout`
- `GET /auth/me`

### Users
- `POST /users`
- `GET /users`
- `GET /users/{user_id}`
- `PATCH /users/{user_id}`
- `DELETE /users/{user_id}`

### Posts
- `POST /posts`
- `GET /posts`
- `GET /posts/{post_id}`
- `PATCH /posts/{post_id}`
- `DELETE /posts/{post_id}`

### Categories
- `POST /categories`
- `GET /categories`
- `GET /categories/{category_id}`
- `PATCH /categories/{category_id}`
- `DELETE /categories/{category_id}`

### Health
- `GET /`

## 3) Written Plan / User Stories

### Plan
1. Build SQLAlchemy models for users, posts, categories, and token blacklist.
2. Define Pydantic request/response schemas for validation and clean API docs.
3. Add CRUD layer for each entity and authentication utility functions.
4. Implement routers for users, posts, categories, and auth using FastAPI dependencies.
5. Secure selected endpoints with JWT auth and verify logout invalidates token.
6. Wire app in `main.py`, auto-create tables, and expose Swagger docs.
7. Document setup and manual testing flow in README.

### User Stories
- As a new user, I can register an account.
- As a user, I can log in and receive a JWT.
- As an authenticated user, I can create, edit, and delete my own posts.
- As any client, I can list users, categories, and posts.
- As a user, I can log out so my token can no longer be used.
