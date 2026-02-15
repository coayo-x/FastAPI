[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/YTH7jNS-)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=22521531)
# FastAPI Project Rubric (100 Points)

## ✅ Minimum Requirements (Must Be Met)
- Project uses FastAPI
- Proper folder structure:
  - `models/`
  - `schemas/`
  - `routes/`
  - `crud/`
- At least **3 database tables**
- At least **2 CRUD routers**
- At least **1 relationship** between tables
- At least **10 working endpoints**
- Includes **login** and **logout**
- Swagger docs available at `/docs`
- All endpoints run without server errors

---

## 1. Planning & Design (15 pts)

| Criteria | Points |
|--------|--------|
| ERD with tables and relationships | 5 |
| Endpoint list with HTTP methods | 5 |
| Written plan or user stories | 5 |

**Full Credit (15):** ERD + endpoint list + clear written plan included in repo  
**Partial Credit:** Missing or incomplete planning documents

---

## 2. Project Structure (15 pts)

| Criteria | Points |
|--------|--------|
| Required folders present | 8 |
| Logical separation of concerns | 4 |
| Clean imports & organization | 3 |

**Expected Structure Example:**
app/
main.py
db.py
models/
schemas/
routes/
crud/
---

## 3. Database Models & Relationships (15 pts)

| Criteria | Points |
|--------|--------|
| At least 3 tables | 6 |
| At least 1 relationship (FK + relationship()) | 6 |
| Correct field types & constraints | 3 |

**Examples:**
- User → Jokes (one-to-many)
- Joke → Category (many-to-one or many-to-many)

---

## 4. Routers & Endpoints (20 pts)

| Criteria | Points |
|--------|--------|
| At least 10 total endpoints | 8 |
| At least 2 full CRUD routers | 8 |
| Correct HTTP methods & status codes | 4 |

**Examples of valid endpoints:**
- `POST /auth/login`
- `POST /auth/logout`
- `GET /jokes`
- `POST /jokes`
- `PATCH /jokes/{id}`

---

## 5. Authentication (Login / Logout) (10 pts)

| Criteria | Points |
|--------|--------|
| Login endpoint | 4 |
| Logout endpoint | 3 |
| Password hashing & auth protection | 3 |

JWT or session-based auth is acceptable.

---

## 6. Functionality (All Endpoints Work) (10 pts)

| Criteria | Points |
|--------|--------|
| No server crashes (500 errors) | 4 |
| Correct responses & status codes | 4 |
| Endpoints testable via Swagger | 2 |

---

## 7. Documentation (Swagger & README) (10 pts)

| Criteria | Points |
|--------|--------|
| `/docs` page works | 4 |
| Endpoints tagged & described | 3 |
| README with setup instructions | 3 |

---

## 8. Code Quality & Validation (5 pts)

| Criteria | Points |
|--------|--------|
| Pydantic schemas used properly | 2 |
| Validation & typing | 2 |
| Clean, readable code | 1 |

---

## ✅ Example Minimum Endpoint List (10)

### Auth
1. POST `/auth/login`
2. POST `/auth/logout`

### Users
3. POST `/users`
4. GET `/users/{id}`
5. PATCH `/users/{id}`
6. DELETE `/users/{id}`

### Jokes
7. GET `/jokes`
8. GET `/jokes/{id}`
9. POST `/jokes`
10. PATCH `/jokes/{id}`

---

## Extra Credit (+5 pts)
- +2: Automated tests (pytest)
- +2: Seed data
- +1: Dockerfile

---

## Submission Checklist
- [ ] Repo runs locally
- [ ] All requirements met
- [ ] Planning docs included
- [ ] Swagger docs working