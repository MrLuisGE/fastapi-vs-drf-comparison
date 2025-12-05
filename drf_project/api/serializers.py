"""
DRF serializers for Todo model.
"""
from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    """
    Serializer for Todo model with validation.
    """
    
    class Meta:
        model = Todo
        fields = '__all__'
