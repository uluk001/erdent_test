from django.contrib import admin

# Register your models here.
from apps.medical_card.models import MedicalCards

admin.site.register(MedicalCards)