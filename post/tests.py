from rest_framework import status
from django.contrib.auth.models import Permission
from django.urls import reverse

from api.tests import GenericTestCase
from business.models import Service, Business

from .models import Post

# Create your tests here.
class PostTests(GenericTestCase):
    """
        Houses tests for Post functionality
    """

    def setUp(self):
        super().setUp()
        add_post_permission = Permission.objects.get(codename="add_post")
        self.user.user_permissions.add(add_post_permission)
        self.service = Service.objects.create(name='test service')
        self.business = Business.objects.create(
            phone_number='876-000-0000',
            name='test business',
            address='test address',
            owner=self.user,
        )

    def test_create_post(self):
        """
            ensure that we can successfully create a new post
        """
        url = reverse('post-list')
        data = {
            'caption': 'caption dis nuh',
            'created_by': 1,
            'service': 1,
            'media_url': 'https://www.stuffit.com',
            'media_type': 'VIDEO'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)