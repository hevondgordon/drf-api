# pylint: disable=E1101

from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import Permission
from django.urls import reverse

from users.models import User

from .models import Appointment

from api.tests import GenericTestCase


class AppointmentTests(GenericTestCase):
    """
        Houses tests for appointment functionality
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        add_appointment_permission = Permission.objects.get(codename="add_appointment")
        cls.user.user_permissions.add(add_appointment_permission)

    def test_create_appointment(self):
        """
            ensure that we can successfully create a new appointment
        """
        url = reverse('appointment-list')
        data = {
            'client': 'hevongordon@gmail.com',
            'service_provider': 1,
            'service_type':  2,
            'time': '10:00',
            'date': '2020-03-10',
            'comment': 'hello'
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.post(url, data, format='json')
        self.assertEqual(1, Appointment.objects.count())
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
