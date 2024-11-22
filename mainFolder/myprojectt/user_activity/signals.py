from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.utils import timezone
from .models import UserActivityLog, Task, TaskSummary


# Signal for user login
@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    UserActivityLog.objects.create(user=user, event='login')


# Signal for user logout
@receiver(user_logged_out)
def user_logged_out_handler(sender, request, user, **kwargs):
    UserActivityLog.objects.create(user=user, event='logout')


# Signal for task creation
@receiver(post_save, sender=Task)
def task_created_handler(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        today = timezone.now().date()

        # Update TaskSummary for the user
        summary, _ = TaskSummary.objects.get_or_create(user=user)
        summary.total_tasks_created += 1

        # Update tasks_today if created today
        if instance.created_at.date() == today:
            summary.tasks_today += 1
        else:
            summary.tasks_today = 1  # Reset if a new day

        summary.save()
