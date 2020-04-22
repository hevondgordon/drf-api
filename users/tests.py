from api.tests import GenericTestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Permission

from .models import User
from business.models import Business, Service

from django.urls import reverse
# Create your tests here.


class UserTests(GenericTestCase):
    """
        Houses tests for user functionality
    """

    def setUp(self):
        super().setUp()
        add_post_permission = Permission.objects.get(codename="add_user")
        self.service = Service.objects.create(name='test service')
        self.user.user_permissions.add(add_post_permission)

    def test_create_user(self):
        """
            ensure that we can successfully create a new user
        """
        url = reverse('user-list')
        data = {
            'first_name': 'test',
            'last_name': 'user',
            'email': 'testuser@test.com',
            'username': 'testuser',
            'phone_number': '876-000-0000',
            'gender': 'Male',
            'password': 'P@ssw0rd123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_business_as_new_user(self):
        """ Ensure that as a new user I am able to create a business """

        url = reverse('user-list')
        data = {
            'first_name': 'test',
            'last_name': 'user',
            'email': 'testuser@test.com',
            'username': 'testuser',
            'phone_number': '876-000-0000',
            'gender': 'Male',
            'password': 'P@ssw0rd123'
        }
        self.client.post(url, data, format='json')
        token = Token.objects.get(
            user=User.objects.get(email='testuser@test.com'))
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        business_url = reverse('business-list')
        business_data = {
            'phone_number': '876-000-0000',
            'name': 'business name',
            'address': 'address',
            'owner':'testuser@test.com',
            'services': [1]
        }
        response = self.client.post(business_url, business_data, format='json')
        self.assertEqual(Business.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
