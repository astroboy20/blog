
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your tests here.


class UserCreationTestCase(APITestCase):
    def test_user_success_creation(self):
        url = reverse('user_signup')
        data = {
            'username': 'midetest',
            'email': 'mide@test.com',
            'firstname': 'Mide',
            'lastname': 'Ola',
            "phone_number": '+2349098046727',
            'password': 'testing123',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'User Created Successfully')
        self.assertEqual(response.data['data']['username'], 'midetest')
        self.assertEqual(response.data['data']['firstname'], 'Mide')
        self.assertEqual(response.data['data']['lastname'], 'Ola')
        self.assertEqual(response.data['data']['email'], 'mide@test.com')
        self.assertEqual(User.objects.all().count(), 1)

    def test_user_fail_creation(self):
        url = reverse('user_signup')
        data = {
            'username': '',
            'email': '',
            'firstname': '',
            'lastname': '',
            "phone_number": '',
            'password': '',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
