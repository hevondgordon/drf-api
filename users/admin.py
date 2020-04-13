from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(admin.ModelAdmin):
    fields = (
        'first_name', 'last_name', 'email', 'username',
        'phone_number', 'gender', 'is_superuser', 'password',
        'is_staff', 'is_active',
        'date_joined', 'groups', 'user_permissions',
    )


admin.site.register(User, UserAdmin)
