# Simple API in Django for CRUD operations (TODO)

A simple REST API for managing a To-Do list, built using Django and Django REST Framework (DRF). This API supports basic CRUD operations: creating, reading, updating, and deleting tasks.

## Features

- **List all tasks**: View all tasks in the to-do list.
- **Create a task**: Add a new task with a title and completion status.
- **Retrieve a task**: Get details of a specific task.
- **Update a task**: Modify the title or completion status of a task.
- **Delete a task**: Remove a task from the list.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Django REST Framework

Install dependencies:
```bash
pip install django djangorestframework
```

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/AdnanRahmanpoor/todo_api_django.git
   cd todo_api_django
   ```

2. Run migrations:
   ```bash
   python manage.py migrate
   ```

3. Start the development server:
   ```bash
   python manage.py runserver
   ```

4. Access the API at `http://127.0.0.1:8000/api/tasks/`.

### Project Structure

```
todo_api_django/
├── todo_api/             # To-Do app with model, serializer, views, and urls
│   ├── models.py         # Task model
│   ├── serializers.py    # Task serializer
│   ├── views.py          # TaskViewSet for CRUD operations
│   └── urls.py           # URL routing for the API
└── todo_api_django/     # Main Django project
    ├── settings.py       # Project settings
    └── urls.py           # Includes the app's API URLs
```

## API Endpoints

| Method | Endpoint         | Description              |
|--------|-------------------|--------------------------|
| GET    | `/api/tasks/`     | List all tasks          |
| POST   | `/api/tasks/`     | Create a new task       |
| GET    | `/api/tasks/<id>/` | Retrieve a specific task |
| PUT    | `/api/tasks/<id>/` | Update a specific task   |
| DELETE | `/api/tasks/<id>/` | Delete a specific task   |

## License

This project is open-source and available under the MIT License.
