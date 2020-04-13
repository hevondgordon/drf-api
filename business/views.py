from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import Business, Service
from .serializers import BusinessSerializer, ServiceSerializer
from users.models import User
from users.serializers import UserSerializer


class BusinessViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows businesses to be viewed or edited.
    """
#     phone_number
# name
# address
# owner
# services
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)

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
