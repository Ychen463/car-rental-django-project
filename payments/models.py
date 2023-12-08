import datetime
from django.db import models
from orders.models import Order
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class Payment(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    # Add the discounted_amount field
    discounted_amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=amount)

    promo_code = models.CharField(max_length=100, blank=True, null=True)
    payment_token = models.CharField(max_length=100, blank=True, null=True)
    transaction_id = models.CharField(
        max_length=100, unique=True, blank=True, null=True)

    # Assuming standard 16-digit card number
    card_number = models.CharField(max_length=16, blank=True, null=True)
    cardholder_name = models.CharField(max_length=100, blank=True, null=True)
    expiry_month = models.CharField(
        max_length=2, blank=True, null=True)  # Format 'MM'
    expiry_year = models.CharField(
        max_length=4, blank=True, null=True)  # Format 'YYYY'
    # CVV can be 3 or 4 digits
    cvv = models.CharField(max_length=4, blank=True, null=True)

    create_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"Payment for Order {self.order.id}"


class PromoCode(models.Model):
    promo_code = models.CharField(max_length=50, unique=True)
    discount_percentage = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)])
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    max_uses = models.PositiveIntegerField(default=1)  # Added field
    used_times = models.PositiveIntegerField(default=0)  # Added field
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.promo_code

    def is_valid(self):
        current_time = timezone.now()
        return (
            self.is_active and
            self.valid_from <= current_time <= self.valid_to and
            self.used_times < self.max_uses
        )


# def is_valid(self):
#     current_time = timezone.now()
#     return (
#         self.is_active and
#         self.valid_from <= current_time <= self.valid_to and
#         self.used_times < self.max_uses
#     )
