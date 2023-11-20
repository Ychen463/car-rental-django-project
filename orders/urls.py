from django.urls import path, include
from . import views

urlpatterns = [
    path('reserve', views.reserve, name='reserve'),
]
