from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import Business, Service
from .serializers import BusinessSerializer, ServiceSerializer
from users.models import User
from users.serializers import UserSerializer


class BusinessViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows businesses to be viewed or edited.
    """
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = {
            'phone_number': request.data.get('phone_number'),
            'name': request.data.get('name'),
            'address': request.data.get('address'),
            'owner': UserSerializer(User.objects.get(email=request.data.get('owner'))).data,
            'services': serialize_services(
                Service.objects.filter(pk__in=request.data.get('services'))
            ),
        }
        serializer = BusinessSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


def serialize_services(services):
    """
        serialize services based on pks received
    """
    service_ccontainer = []
    for service in services:
        _service = ServiceSerializer(service).data
        service_ccontainer.append(_service)
    return service_ccontainer


class ServiceViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows services to be viewed or edited.
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
