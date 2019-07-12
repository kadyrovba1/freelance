from django.urls import path
from .views import UserCreate

urlpatterns = [
    path('auth/', UserCreate.as_view(), name='create_user')
]