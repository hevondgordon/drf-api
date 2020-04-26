from django.db import models
from users.models import User


class Service(models.Model):
    """ this model defines the services that are available to be 
    provided by businesses """
    name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        """Return name of business"""
        return self.name


class Business(models.Model):
    """ this model is used to define the structure of a business """
    phone_number = models.CharField(max_length=12)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    owner = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='business')
    services = models.ManyToManyField(Service, related_name='businesses')
    setup_complete = models.BooleanField(default=False)

    def __str__(self):
        """Return name of business"""
        return self.name
