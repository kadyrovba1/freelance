from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'name', 'user_type', 'balance', 'password',)
        extra_kwargs = {'password': {'write_only': 'True'}}

    def create (self, validate_data):
        user = User(
            email = validate_data['email'],
            name = validate_data['name']
        )
        user.set_password(validate_data['password'])
        user.save()
        return user