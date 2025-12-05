"""
Django admin configuration for Todo model.
"""
from django.contrib import admin
from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    """
    Admin interface for Todo model.
    """
    list_display = ['id', 'title', 'completed']
    list_filter = ['completed']
    search_fields = ['title', 'description']
    list_editable = ['completed']
