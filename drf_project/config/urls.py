"""
URL configuration for DRF Todo project.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views

# Create a router and register our viewsets
router = routers.DefaultRouter()
router.register(r'todos', views.TodoViewSet, basename='todo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', views.api_root, name='api-root'),
]
