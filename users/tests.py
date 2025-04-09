from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class AuthTests(APITestCase):
    def test_user_registration(self):
        url = reverse('register')
        data = {
            'email': 'test@example.com',
            'username': 'testuser',
            'password': 'testpass123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('email' in response.data)

    def test_user_login(self):
        User.objects.create_user(
            email='test@example.com',
            username='testuser',
            password='testpass123'
        )

        url = reverse('login')
        data = {
            'email': 'test@example.com',
            'password': 'testpass123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)

    def test_invalid_login(self):
        url = reverse('login')
        data = {
            'email': 'wrong@example.com',
            'password': 'wrongpass'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)