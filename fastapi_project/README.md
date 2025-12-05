# ⚡ FastAPI Todo API

A modern, async-first Todo API built with **FastAPI** featuring auto-generated documentation and minimal boilerplate.

## 🌟 Features

- ✅ **Async Python** - Built on Starlette for high performance
- ✅ **Auto-generated docs** - Swagger UI and ReDoc included
- ✅ **Type safety** - Pydantic models for validation
- ✅ **SQLModel** - Clean, typed database models
- ✅ **Minimal boilerplate** - Clean, modern code structure

## 📦 Installation

```bash
# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Running the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

## 📚 API Documentation

Once the server is running, visit:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## 🔌 API Endpoints

| Method | Endpoint          | Description            |
|--------|-------------------|------------------------|
| GET    | `/`               | API root & info        |
| GET    | `/health`         | Health check           |
| POST   | `/todos/`         | Create a new todo      |
| GET    | `/todos/`         | List all todos         |
| GET    | `/todos/{id}`     | Retrieve a todo        |
| PUT    | `/todos/{id}`     | Update a todo          |
| DELETE | `/todos/{id}`     | Delete a todo          |

## 📝 Example Usage

### Create a Todo
```bash
curl -X POST "http://127.0.0.1:8000/todos/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Buy milk",
    "description": "Remember to stop at the store",
    "completed": false
  }'
```

### Get All Todos
```bash
curl "http://127.0.0.1:8000/todos/"
```

### Update a Todo
```bash
curl -X PUT "http://127.0.0.1:8000/todos/1" \
  -H "Content-Type: application/json" \
  -d '{
    "completed": true
  }'
```

### Delete a Todo
```bash
curl -X DELETE "http://127.0.0.1:8000/todos/1"
```

## 🏗️ Project Structure

```
fastapi_project/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app & configuration
│   ├── database.py      # Database setup
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   └── routes.py        # API endpoints
├── requirements.txt
└── README.md
```

## 🔧 Tech Stack

- **FastAPI** - Modern web framework
- **Uvicorn** - ASGI server
- **SQLModel** - ORM with type hints
- **Pydantic** - Data validation (built into SQLModel)
- **SQLite** - Database (easily swappable)

## 🎯 Why FastAPI?

- **Fast**: Very high performance, on par with NodeJS and Go
- **Fast to code**: Increase development speed
- **Fewer bugs**: Reduce human errors with type hints
- **Intuitive**: Great editor support with autocomplete
- **Easy**: Designed to be easy to learn and use
- **Standards-based**: Based on OpenAPI and JSON Schema

## 📄 License

This project is part of a FastAPI vs Django REST Framework comparison repository.
