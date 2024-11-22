# django-activity-logger-middleware
A Django-based logging and analytics system that tracks user activities using middleware and Django signals. It logs requests, task creation, and updates. Includes APIs to manage tasks and filter activity logs by user or date. Built with Django and Django Rest Framework for easy integration and scalability.
Here’s the complete guide for **Setting Up the Django Backend Assignment** (Enhanced Logging and Analytics System), with all the steps to follow:

### 1. **Set Up the Development Environment**
To get started with this project, make sure you have the following prerequisites installed:
- **Python 3.8+**: Python must be installed on your machine.
- **Django 4.x**: We will use Django for building the web framework.
- **Django REST Framework**: This will be used to create RESTful APIs for managing tasks and logs.
- **SQLite**: The database (default in Django).
  
#### 1.1 Create a Virtual Environment (optional but recommended)
A virtual environment helps keep your project's dependencies isolated from others.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. **Install Required Packages**
After activating the virtual environment, install the required packages.

#### 2.1 Install Django and Dependencies
Create a `requirements.txt` file and list the dependencies inside it:

```text
Django==4.0.3
djangorestframework==3.13.1
```

Now, install all the dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 3. **Set Up Django Project**

#### 3.1 Create a Django Project
After installing the dependencies, you can create the Django project:

```bash
django-admin startproject myproject
```

#### 3.2 Create a Django App
Now, create a Django app for handling the user activities and tasks:

```bash
python myprojectt\manage.py startapp user_activity
```

#### 3.3 Add the App to `INSTALLED_APPS`
In `myproject/settings.py`, add your app to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    # other apps...
    'user_activity',
]
```

#### 3.4 Configure Middleware (for logging)
In `myproject/settings.py`, add the middleware to log user activities:

```python
MIDDLEWARE = [
    # other middleware...
    'user_activity.middleware.RequestLoggingMiddleware',
]
```

#### 3.5 Configure Rest Framework (optional, if using DRF)
In `settings.py`, add `'rest_framework'` to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # other apps...
    'rest_framework',
]
```

### 4. **Define Models and Migrations**

#### 4.1 Create Models
Define models in `user_activity/models.py`:

```python
from django.db import models
from django.contrib.auth.models import User

class RequestLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    ip_address = models.GenericIPAddressField()
    url = models.URLField()
    method = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)
    status_code = models.IntegerField()

    def __str__(self):
        return f"Request by {self.user if self.user else 'Anonymous'} at {self.timestamp}"

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

#### 4.2 Run Migrations
Create the necessary database tables for the models:

```bash
python myprojectt\manage.py makemigrations
python myprojectt\manage.py migrate
```

### 5. **Set Up Views, URLs, and Serializers**

#### 5.1 Create Serializers
In `user_activity/serializers.py`, create serializers to handle request and task data:

```python
from rest_framework import serializers
from .models import RequestLog, Task

class RequestLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestLog
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
```

#### 5.2 Create Views for API Endpoints
In `user_activity/views.py`, create views for the API endpoints:

```python
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task, RequestLog
from .serializers import TaskSerializer, RequestLogSerializer

class ActivityLogsView(APIView):
    def get(self, request):
        user_id = request.GET.get('user_id', None)
        date = request.GET.get('date', None)
        logs = RequestLog.objects.all()

        if user_id:
            logs = logs.filter(user_id=user_id)
        if date:
            logs = logs.filter(timestamp__date=date)

        serializer = RequestLogSerializer(logs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
```

#### 5.3 Create URLs
In `user_activity/urls.py`, add the URLs for your views:

```python
from django.urls import path
from .views import ActivityLogsView

urlpatterns = [
    path('activity_logs/', ActivityLogsView.as_view(), name='activity_logs'),
]
```

In the `myproject/urls.py`, include the app's URLs:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user_activity.urls')),
]
```

### 6. **Create Middleware for Request Logging**
In `user_activity/middleware.py`, create a middleware to log requests:

```python
import datetime
from .models import RequestLog

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        user = request.user if request.user.is_authenticated else None
        ip_address = request.META.get('REMOTE_ADDR')
        url = request.build_absolute_uri()
        method = request.method
        status_code = response.status_code
        timestamp = datetime.datetime.now()

        RequestLog.objects.create(
            user=user,
            ip_address=ip_address,
            url=url,
            method=method,
            timestamp=timestamp,
            status_code=status_code
        )

        return response
```

### 7. **Run the Server**
Start the development server:

```bash
python myprojectt\manage.py runserver
```

### 8. **Test the Application**
- Test the functionality of the API endpoints and middleware using **Django TestCase** (for unit tests).
- Run the tests with:

```bash
python myprojectt\manage.py test user_activity
```

### 9. **Final Setup**
- Once everything is set up and working, push your code to GitHub.
- If using virtual environments, make sure to add `venv/` (or equivalent) to `.gitignore` to avoid pushing unnecessary files.

### Conclusion
Follow the steps above to successfully set up the Django backend system. This includes creating models, views, middleware, and APIs for logging and analytics, with appropriate tests and configurations.
