"""
API views for Todo CRUD operations.
"""
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Todo
from .serializers import TodoSerializer


@api_view(['GET'])
def api_root(request, format=None):
    """
    API root endpoint with links to available endpoints.
    """
    return Response({
        'message': 'Welcome to Django REST Framework Todo API',
        'endpoints': {
            'todos': reverse('todo-list', request=request, format=format),
            'admin': '/admin/',
        },
        'version': '1.0.0'
    })


class TodoViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Todo CRUD operations.
    
    Provides:
    - list: GET /api/todos/
    - create: POST /api/todos/
    - retrieve: GET /api/todos/{id}/
    - update: PUT /api/todos/{id}/
    - partial_update: PATCH /api/todos/{id}/
    - destroy: DELETE /api/todos/{id}/
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    def destroy(self, request, *args, **kwargs):
        """
        Delete a todo and return 204 No Content.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
