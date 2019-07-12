from django.urls import path
from .views import UserCreate, LoginView

urlpatterns = [
    path('auth/', UserCreate.as_view(), name='create_user'),
    path('login/', LoginView.as_view(), name='login')
]