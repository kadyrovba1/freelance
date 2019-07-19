from django.shortcuts import render
from django.contrib.auth import authenticate, login, get_user_model
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import *

# Create your views here.
User = get_user_model()

class UserCreate(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer



class LoginView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = authenticate(request, **serializer.validated_data)
            if user:
                login(request, user)
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)



class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

