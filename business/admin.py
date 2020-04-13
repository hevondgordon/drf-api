from django.contrib import admin
from .models import Business, Service


class ServiceAdmin(admin.ModelAdmin):
    fields = (
        'name',
    )
    list_display = fields


class BusinessAdmin(admin.ModelAdmin):
    fields = (
        'phone_number',
        'name',
        'address',
        'owner',
    )

    list_display = fields


admin.site.register(Business, BusinessAdmin)
admin.site.register(Service, ServiceAdmin)
