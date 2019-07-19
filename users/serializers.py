from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'user_type', 'balance', 'password',)
        extra_kwargs = {'password': {'write_only': 'True'}}

    def create(self, validate_data):
        user = User(
            email=validate_data['email'],
            username=validate_data['username'],
            user_type=validate_data['user_type'],
        )
        user.set_password(validate_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')

