from django.contrib import admin
from .models import RequestLog, UserActivityLog, Task, TaskSummary

# Register models for the Django admin interface
admin.site.register(RequestLog)
admin.site.register(UserActivityLog)
admin.site.register(Task)
admin.site.register(TaskSummary)

