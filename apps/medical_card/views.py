import datetime

from rest_framework import generics
from rest_framework.response import Response 
from rest_framework.permissions import IsAdminUser
from apps.medical_card.models import MedicalCards
from apps.user.permissions import IsDoctors
from apps.medical_card.serializers import MedCardsCreateSerializers, WeekActivitySerilizer


class MedicalCardCreateApiView(generics.CreateAPIView):
    queryset = MedicalCards.objects.all()
    serializer_class = MedCardsCreateSerializers
    permission_classes = [IsDoctors]

    def perform_create(self, serializer):
        return serializer.save(doctor=self.request.user)


class MedicalCardApiView(generics.RetrieveUpdateAPIView):
    queryset=MedicalCards.objects.all()
    serializer_class=MedCardsCreateSerializers
    permission_classes=[IsDoctors]

    def perform_create(self, serializer):
        return serializer.save(doctor=self.request.user)


class WeekActivityDetailApiView(generics.RetrieveAPIView):
    serializer_class = WeekActivitySerilizer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk', None)
        today = datetime.datetime.today().date()
        date = today - datetime.timedelta(days=7)
        doctor = MedicalCards.objects.filter(doctor_id = pk).filter(data__gte = date).filter(data__lte = today).values()
        return Response({'Doctor activity for a week.':list(doctor)})