from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task, ActivityLog
from django.contrib.auth.models import User

@receiver(post_save, sender=Task)
def create_activity_log(sender, instance, created, **kwargs):
    if created:
        owner = instance.project.owner or User.objects.get(username='admin')  # Replace 'admin' with a real username
        ActivityLog.objects.create(task=instance, user=owner, action='CREATE')