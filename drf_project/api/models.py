"""
Django models for the Todo application.
"""
from django.db import models


class Todo(models.Model):
    """
    Todo model representing a task item.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
