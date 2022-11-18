import datetime
from rest_framework import generics
from rest_framework.response import Response

from apps.user.permissions import  IsOperator,IsOwner
from apps.medical_card.models import MedicalCards
from apps.medical_card.serializers import CashierMedicalCardsPriceSerializers,CashierMedicalCardsIsPayedSerializers


class CashierApiView(generics.ListAPIView):
    serializer_class=CashierMedicalCardsPriceSerializers
    permission_classes=[IsOperator]

    def get_queryset(self):
        operator=self.request.user.branch
        return MedicalCards.objects.filter(doctor__branch=operator,is_payed=False)


class CashierIsPayedApiView(generics.RetrieveUpdateAPIView):
    permission_classes=[IsOperator]
    serializer_class=CashierMedicalCardsIsPayedSerializers

    def get_queryset(self):
        operator=self.request.user.branch
        return MedicalCards.objects.filter(doctor__branch=operator)


class UserMedicalCards(generics.ListAPIView):
    permission_classes=[IsOwner]
    serializer_class=CashierMedicalCardsPriceSerializers

    def get_queryset(self):
        return MedicalCards.objects.filter(patient=self.request.user)