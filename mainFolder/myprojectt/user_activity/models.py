from django.db import models
from django.contrib.auth.models import User


class RequestLog(models.Model):
    """
     Model to store logs for each HTTP request made by a user.

     Fields:
         user (ForeignKey): The user making the request. Can be null for anonymous requests.
         ip_address (GenericIPAddressField): The IP address of the client.
         url (URLField): The URL that was accessed.
         method (CharField): The HTTP method (GET, POST, etc.) used for the request.
         timestamp (DateTimeField): The timestamp of the request (automatically generated when created).
         status_code (IntegerField): The HTTP status code returned for the request (e.g., 200, 404).

     Methods:
         __str__() -> str: Returns a string representation of the request log.
     """
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    ip_address = models.GenericIPAddressField()
    url = models.URLField()
    method = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)
    status_code = models.IntegerField()

    def __str__(self):
        return f"Request by {self.user if self.user else 'Anonymous'} at {self.timestamp}"


class UserActivityLog(models.Model):
    """
    Logs user activities with the event type and timestamp.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.CharField(max_length=255)  # Ensure this field exists
    # activity = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String representation of the UserActivityLog model.
        Returns:
            str: A human-readable string for the UserActivityLog instance, showing the user, event, and timestamp.
        """

        return f"{self.user} {self.event} at {self.timestamp}"


class Task(models.Model):
    """
    Model to represent tasks that a user can create and manage.

    Fields:
        user (ForeignKey): The user who created the task.
        title (CharField): The title of the task.
        description (TextField): A detailed description of the task.
        created_at (DateTimeField): Timestamp of when the task was created (auto-generated).

    Methods:
        __str__() -> str: Returns a string representation of the task.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class TaskSummary(models.Model):
    """
    Model to store task summary data for each user.
    Fields:
        user (ForeignKey): The user to whom the summary belongs.
        total_tasks_created (IntegerField): The total number of tasks created by the user.
        tasks_today (IntegerField): The number of tasks created today by the user.
        date (DateField): The date for which the summary is created.

    Methods:
        __str__() -> str: Returns a string representation of the task summary.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_tasks_created = models.IntegerField(default=0)
    tasks_today = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Summary for {self.user} on {self.date}"

