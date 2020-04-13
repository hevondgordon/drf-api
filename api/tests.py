from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Permission

from users.models import User
from business.models import Business, Service


class GenericTestCase(APITestCase):
    """
        Generic test case setup
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create(
            email='hevongordon@gmail.com',
            phone_number='18764790489',
            gender='Male',
            password='P@ssw0rd123',
            first_name='Hevon',
            last_name='Gordon',
        )
        cls.service = Service.objects.create(name='test service')
        cls.business = Business.objects.create(
            phone_number='876-000-0000',
            name='test business',
            address='test address',
            owner=cls.user,
        )
        cls.business.services.add(cls.service)
        cls.token = Token.objects.get_or_create(user=cls.user)[0].key

