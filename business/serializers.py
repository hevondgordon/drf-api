from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Business, Service
from users.serializers import UserSerializer
from users.models import User

import json


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class BusinessSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True)
    owner = UserSerializer()

    class Meta:
        model = Business
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
        instance = Business.objects.create(
            phone_number=validated_data.get('phone_number'),
            name=validated_data.get('name'),
            address=validated_data.get('address'),
            owner=User.objects.get(email=validated_data.get('owner').get('email')),
            # services=Service.objects.filter(pk__in=validated_data.get('services'))
        )
        for service in validated_data.get('services'):
            _service = Service.objects.get(pk=service.get('id'))
            instance.services.add(_service)
        return instance
