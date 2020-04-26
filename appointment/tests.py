# pylint: disable=E1101

from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import Permission
from django.urls import reverse

from business.models import Service, Business
from api.tests import GenericTestCase
from .models import Appointment


class AppointmentTests(GenericTestCase):
    """
        Houses tests for appointment functionality
    """

    def setUp(self):
        super().setUp()
        add_appointment_permission = Permission.objects.get(
            codename="add_appointment")
        self.user.user_permissions.add(add_appointment_permission)
        self.service = Service.objects.create(name='test service')
        self.business = Business.objects.create(
            phone_number='876-000-0000',
            name='test business',
            address='test address',
            owner=self.user,
        )

    def test_create_appointment(self):
        """
            ensure that we can successfully create a new appointment
        """
        url = reverse('appointment-list')
        data = {
            'service_provider': 1,
            'service_type':  1,
            'time': '10:00',
            'date': '2020-03-10',
            'comment': 'hello'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(1, Appointment.objects.count())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
