from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(Contact)
admin.site.register(User)
admin.site.register(Doctor_Profile)
admin.site.register(Appointment)
admin.site.register(CencelAppointment)
admin.site.register(HealthProfile)