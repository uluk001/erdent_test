from django.contrib import admin

# Register your models here.
from apps.user.models import  User,Branch,Schedule

admin.site.register(User)
admin.site.register(Branch)
admin.site.register(Schedule)