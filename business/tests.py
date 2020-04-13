from rest_framework import status
from django.contrib.auth.models import Permission

from django.urls import reverse

from .models import Business, Service

from api.tests import GenericTestCase


class BusinessTests(GenericTestCase):
    """
        Houses tests for Business functionality
    """
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        add_business_permission = Permission.objects.get(codename="add_business")
        cls.user.user_permissions.add(add_business_permission)

    def test_create_business(self):
        """
            ensure that we can successfully create a new business
        """
        url = reverse('business-list')
        data = {
            'phone_number': '888-888-0000',
            'name': 'test api business name',
            'address': 'test api address',
            'owner':'hevongordon@gmail.com',
            'services': [1]
        }
        response = self.client.post(url, data, format='json')
        self.assertGreater(Business.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ServiceTests(GenericTestCase):
    """
        Houses tests for Service functionality
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        add_service_permission = Permission.objects.get(codename="add_service")
        cls.user.user_permissions.add(add_service_permission)

    def test_create_service(self):
        """
            ensure that we can successfully create a new service
        """
        url = reverse('service-list')
        data = {
            'name': 'test service'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(1, Service.objects.count())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
