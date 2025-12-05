"""
Tests for the Todo API.
"""
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Todo


class TodoAPITestCase(APITestCase):
    """
    Test cases for Todo API endpoints.
    """
    
    def setUp(self):
        """Set up test data."""
        self.todo_data = {
            'title': 'Test Todo',
            'description': 'Test Description',
            'completed': False
        }
        self.todo = Todo.objects.create(**self.todo_data)
    
    def test_create_todo(self):
        """Test creating a new todo."""
        response = self.client.post('/api/todos/', {
            'title': 'New Todo',
            'description': 'New Description',
            'completed': False
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Todo.objects.count(), 2)
    
    def test_list_todos(self):
        """Test listing all todos."""
        response = self.client.get('/api/todos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data['results']), 1)
    
    def test_retrieve_todo(self):
        """Test retrieving a specific todo."""
        response = self.client.get(f'/api/todos/{self.todo.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.todo_data['title'])
    
    def test_update_todo(self):
        """Test updating a todo."""
        response = self.client.put(f'/api/todos/{self.todo.id}/', {
            'title': 'Updated Todo',
            'description': 'Updated Description',
            'completed': True
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.title, 'Updated Todo')
        self.assertTrue(self.todo.completed)
    
    def test_delete_todo(self):
        """Test deleting a todo."""
        response = self.client.delete(f'/api/todos/{self.todo.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Todo.objects.count(), 0)
