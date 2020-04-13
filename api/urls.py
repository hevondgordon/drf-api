"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from users.views import UserViewSet
from post.views import PostViewset
from business.views import BusinessViewset, ServiceViewset
from appointment.views import AppointmentViewset
from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewset)
router.register(r'business', BusinessViewset)
router.register(r'appointments', AppointmentViewset)
router.register(r'services', ServiceViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
