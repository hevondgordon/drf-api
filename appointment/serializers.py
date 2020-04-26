from django.http import HttpResponseForbidden

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.utils import model_meta

from users.serializers import UserSerializer
from users.models import User

from business.models import Business, Service
from business.serializers import BusinessSerializer, ServiceSerializer
from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    """
        Serializes appointment model
    """
    client = UserSerializer(read_only=True)
    service_provider = BusinessSerializer(read_only=True)
    service_type = ServiceSerializer()

    class Meta:
        model = Appointment
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        assert hasattr(self, 'initial_data'), (
            'Cannot call `.is_valid()` as no `data=` keyword argument was '
            'passed when instantiating the serializer instance.'
        )

        if not hasattr(self, '_validated_data'):
            try:
                self._validated_data = self.initial_data
            except ValidationError as exc:
                self._validated_data = {}
                self._errors = exc.detail
            else:
                self._errors = {}

        if self._errors and raise_exception:
            raise ValidationError(self.errors)

        return not bool(self._errors)

    def create(self, validated_data):
        _client = validated_data.get('client')
        client = User.objects.get(email=_client.get('email'))

        service_provider_id = validated_data.get('service_provider').get('id')
        service_provider = Business.objects.get(pk=service_provider_id)

        service_type_id = validated_data.get('service_type').get('id')
        service_type = Service.objects.get(pk=service_type_id)

        time = validated_data.get('time')
        date = validated_data.get('date')
        comment = validated_data.get('comment')

        instance = Appointment.objects.create(
            client=client,
            service_provider=service_provider,
            service_type=service_type,
            time=time,
            date=date,
            comment=comment
        )

        return instance
    
    def update(self, instance, validated_data):
        info = model_meta.get_field_info(instance)

        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                continue
            else:
                if attr == 'service_type':
                    self.validate_service(instance, value)
                    service_type = Service.objects.get(
                        name=validated_data.get('service_type').get('name'))
                    setattr(instance, attr, service_type)
                else:
                    setattr(instance, attr, value)

        instance.save()

        return instance

    def validate_service(self, instance, service):
        """ validates that the service that is being requested is
        acually provided by the business that it is being requested from """
        _service = Service.objects.get(name=service.get('name'))
        if _service not in instance.service_provider.services.all():
            raise Exception('AppointmentException', 'provided service is not offered by business')


