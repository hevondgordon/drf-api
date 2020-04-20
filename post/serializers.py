from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Post
from users.serializers import UserSerializer
from business.serializers import ServiceSerializer, BusinessSerializer
from business.models import Business, Service


class PostSerializer(serializers.ModelSerializer):
    """  """
    liked_by = UserSerializer(many=True, allow_null=True)
    created_by = BusinessSerializer()
    service = ServiceSerializer()
    is_liked = serializers.ReadOnlyField()

    class Meta:
        model = Post
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
        instance = Post.objects.create(
            caption=validated_data.get('caption'),
            like_count=0,
            is_liked=False,
            created_by=Business.objects.get(
                pk=validated_data.get('created_by').get('id')),
            service=Service.objects.get(
                pk=validated_data.get('service').get('id')),
            media_url=validated_data.get('media_url'),
            media_type=validated_data.get('media_type')
        )
        return instance
