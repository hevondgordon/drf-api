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
        