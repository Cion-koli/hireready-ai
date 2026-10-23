from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status


class AccountsAuthTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_user_registration_and_login(self):
        # 1. Register
        reg_data = {
            "name": "Jane Candidate",
            "username": "janec",
            "email": "jane@example.com",
            "password": "Password123!",
            "password_confirm": "Password123!"
        }
        res = self.client.post('/api/auth/register/', reg_data, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertIn('tokens', res.data)
        self.assertIn('access', res.data['tokens'])
        self.assertEqual(res.data['user']['email'], 'jane@example.com')

        # 2. Login with email
        login_data = {
            "username": "jane@example.com",
            "password": "Password123!"
        }
        login_res = self.client.post('/api/auth/login/', login_data, format='json')
        self.assertEqual(login_res.status_code, status.HTTP_200_OK)
        self.assertIn('tokens', login_res.data)

        # 3. Access profile with token
        token = login_res.data['tokens']['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        profile_res = self.client.get('/api/auth/profile/')
        self.assertEqual(profile_res.status_code, status.HTTP_200_OK)
        self.assertEqual(profile_res.data['username'], 'janec')
