from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions

from .models import Post
from .serializers import PostSerializer
from users.models import User
from business.models import Service, Business
from business.serializers import ServiceSerializer, BusinessSerializer

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
# Create your views here.


class PostViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        Post.set_user(request.user)
        instance = {}
        try:
            instance = Post.objects.get(pk=kwargs.get('pk'))
        except ObjectDoesNotExist:
            raise Http404
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        Post.set_user(request.user)
        queryset = self.filter_queryset(Post.objects.all())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = {
            'caption': request.data.get('caption'),
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
