from django.urls import path, include
from . import views

urlpatterns = [
    path('checkout/<int:order_id>/', views.checkout, name='checkout'),
    path('apply_promo_code/<int:order_id>/',
         views.apply_promo_code, name='apply_promo_code'),

    # path('payments/apply_promo_code/<int:order_id>/',
    #      views.apply_promo_code, name='apply_promo_code'),
    path('config/', views.stripe_config),  # new


]
