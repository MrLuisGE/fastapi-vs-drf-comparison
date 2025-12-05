# 🏛️ Django REST Framework Todo API

A feature-rich Todo API built with **Django REST Framework** featuring built-in admin panel, ORM, and extensive ecosystem.

## 🌟 Features

- ✅ **Django ORM** - Powerful database abstraction with migrations
- ✅ **Admin Panel** - Built-in admin interface for data management
- ✅ **Browsable API** - Interactive API browser included
- ✅ **ViewSets & Routers** - Clean, organized code structure
- ✅ **Batteries included** - Auth, permissions, pagination out-of-the-box
- ✅ **Extensive ecosystem** - Huge collection of Django packages

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

# Run migrations
python manage.py migrate

# Create superuser for admin panel (optional)
python manage.py createsuperuser
```

## 🚀 Running the Application

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000`

## 📚 API Documentation

Once the server is running, visit:

- **API Root**: http://127.0.0.1:8000/api/
- **Browsable API**: http://127.0.0.1:8000/api/todos/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## 🔌 API Endpoints

| Method | Endpoint              | Description            |
|--------|-----------------------|------------------------|
| GET    | `/`                   | API root & info        |
| GET    | `/api/todos/`         | List all todos         |
| POST   | `/api/todos/`         | Create a new todo      |
| GET    | `/api/todos/{id}/`    | Retrieve a todo        |
| PUT    | `/api/todos/{id}/`    | Update a todo (full)   |
| PATCH  | `/api/todos/{id}/`    | Update a todo (partial)|
| DELETE | `/api/todos/{id}/`    | Delete a todo          |

## 📝 Example Usage

### Create a Todo
```bash
curl -X POST "http://127.0.0.1:8000/api/todos/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Buy milk",
    "description": "Remember to stop at the store",
    "completed": false
  }'
```

### Get All Todos
```bash
curl "http://127.0.0.1:8000/api/todos/"
```

### Update a Todo (Partial)
```bash
curl -X PATCH "http://127.0.0.1:8000/api/todos/1/" \
  -H "Content-Type: application/json" \
  -d '{
    "completed": true
  }'
```

### Delete a Todo
```bash
curl -X DELETE "http://127.0.0.1:8000/api/todos/1/"
```

## 🏗️ Project Structure

```
drf_project/
├── config/
│   ├── __init__.py
│   ├── settings.py      # Django settings
│   ├── urls.py          # URL routing
│   ├── wsgi.py          # WSGI config
│   └── asgi.py          # ASGI config
├── api/
│   ├── __init__.py
│   ├── models.py        # Database models
│   ├── serializers.py   # DRF serializers
│   ├── views.py         # API views/viewsets
│   ├── admin.py         # Admin configuration
│   ├── apps.py          # App configuration
│   └── tests.py         # Unit tests
├── manage.py
├── requirements.txt
└── README.md
```

## 🔧 Tech Stack

- **Django** - Web framework
- **Django REST Framework** - REST API toolkit
- **SQLite** - Database (easily swappable to PostgreSQL, MySQL, etc.)
- **django-cors-headers** - CORS support

## 🧪 Running Tests

```bash
python manage.py test
```

## 🎯 Why Django REST Framework?

- **Mature & Stable**: Battle-tested in production for years
- **Feature-Rich**: Authentication, permissions, throttling, pagination built-in
- **Admin Panel**: Manage data without writing custom interfaces
- **ORM**: Powerful database abstraction with migrations
- **Ecosystem**: Thousands of reusable Django packages
- **Documentation**: Extensive documentation and community support
- **Scalable**: Powers some of the world's largest websites

## 🔐 Admin Panel

After creating a superuser, you can access the admin panel at:
http://127.0.0.1:8000/admin/

The admin panel allows you to:
- View, create, edit, and delete todos
- Filter and search todos
- Manage users and permissions
- View database statistics

## 📄 License

This project is part of a FastAPI vs Django REST Framework comparison repository.
