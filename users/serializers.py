from .models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',
                  'username', 'phone_number', 'gender', ]

    def create(self, validated_data):
        instance = User.objects.create(
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            email=validated_data.get('email'),
            username=validated_data.get('email').split('@')[0],
            phone_number=validated_data.get('phone_number'),
            gender=validated_data.get('gender'),
            password=validated_data.get('password')
        )
        Token.objects.create(user=instance)
        return instance

