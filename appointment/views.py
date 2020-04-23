from rest_framework import viewsets
from rest_framework import permissions
from appointment.models import Appointment
from .serializers import AppointmentSerializer
from rest_framework import status
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer
from business.models import Service, Business
from business.serializers import BusinessSerializer, ServiceSerializer


class AppointmentViewset(viewsets.ModelViewSet):
    """
    This viewset is used to present the appointment model
    to the user
    """

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        service_provider = Business.objects.get(
            pk=request.data.get('service_provider'))
        service_type = Service.objects.get(pk=request.data.get('service_type'))
        appointment_data = {
            'client': UserSerializer(request.user).data,
            'service_provider': BusinessSerializer(service_provider).data,
            'time': request.data.get('time'),
            'date': request.data.get('date'),
            'service_type': ServiceSerializer(service_type).data,
            'comment': request.data.get('comment'),
        }
        serializer = AppointmentSerializer(data=appointment_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()
