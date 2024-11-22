from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task, RequestLog  # Import your RequestLog model
from .serializers import TaskSerializer, RequestLogSerializer  # Import serializer for RequestLog
from django.http import HttpResponse, HttpRequest


class ActivityLogsView(APIView):
    """
    API View to retrieve activity logs filtered by user or date.
    Methods:
        get(request): Handles GET requests to retrieve and filter logs.

    Query Parameters:
        - user_id (str): Optional. Filters logs by user ID.
        - date (str): Optional. Filters logs by date (format YYYY-MM-DD).

    Response:
        - 200 OK: Returns the serialized list of logs.
        - 400 Bad Request: If there is any validation error.
    """

    def get(self, request: HttpRequest) -> Response:

        # Optionally, filter by user or date
        user_id = request.GET.get('user_id', None)
        date = request.GET.get('date', None)

        # Retrieve all logs from the database
        logs = RequestLog.objects.all()

        # Apply filters if user_id or date is provided
        if user_id:
            logs = logs.filter(user_id=user_id)
        if date:
            logs = logs.filter(timestamp__date=date)

        # Serialize the filtered logs
        serializer = RequestLogSerializer(logs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TaskManagementView(APIView):
    """
    API View to manage tasks including creation, updating, and deletion.

    Methods:
        - post(request): Handles task creation.
        - put(request, task_id): Handles task updates based on task ID.
        - delete(request, task_id): Handles task deletion based on task ID.

    URL Parameters:
        - task_id (int): Required for PUT and DELETE requests. The ID of the task.

    Response:
        - 201 Created: Task successfully created.
        - 200 OK: Task successfully updated.
        - 204 No Content: Task successfully deleted.
        - 400 Bad Request: If there is any validation error.
    """

    def post(self, request: HttpRequest) -> Response:

        # Handle task creation
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            return Response({"message": "Task created successfully", "task_id": task.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request: HttpRequest, task_id: int):

        # Handle task update (assuming task_id is provided)
        task = Task.objects.get(id=task_id)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Task updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: HttpRequest, task_id: int) -> Response:

        # Handle task deletion based on task ID.
        task = Task.objects.get(id=task_id)
        task.delete()
        return Response({"message": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


def home_view(request: HttpRequest) -> HttpResponse:
    """
    Simple view to render a homepage. Returns a basic HTTP response with a welcome message.
    URL:
        / (root URL)
    Response:
        - 200 OK: Basic welcome message as plain text.
    """
    return HttpResponse("Welcome! You're at the homepage!")
