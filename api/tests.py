from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Permission

from users.models import User


class GenericTestCase(APITestCase):
    """
        Generic test case setup
    """

    def setUp(self):
        super().setUp()
        self.user = User.objects.create(
            email='hevongordon@gmail.com',
            phone_number='18764790489',
            password='P@ssw0rd123',
            first_name='Hevon',
            last_name='Gordon',
        )
        self.token = Token.objects.get_or_create(user=self.user)[0].key
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
