from django.urls import path, include
from . import views

urlpatterns = [
    path('checkout/<int:order_id>/', views.checkout, name='checkout'),
    path('apply-code/<int:order_id>/<str:code>/',
         views.apply_promo_code, name='apply_promo_code'),

]
