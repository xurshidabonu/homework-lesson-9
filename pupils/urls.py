from django.urls import path
from . import views

urlpatterns = [
    path('', views.pupil_list, name='pupil_list'),
    path('<int:pk>/', views.pupil_detail, name='pupil_detail'),
]

