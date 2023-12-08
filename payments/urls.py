from django.urls import path, include
from . import views

urlpatterns = [
    path('checkout/<int:order_id>/', views.checkout, name='checkout'),
    path('remove_order/<int:order_id>/',
         views.remove_order, name='remove_order'),
    path('apply_promo_code/<int:order_id>/',
         views.apply_promo_code, name='apply_promo_code'),

    # path('payments/apply_promo_code/<int:order_id>/',
    #      views.apply_promo_code, name='apply_promo_code'),
    path('config/', views.stripe_config),  # new


]
