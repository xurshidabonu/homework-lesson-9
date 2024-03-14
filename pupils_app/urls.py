from django.urls import path
from .views import pupils,pupil_info



urlpatterns=[
    path('pupils/',pupils,name='pupils'),
    path('pupils/<int:pk>/',pupil_info,name="pupil_info")



]