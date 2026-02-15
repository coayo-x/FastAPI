
# FastAPI Project Rubric Implementation

This repository contains a complete FastAPI backend in `/app` that meets the rubric requirements:
- FastAPI + Swagger docs at `/docs`
- Required folder structure: `models/`, `schemas/`, `routes/`, `crud/`
- SQLite database with 4 tables (`users`, `posts`, `categories`, `token_blacklist`)
- Required relationships (`User 1-many Posts`, `Category 1-many Posts`)
- JWT login/logout authentication with password hashing
- 19 endpoints total (well above 10 minimum)

---

## Tech Stack
- Python 3.12+
- FastAPI
- SQLAlchemy ORM
- Pydantic
- SQLite
- bcrypt (direct usage for password hashing)
- JWT (`python-jose`)
- dotenv support for `SECRET_KEY`

---

## Setup (using uv)

### 1) Open terminal and go to backend folder
```bash
cd app
```

### 2) Create virtual environment

```bash
uv venv
```


### 3) Activate virtual environment

* **Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

* **Windows (cmd):**

```cmd
.venv\Scripts\activate.bat
```

* **macOS/Linux:**

```bash
source .venv/bin/activate
```

### 4) Install dependencies

```bash
uv pip install -r requirements.txt
```

### 5) (Optional) Configure secret key with .env

Create `app/.env` and add:

```env
SECRET_KEY=your-very-secret-key
```

If omitted, the app uses a safe default for school/demo use.

### 6) Run backend (recommended)

```bash
uvicorn main:app --reload
```

The server starts on:
`http://127.0.0.1:8000`

> Note: If you want to use `fastapi dev`, install:
>
> ```bash
> uv pip install "fastapi[standard]"
> ```

---

## Swagger / API Docs

* Open: `http://127.0.0.1:8000/docs`
* All endpoints can be tested directly in Swagger.

---

## Database Notes

* Database tables are auto-created at startup (`Base.metadata.create_all`).
* SQLite database file is: `app/app.db`.

---

## Authentication (How to Use Swagger Correctly)

This project uses OAuth2 Password Flow in Swagger.

### How to authorize in Swagger:

1. Create a user first using `POST /users`
2. Click **Authorize** (top right)
3. Enter your username + password
4. Click **Authorize** and close the popup

After that, protected endpoints will work.

Protected endpoints include:

* `GET /auth/me`
* `POST /auth/logout`
* `POST /posts`
* `PATCH /posts/{post_id}`
* `DELETE /posts/{post_id}`

---

## Endpoint List

### Health

* `GET /`

### Auth

* `POST /auth/login`
* `POST /auth/logout` (auth required)
* `GET /auth/me` (auth required)

### Users

* `POST /users`
* `GET /users`
* `GET /users/{user_id}`
* `PATCH /users/{user_id}`
* `DELETE /users/{user_id}`

### Posts

* `POST /posts` (auth required)
* `GET /posts`
* `GET /posts/{post_id}`
* `PATCH /posts/{post_id}` (auth required)
* `DELETE /posts/{post_id}` (auth required)

### Categories

* `POST /categories`
* `GET /categories`
* `GET /categories/{category_id}`
* `PATCH /categories/{category_id}`
* `DELETE /categories/{category_id}`

---

## Manual Rubric Test (Swagger) - Full Step-by-Step

Open Swagger:
`http://127.0.0.1:8000/docs`

### Step 1) Create a user (201 expected)

Endpoint:
`POST /users`

Example request body:

```json
{
  "username": "twin",
  "email": "twin@school.com",
  "password": "123456"
}
```

Expected result:

* `201 Created`
* Response includes user `id`

---

### Step 2) Login (200 expected)

Endpoint:
`POST /auth/login`

Enter:

* username: `twin`
* password: `123456`

Expected result:

* `200 OK`
* Response includes `access_token`

---

### Step 3) Authorize (Swagger)

Click **Authorize** (top right) and enter:

* username: `twin`
* password: `123456`

Expected result:

* You become authorized
* Protected endpoints now work

---

### Step 4) Verify protected endpoint works (200 expected)

Endpoint:
`GET /auth/me`

Expected result:

* `200 OK`
* Response includes current user info

---

### Step 5) Create a category (201 expected)

Endpoint:
`POST /categories`

Example request body:

```json
{
  "name": "School",
  "description": "test category"
}
```

Expected result:

* `201 Created`
* Response includes category `id` (example: `1`)

---

### Step 6) Create a post (201 expected, AUTH REQUIRED)

Endpoint:
`POST /posts`

Example request body:

```json
{
  "title": "First Post",
  "content": "rubric test post",
  "category_id": 1
}
```

Expected result:

* `201 Created`
* Response includes:

  * `owner_id`
  * `category_id`
* This confirms database relationships are working

---

### Step 7) Verify authorization enforcement (401 expected)

Click **Authorize** again and press **Logout** (Swagger logout only).

Now test these endpoints WITHOUT a token:

1. `POST /posts` → should return `401 Unauthorized`
2. `GET /auth/me` → should return `401 Unauthorized`

Expected result:

* Both return `401`

---

### Step 8) Verify real logout (blacklist) (401 expected after logout)

Authorize again (same username/password).

Now:

1. Confirm token works:

   * `GET /auth/me` should return `200`
2. Logout using API:

   * `POST /auth/logout`
3. After logout, token should be invalid:

   * `GET /auth/me` should return `401`
   * `POST /posts` should return `401`

Expected result:

* Token is blacklisted successfully.

---

## Common Issues

### 1) Swagger Authorize gives 422

Make sure you are using the Swagger **Authorize button** with username/password.
Do not send JSON manually for OAuth2.

### 2) Missing `email-validator`

This project uses `EmailStr` in Pydantic.
If you see:
`ImportError: email-validator is not installed`

Fix:

```bash
uv pip install -r requirements.txt
```

---

## Planning Document

See `PLANNING.md` for:

* ERD
* Endpoint list
* User stories / plan



---

## Rubric Proof (Quick Checklist)
- Swagger available at `/docs`
- Folder structure present: `models/`, `schemas/`, `routes/`, `crud/`
- Database tables: `users`, `posts`, `categories`, `token_blacklist`
- Relationships:
  - `User (1) -> (many) Posts`
  - `Category (1) -> (many) Posts`
- CRUD routers:
  - `/users` (full CRUD)
  - `/posts` (full CRUD)
  - `/categories` (full CRUD)
- Authentication:
  - `POST /auth/login`
  - `POST /auth/logout` (blacklists token)
  - `GET /auth/me` (protected)
- Endpoint count: 19 total (above minimum 10)
- Protected endpoints return `401` without authorization
```