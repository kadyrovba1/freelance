from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import Client
from users.models import User

class UserTest(APITestCase):

    def SetUp(self):
        self.client = Client()
        self.client = User.objects.create(
            email='test@test.kg',
            username='testuser',
            user_type=1,
            balance=1000,
            password='default',
        )
        self.client.save()
        self.client.login(username='testuser', password='default')

    def test_create_user(self):
        url = reverse('create_user')
        data = {
                'email': 'test@test.kg',
                'username': 'testuser',
                'user_type': 1,
                'balance': 1000,
                'password': 'default',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.get().username, 'testuser')

    def test_login(self):
        url = reverse('login')
        data = {
            'username': 'testuser',
            'password': 'default',
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_list(self):
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)