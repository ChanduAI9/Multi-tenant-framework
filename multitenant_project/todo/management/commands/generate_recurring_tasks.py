from django.core.management.base import BaseCommand
from django.utils import timezone
from todo.models import Todo
from datetime import timedelta

class Command(BaseCommand):
    help = 'Generates recurring tasks'

    def handle(self, *args, **kwargs):
        today = timezone.now().date()
        recurring_tasks = Todo.objects.filter(recurrence_interval__isnull=False)

        for task in recurring_tasks:
            next_due_date = today + timedelta(days=task.recurrence_interval)
            # Clone the task if completed
            if task.completed:
                task.pk = None  # Resets the ID for new task
                task.completed = False
                task.save()
                self.stdout.write(self.style.SUCCESS(f'Generated recurring task: {task.title}'))
