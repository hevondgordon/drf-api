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

premium_permissions = [
    'add_appointment',
    'change_appointment',
    'delete_appointment',
    'view_appointment',
    'view_group',
    'view_permission',
    'view_Token',
    'add_business',
    'change_business',
    'delete_business',
    'view_business',
    'view_service',
    'add_post',
    'change_post',
    'delete_post',
    'view_post',
    'view_session',
    'add_user',
    'view_user',
]

standard_permissions = [
    'add appointment',
    'change appointment',
    'delete appointment',
    'view appointment',
    'view group',
    'view permission',
    'view Token',
    'view business',
    'view service',
    'view post',
    'add user',
    'view user',
]