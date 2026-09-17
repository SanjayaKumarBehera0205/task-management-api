# Task Management API

A production-style REST API built with FastAPI. Users can create an account, sign in with JWT authentication, and securely manage their own tasks.

## Features

- User registration and login
- JWT bearer authentication
- Secure Argon2 password hashing
- Create, read, update, and delete tasks
- Task ownership protection: users only access their own data
- Filter by status or priority
- Search task titles and descriptions
- Pagination
- Interactive Swagger documentation
- SQLite for easy local setup
- PostgreSQL and Docker Compose support
- Automated API tests

## Tech stack

- Python 3.12
- FastAPI
- SQLAlchemy 2.0
- Pydantic
- SQLite / PostgreSQL
- PyJWT and pwdlib
- Pytest
- Docker

## Project structure

```text
task-management-api/
├── app/
│   ├── api/routes/       # Authentication and task endpoints
│   ├── core/             # Settings and security
│   ├── db/               # Database setup
│   ├── models/           # SQLAlchemy models
│   ├── schemas/          # Pydantic schemas
│   └── main.py           # FastAPI application
├── tests/                # Automated tests
├── .env.example
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Run locally

### 1. Clone and enter the project

```bash
git clone https://github.com/YOUR-USERNAME/task-management-api.git
cd task-management-api
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `.env.example` to `.env`, then replace `SECRET_KEY` with a secure value.

Generate a secret with:

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### 5. Start the API

```bash
uvicorn app.main:app --reload
```

Open:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
- Health check: http://127.0.0.1:8000/health

## API endpoints

| Method | Endpoint | Description | Authentication |
|---|---|---|---|
| POST | `/api/v1/auth/register` | Create an account | No |
| POST | `/api/v1/auth/login` | Sign in and receive a token | No |
| GET | `/api/v1/auth/me` | Get the signed-in user | Yes |
| POST | `/api/v1/tasks` | Create a task | Yes |
| GET | `/api/v1/tasks` | List, search, filter, and paginate tasks | Yes |
| GET | `/api/v1/tasks/{task_id}` | Get one task | Yes |
| PATCH | `/api/v1/tasks/{task_id}` | Update a task | Yes |
| DELETE | `/api/v1/tasks/{task_id}` | Delete a task | Yes |

Login uses OAuth2 form data. Enter the email in the `username` field and the account password in the `password` field.

Example filter request:

```text
GET /api/v1/tasks?status=todo&priority=high&search=api&page=1&page_size=10
```

## Run tests

```bash
pytest
```

## Run with Docker and PostgreSQL

```bash
docker compose up --build
```

The API will be available at http://localhost:8000/docs.

> The credentials in `docker-compose.yml` are for local development only. Use secure secrets in production.

## Ideas for future improvements

- Refresh tokens and email verification
- Task categories and tags
- Team workspaces
- Alembic database migrations
- CI/CD with GitHub Actions
- Deployment to Render, Railway, or AWS

## License

This project is available under the MIT License.
