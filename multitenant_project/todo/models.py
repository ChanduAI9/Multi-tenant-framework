from django.db import models
from django.utils import timezone
# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    recurrence_interval = models.IntegerField(null=True, blank=True, help_text="Interval in days for recurring tasks")
    completion_time=models.DateTimeField(null=True,blank=True)

    def save(self, *args, **kwargs):
        if self.completed and self.completion_time is None:
            self.completion_time = timezone.now()
        elif not self.completed:
            self.completion_time = None 
        super(Todo, self).save(*args, **kwargs)


    def __str__(self):
        return self.title
    