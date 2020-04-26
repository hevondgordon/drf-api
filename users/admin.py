from django.contrib import admin

from .models import User

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class CustomUserAdmin(BaseUserAdmin):
    """ customer user admin that adds gender and phone number fields  """
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('gender', 'phone_number',)}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {'fields': ('gender', 'phone_number',)}),
    )

admin.site.register(User, CustomUserAdmin)
