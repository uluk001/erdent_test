from django.urls import path
from apps.medical_card.views import *


urlpatterns=[
    path('doctor/create/',MedicalCardCreateApiView.as_view()),
    path('doctor/do/card/<int:pk>/',MedicalCardApiView.as_view()),
    path('doctor/week_activity/<int:pk>/', WeekActivityDetailApiView.as_view())
    ]
