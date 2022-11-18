from django.urls import path

from apps.dental.views import *

urlpatterns=[
    path('patients/payment/',CashierApiView.as_view()),
    path('patients/payment/<int:pk>/',CashierIsPayedApiView.as_view()),
    path('my/medical/cards/all/',UserMedicalCards.as_view()),

    ]
