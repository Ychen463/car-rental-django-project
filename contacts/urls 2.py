from django.urls import path, include
from . import views

urlpatterns = [
    path('inquiry', views.inquiry, name='inquiry'),
]
