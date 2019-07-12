from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework import generics

# Create your views here.
class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer