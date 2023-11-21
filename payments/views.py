from unittest import loader
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Payment, PromoCode
from orders.models import Order
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request, order_id):
    # Logic to process checkout
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        # Retrieve Stripe token and other payment information from the form
        token = request.POST.get('stripeToken')

        try:
            # Calculate total amount (consider applying discounts, taxes, etc.)
            # Assuming you have a method to calculate total
            total_amount = order.total_amount()

            # Create a charge on Stripe
            charge = stripe.Charge.create(
                amount=int(total_amount * 100),  # Amount in cents
                currency='usd',
                description=f'Order {order_id}',
                source=token
            )

            # Create a Payment record
            payment = Payment.objects.create(
                order=order,
                amount=total_amount,
                transaction_id=charge.id
            )

            # Additional logic for successful payment (e.g., updating order status, sending confirmation emails)

            return redirect('success_view')  # Redirect to a success page

        except stripe.error.CardError as e:
            # Handle card error
            context = {'error_message': str(e)}

            return render(request, 'payments/checkout.html', context)

    # For GET request, render checkout page
    return render(request, 'payments/checkout.html', {'order': order})


def apply_promo_code(request, order_id, code):
    # Assuming this is an AJAX request
    if request.method == 'POST':
        try:
            promo_code = PromoCode.objects.get(code=code, is_active=True)
            order = Order.objects.get(id=order_id)

            # Logic to apply promo code (e.g., updating order total)
            # ...

            return JsonResponse({'success': True, 'new_total': order.total_amount()})
        except PromoCode.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Invalid promo code'})

    return JsonResponse({'success': False, 'error': 'Invalid request'})

# Add a view for successful payment


def success_view(request):
    # Render a success page
    return render(request, 'account/success.html')
