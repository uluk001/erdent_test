import datetime
from rest_framework import generics
from rest_framework.response import Response

from apps.user.models import *
from apps.user.serializers import *
from apps.enroll.models import Enroll

from rest_framework.permissions import IsAdminUser
from apps.user.permissions import IsOwner



# patient profile 
class PatientProfileViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=UserSerializerList
    queryset=User.objects.all()
    permission_classes=(IsOwner,)


# doctor profile   
class DoctorProfileViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=DoctorProfileSerializerList
    permission_classes=(IsOwner,)

    def get_queryset(self):
        return User.objects.filter(is_doctor=True)


# admin confirmation
class AdminConfirmationApiView(generics.UpdateAPIView):
    serializer_class=AdminConfirmationSrializer
    queryset=User.objects.all()
    permission_classes=[IsAdminUser]

   





