from django.contrib import admin
from .models import Payment, PromoCode  # Combined import statement


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'amount', 'status', 'promo_code', 'create_date')
    list_filter = ('status',)
    search_fields = ('order__id', 'promo_code')
    date_hierarchy = 'create_date'


@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ('promo_code', 'discount_percentage',
                    'valid_from', 'valid_to', 'is_active')
    list_filter = ('is_active', 'valid_from', 'valid_to')
    search_fields = ('promo_code',)
