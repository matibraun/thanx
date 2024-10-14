from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from .models import User


class UserViewSetTest(APITestCase):
    
    def setUp(self):

        self.user_url = "http://127.0.0.1:8000/user/users/"  

        self.user_data = {
            "email": "testuser@example.com",
            "first_name": "Test",
            "last_name": "User",
            "document_type": "passport",
            "document_number": "A12345678",
            "country_code": "+1",
            "phone": "1234567890",
            "address": "123 Test Street",
            "nationality": "USA",
            "gender": "male",
            "civil_state": "single"
        }
        self.user = User.objects.create(**self.user_data)
    
    def test_list_users(self):

        response = self.client.get(self.user_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)
    
    def test_create_user(self):
        new_user_data = {
            "email": "newuser@example.com",
            "first_name": "New",
            "last_name": "User",
            "document_type": "passport",
            "document_number": "B98765432",
            "country_code": "+1",
            "phone": "9876543210",
            "address": "456 New Street",
            "nationality": "USA",
            "gender": "female",
            "civil_state": "married"
        }

        response = self.client.post(self.user_url, new_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], new_user_data['email'])
        self.assertEqual(response.data['first_name'], new_user_data['first_name'])
        self.assertEqual(response.data['last_name'], new_user_data['last_name'])
        self.assertEqual(response.data['document_type'], new_user_data['document_type'])
        self.assertEqual(response.data['document_number'], new_user_data['document_number'])
        self.assertEqual(response.data['phone'], new_user_data['phone'])
        self.assertEqual(response.data['country_code'], new_user_data['country_code'])
        self.assertEqual(response.data['address'], new_user_data['address'])
        self.assertEqual(response.data['nationality'], new_user_data['nationality'])
        self.assertEqual(response.data['gender'], new_user_data['gender'])
        self.assertEqual(response.data['civil_state'], new_user_data['civil_state'])
    
    def test_create_user_with_invalid_data(self):

        invalid_user_data = {
            "email": "invaliduser@example.com",
            "first_name": "Invalid",
            "last_name": "User",
            "document_type": "passport",
            # Missing document_number
            "country_code": "+1",
            "phone": "9876543210"
        }
        response = self.client.post(self.user_url, invalid_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_get_user_points_balance(self):

        points_balance_url = f"{self.user_url}{self.user.id}/points-balance/"
        response = self.client.get(points_balance_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("points_balance", response.data)
