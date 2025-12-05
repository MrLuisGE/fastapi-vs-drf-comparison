# 🚀 FastAPI vs Django REST Framework — A Hands-On Comparison

> A practical, side-by-side comparison of two Python API frameworks through real, working code.

## � About This Project

This repository contains **two complete implementations** of the same Todo CRUD API:

- **`fastapi_project/`** — Built with FastAPI + SQLModel
- **`drf_project/`** — Built with Django REST Framework

Both projects implement identical functionality, allowing you to compare:
- Code structure and complexity
- Developer experience
- Performance characteristics
- Built-in features
- Async vs sync approaches

**Purpose:** This is a learning resource and technical comparison tool for developers choosing between FastAPI and Django REST Framework for their next project.

---

## 🎯 What's Implemented

Both projects expose a **Todo API** with full CRUD operations:

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/todos/` | Create a new todo |
| GET | `/todos/` | List all todos |
| GET | `/todos/{id}` | Get a specific todo |
| PUT | `/todos/{id}` | Update a todo |
| DELETE | `/todos/{id}` | Delete a todo |

**Todo Model:**
```json
{
  "id": 1,
  "title": "Buy milk",
  "description": "Remember to stop at the store",
  "completed": false
}
```

---

## 🏗️ Tech Stack

### FastAPI Project
- **FastAPI** 0.109.0 — Modern async web framework
- **SQLModel** 0.0.14 — SQL databases with Python type hints
- **Uvicorn** — ASGI server
- **SQLite** — Database

### DRF Project
- **Django** 4.2.9 — Full-featured web framework
- **Django REST Framework** 3.14.0 — Powerful REST toolkit
- **SQLite** — Database

---

## 🚀 Quick Start

### Option 1: Run FastAPI Project

```bash
# Navigate to FastAPI project
cd fastapi_project

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn app.main:app --reload
```

**Access the API:**
- 🌐 API Root: http://127.0.0.1:8000
- � Swagger Docs: http://127.0.0.1:8000/docs
- � ReDoc: http://127.0.0.1:8000/redoc

### Option 2: Run DRF Project

```bash
# Navigate to DRF project
cd drf_project

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# (Optional) Create superuser for admin panel
python manage.py createsuperuser

# Run the server
python manage.py runserver
```

**Access the API:**
- 🌐 API Root: http://127.0.0.1:8000/api/
- 🎨 Browsable API: http://127.0.0.1:8000/api/todos/
- � Admin Panel: http://127.0.0.1:8000/admin/

---

## 📊 Key Differences at a Glance

| Aspect | FastAPI | Django REST Framework |
|--------|---------|----------------------|
| **Architecture** | Async-first, lightweight | Sync-first, full-featured |
| **Performance** | Very fast (async) | Moderate (sync) |
| **Type Hints** | Native, everywhere | Limited |
| **Auto Docs** | OpenAPI/Swagger built-in | Browsable API |
| **ORM** | SQLModel (optional) | Django ORM (integrated) |
| **Admin Panel** | None | Full admin interface |
| **Auth** | Manual/3rd-party | Built-in |
| **Learning Curve** | Easy for modern Python | Requires Django knowledge |
| **Best For** | Microservices, async APIs | Full web apps, monoliths |

---

## 📁 Repository Structure

```
fastapi-vs-drf-comparison/
│
├── fastapi_project/              # FastAPI implementation
│   ├── app/
│   │   ├── main.py              # Application entry point
│   │   ├── models.py            # SQLModel database models
│   │   ├── schemas.py           # Pydantic request/response schemas
│   │   ├── routes.py            # API route handlers
│   │   └── database.py          # Database configuration
│   ├── requirements.txt         # Python dependencies
│   └── README.md               # FastAPI project documentation
│
└── drf_project/                  # Django REST Framework implementation
    ├── config/                   # Django project configuration
    │   ├── settings.py          # Django settings
    │   ├── urls.py              # URL routing
    │   ├── wsgi.py              # WSGI configuration
    │   └── asgi.py              # ASGI configuration
    ├── api/                      # Django app
    │   ├── models.py            # Django ORM models
    │   ├── serializers.py       # DRF serializers
    │   ├── views.py             # DRF ViewSets
    │   ├── admin.py             # Admin panel configuration
    │   └── tests.py             # Unit tests
    ├── manage.py                # Django management script
    ├── requirements.txt         # Python dependencies
    └── README.md               # DRF project documentation
```

---

## 🧪 Testing the APIs

### Example: Create a Todo

**FastAPI:**
```bash
curl -X POST "http://127.0.0.1:8000/todos/" \
  -H "Content-Type: application/json" \
  -d '{"title":"Buy milk","description":"Remember to stop at the store","completed":false}'
```

**DRF:**
```bash
curl -X POST "http://127.0.0.1:8000/api/todos/" \
  -H "Content-Type: application/json" \
  -d '{"title":"Buy milk","description":"Remember to stop at the store","completed":false}'
```

### Example: List All Todos

**FastAPI:**
```bash
curl "http://127.0.0.1:8000/todos/"
```

**DRF:**
```bash
curl "http://127.0.0.1:8000/api/todos/"
```

---

## 💡 Code Comparison Highlights

### Models

**FastAPI (SQLModel):**
```python
class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    completed: bool = False
```

**DRF (Django ORM):**
```python
class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
```

### Views/Endpoints

**FastAPI:**
```python
@router.get("/todos")
async def list_todos(session: Session = Depends(get_db)):
    return session.exec(select(Todo)).all()
```

**DRF:**
```python
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
```

---

## 🎓 Learning Resources

Each project folder contains its own detailed README with:
- Installation instructions
- API endpoint documentation
- Code structure explanation
- Framework-specific features

**Explore:**
- [`fastapi_project/README.md`](./fastapi_project/README.md) — FastAPI implementation details
- [`drf_project/README.md`](./drf_project/README.md) — DRF implementation details

---

## 🤝 Contributing

Contributions are welcome! If you find issues or have suggestions:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available for educational purposes.

---

## 🌟 Related Article

This repository accompanies a detailed technical article comparing FastAPI and Django REST Framework. Check it out for deeper insights into when to use each framework!

---

**Built with ❤️ for the Python developer community**