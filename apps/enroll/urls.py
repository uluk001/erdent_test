from django.urls import path

from apps.enroll.views import *

urlpatterns=[
    
    path('create/',EnrollCreateApiView.as_view()),
    path('doctors/free/time/<int:pk>/',DoctorsTime.as_view()),
    path('todays/patients/',DoctorsPatientForTodayApiView.as_view()),
    path('operator/list/',OperatorsApiView.as_view()),
    path('operator/enroll/delete/<int:pk>/',OperatorDeleteApiView.as_view()),

    ]

