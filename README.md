# Remind-me-later API

A Django REST API for a reminder application that allows users to set up reminders with customizable messages and notification methods.

## Features

- Create reminders with a specified date, time, and message
- Choose notification method (SMS or Email)
- RESTful API for easy integration with frontend applications
- Extensible design for adding additional notification methods in the future

## Setup and Installation

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/KalyaniWaghchaure/remind-me-later.git
cd remind-me-later
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser (optional, for admin access):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/reminders/`

## API Endpoints

### Reminders

- `GET /api/reminders/` - List all reminders
- `POST /api/reminders/` - Create a new reminder
- `GET /api/reminders/{id}/` - Get a specific reminder
- `PUT /api/reminders/{id}/` - Update a reminder
- `DELETE /api/reminders/{id}/` - Delete a reminder

## API Request Example

### Create a Reminder

```http
POST /api/reminders/
Content-Type: application/json

{
  "message": "Don't forget to submit your assignment!",
  "date": "2025-05-15",
  "time": "14:30:00",
  "notification_method": "email",
  "email": "user@example.com"
}
```

### Response

```json
{
  "id": 1,
  "message": "Don't forget to submit your assignment!",
  "notification_method": "email",
  "email": "user@example.com",
  "phone_number": null,
  "is_sent": false
}
```

## Project Structure

```
remind_me_later/
├── manage.py
├── remind_me_later/          # Main project folder
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── reminders/                # Reminders app
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    ├── models.py
    ├── serializers.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

## Requirements

- Django
- Django REST Framework

These dependencies are listed in `requirements.txt`.

## Future Enhancements

- Add support for additional notification methods (Push notifications, Messaging apps)
- Implement user authentication and user-specific reminders
- Create a background task system to actually send the reminders
- Add recurring reminders support
