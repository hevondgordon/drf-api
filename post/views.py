from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions

from .models import Post
from .serializers import PostSerializer
from users.models import User
from business.models import Service, Business
from business.serializers import ServiceSerializer, BusinessSerializer
# Create your views here.


class PostViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = {
            'caption': request.data.get('caption'),
            'like_count': 0,
            'is_liked': False,
            'created_by': BusinessSerializer(
                Business.objects.get(pk=request.data.get('created_by'))).data,
            'service': ServiceSerializer(
                Service.objects.get(pk=request.data.get('service'))).data,
            'liked_by': [],
            'media_url': request.data.get('media_url'),
            'media_type': request.data.get('media_type')
        }
        serializer = PostSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
