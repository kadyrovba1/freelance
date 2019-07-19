from django.urls import path
from .views import UserCreate, LoginView, UserListView, UserDetailView

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('auth/', UserCreate.as_view(), name='create_user'),
    path('login/', LoginView.as_view(), name='login'),
    path('<int:pk>', UserDetailView.as_view(), name='detail')
]