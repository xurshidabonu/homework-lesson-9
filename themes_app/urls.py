from django.urls import path

from .views import index


urlpatterns=[
    path('themes/',index,name='index'),
    path('',index,name='index'),
]