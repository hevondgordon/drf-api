from api.tests import GenericTestCase
from rest_framework import status
from django.contrib.auth.models import Permission

from .models import User

from django.urls import reverse
# Create your tests here.
class UserTests(GenericTestCase):
    """
        Houses tests for user functionality
    """
    
    def setUp(self):
        super().setUp()
        add_post_permission = Permission.objects.get(codename="add_post")
        self.user.user_permissions.add(add_post_permission)

    # def test_create_user(self):
    #     """
    #         ensure that we can successfully create a new user
    #     """
    #     url = reverse('user-list')
    #     data = {
    #         'caption': 'caption',
    #         'created_by': 1,
    #         'service': 1,
    #         'media_url': 'https://www.test.com',
    #         'media_type': 'VIDEO'
    #     }
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(User.objects.count(), 1)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)