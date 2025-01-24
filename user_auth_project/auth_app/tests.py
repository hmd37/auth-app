from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class AuthTests(APITestCase):
    def test_user_registration(self):
        """Test user registration endpoint."""
        url = '/api/register/'
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword123'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_user_login(self):
        """Test user login endpoint."""
        # Create a user
        user = User.objects.create_user(username='testuser', password='testpassword123')

        url = '/api/login/'
        data = {
            'username': 'testuser',
            'password': 'testpassword123'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)


class GoogleLoginTests(APITestCase):
    def test_google_login(self):
        """Test Google login endpoint."""
        url = '/api/google-login/'
        # Simulate an authenticated user (mock session-based login)
        user = User.objects.create_user(username='googleuser', email='googleuser@example.com')
        self.client.force_login(user)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)


class UserProfileTests(APITestCase):
    def setUp(self):
        """Create a test user and authenticate."""
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword123')
        self.token = RefreshToken.for_user(self.user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_get_user_profile(self):
        """Test retrieving user profile."""
        url = '/api/profile/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser')
        self.assertEqual(response.data['email'], 'testuser@example.com')
