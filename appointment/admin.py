from django.contrib import admin
from .models import Appointment

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    fields = (
        'client',
        'service_provider',
        'time',
        'date',
        'service_type',
        'comment',
    )

    list_display = fields

admin.site.register(Appointment, AppointmentAdmin)