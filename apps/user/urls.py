from django.urls import path

from apps.user.views import *



urlpatterns=[
    # all profiles
    path('profile/<int:pk>/',PatientProfileViewSet.as_view()),
    path('doctor/profile/<int:pk>/',DoctorProfileViewSet.as_view()),
 
    # admin confirmation
    path('admin/give/permission/<int:pk>/',AdminConfirmationApiView.as_view()),

]