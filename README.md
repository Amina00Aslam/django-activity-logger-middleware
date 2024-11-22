# django-activity-logger-middleware
A Django-based logging and analytics system that tracks user activities using middleware and Django signals. It logs requests, task creation, and updates. Includes APIs to manage tasks and filter activity logs by user or date. Built with Django and Django Rest Framework for easy integration and scalability.
Here’s the complete guide for **Setting Up the Django Backend Assignment** (Enhanced Logging and Analytics System), with all the steps to follow:

## Features
- **User Activity Logging**: Logs user requests including IP, URL, HTTP method, and status code.
- **Event Tracking**: Uses Django signals to track events triggered by specific actions (e.g., task creation, updates).
- **Task Management**: Allows users to create, update, and delete tasks while tracking them in the database.
- **Analytics**: Keeps track of task statistics and activity logs.

## Project Files Overview
- **middleware.py**
Handles the logging of requests. This middleware captures the user's IP address, request method, URL, status code, and logs it into the RequestLog model.

- **signals.py**
Handles the logic for updating task summaries when tasks are created, updated, or deleted. It uses Django signals to automatically update the TaskSummary model.

- **models.py**
Contains the database models for RequestLog, UserActivityLog, Task, and TaskSummary. These models store logs of requests, task activities, and task statistics.

- **views.py**
Handles API logic for creating, updating, and deleting tasks as well as fetching activity logs.

- **tests.py**
Purpose: This file contains test cases for your application. It is designed to test the functionality of your models, views, signals, and middleware.
Structure:
The tests.py file is divided into different test classes. For example:
  - MiddlewareTest: Tests the middleware functionality, ensuring that requests are logged properly.
  - SignalTest: Tests that signals are fired correctly, e.g., ensuring that creating a task updates the TaskSummary.

# Part - 1: Getting Started
### 1. **Set Up the Development Environment**
To get started with this project, make sure you have the following prerequisites installed:
- **Python 3.8+**: Python must be installed on your machine.
- **Django 4.x**: We will use Django for building the web framework.
You can install Django using pip:
```bash
pip install django
```

- **Django REST Framework**: This will be used to create RESTful APIs for managing tasks and logs.
Install Django REST Framework (DRF) to handle API endpoints:
```bash
pip install djangorestframework
```

- **SQLite**: The database (default in Django).
  
### 2. **Install Required Packages**

#### 2.1 Install Django and Dependencies
Install all the dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```
#### 2.2 Clone the repository to your local machine:

```bash
git clone https://github.com/Amina00Aslam/django-activity-logger-middleware.git
cd django-activity-logger-middleware
```

### 3. **Set Up**
#### 3.1 Setup Django Project
In the cloned repository, run the following command to set up the Django project:
```bash
python myprojectt\manage.py migrate
```

#### 3.2 Start the Development Server
You can now run the Django development server:
```bash
python myprojectt\manage.py runserver
```

### 4. **Test the Application**
- Test the functionality of the signals and middleware using **Django TestCase** (for unit tests).
- Run the tests with:

```bash
python myprojectt\manage.py test user_activity
```


### 5. **Error Handling and Debugging**
Here are common issues I encountered and how you can resolve them:

Issue: django.db.utils.OperationalError: no such table: <table_name>

Solution: This typically occurs if migrations are not run. Run:

```bash
python myprojectt\manage.py migrate
```

Issue: ModuleNotFoundError: No module named 'myproject.settings'

Solution: Ensure that the DJANGO_SETTINGS_MODULE is correctly set in manage.py:

```bash
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
```

# Part - 2: Example API Request and Response Samples
Some example API requests with their HTTP methods, endpoints, and sample payloads (for POST, PUT requests) or URL parameters (for GET requests):

GET Request:

```bash
GET /api/activity-logs/?user_id=1&date=2024-11-22
```

Response:
```bash
[
  {
    "user": 1,
    "ip_address": "192.168.1.1",
    "url": "/api/activity-logs/",
    "method": "GET",
    "timestamp": "2024-11-22T15:30:00Z",
    "status_code": 200
  }
]
```

POST Request (Task Creation):
```bash
POST /api/task-management/
Content-Type: application/json
{
  "user": 1,
  "title": "New Task",
  "description": "Task details here"
}
```

Response:
```bash
{
  "message": "Task created successfully",
  "task_id": 1
}
```

### Conclusion
Follow the steps above to successfully set up the Django backend system. This includes creating models, views, middleware, and APIs for logging and analytics, with appropriate tests and configurations.
