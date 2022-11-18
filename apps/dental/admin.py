from django.contrib import admin

from apps.dental.models import DentalServicesCategory, DentalServicesList

admin.site.register(DentalServicesCategory)
admin.site.register(DentalServicesList)
