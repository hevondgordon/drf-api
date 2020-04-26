from django.db import models
from business.models import Business, Service
from users.models import User


class Appointment(models.Model):
    """Appointment model"""
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    service_provider = models.ForeignKey(
        Business, related_name='appointments', on_delete=models.CASCADE)
    time = models.CharField(max_length=30)
    date = models.DateField()
    service_type = models.ForeignKey(Service, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100, null=True)

    def __str__(self):
        """Return appointment details"""
        return self.client.first_name + ' - ' +self.service_type.name
