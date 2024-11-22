from django.urls import path
from . import views

urlpatterns = [
    path('activity-logs/', views.ActivityLogsView.as_view(), name='activity-logs'),  # GET for activity logs
    path('task/', views.TaskManagementView.as_view(), name='create-task'),  # POST for creating a task
    path('task/<int:task_id>/', views.TaskManagementView.as_view(), name='update-delete-task'),  # PUT & DELETE for task
]

