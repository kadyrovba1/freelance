from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, LoginSerializer


# Create your views here.
class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

class LoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = ()

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            return Response({'token': user.auth_token.key})
        else:
            return Response({'error: "Wrong Credentials'}, status=status.HTTP_400_BAD_REQUEST)