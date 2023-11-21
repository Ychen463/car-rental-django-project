from unittest import loader
import uuid
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt  # new
from django.contrib import messages

from .models import Payment, PromoCode, Order
# from orders.models import Order
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request, order_id, promo_code):
    # Logic to process checkout
    order = Order.objects.get(id=order_id)

    if request.method == 'POST':
        # Retrieve Stripe token and other payment information from the form
        # token = request.POST.get('stripeToken')

        try:
            # Calculate total amount (consider applying discounts, taxes, etc.)
            # Assuming you have a method to calculate total
            total_amount = order.total_amount()
            # Get data from the form
            card_number = request.POST.get('card_number')
            card_name = request.POST.get('card_name')
            expiry_month = request.POST.get('expiry_month')
            expiry_year = request.POST.get('expiry_year')
            cvv = request.POST.get('cvv')
            if request.user.is_authenticated:
                user_id = request.user.id
            else:
                # User is not logged in, assign a default or generated user ID
                user_id = generate_visitor_id()

            # Create a Payment record
            payment = Payment.objects.create(
                order=order,
                amount=total_amount,
                # transaction_id=charge.id
                card_number=card_number,
                cardholder_name=card_name,
                expiry_month=expiry_month,
                expiry_year=expiry_year,
                cvv=cvv
            )

            # Additional logic for successful payment (e.g., updating order status, sending confirmation emails)
            payment.save()
            # Redirect to a success page
            return redirect('/accounts/dashboard')

        except stripe.error.CardError as e:
            #     # Handle card error
            context = {'error_message': str(e)}

            return render(request, '/accounts/dashboard', context)
    messages.success(
        request, 'Your order has been submitted, see you shortly.')
    # For GET request, render checkout page
    # return render(request, 'payments/checkout.html', {'order': order})
    redirect('/accounts/dashboard')


def generate_visitor_id():
    # Your logic to generate or provide a default user ID
    # This could be a static ID, a random ID, or whatever suits your application's needs
    # For example, return a static ID like -1 or generate a random one
    # Generate a new UUID
    new_id = uuid.uuid4()

    # Return the new ID
    return new_id


def apply_promo_code(request, order_id):
    # Assuming this is an AJAX request
    if request.method == 'POST':
        promo_code_input = request.POST.get('promo_code', "")

        try:
            order = Order.objects.get(id=order_id)
            promo_code_obj = PromoCode.objects.get(
                promo_code=promo_code_input, is_active=True)

            # Logic to apply promo code (e.g., updating order total)
            if not promo_code_obj.is_valid():

                return JsonResponse({'success': False, 'error': 'Promo code is not valid or expired'})

            # Calculate the discount
            print("Total amount:", order.total_amount())

            new_total = (promo_code_obj.discount_percentage *
                         0.01) * order.total_amount()
            order.discounted_amount = new_total
            order.promo_code_applied = True

            print("discount amount:", order.discounted_amount)

            order.save()

            return JsonResponse({'success': True, 'new_total': new_total,  'promo_code_applied': True})
        except PromoCode.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Invalid promo code'})

    return JsonResponse({'success': False, 'error': 'Invalid request'})

# Add a view for successful payment
# new


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


def success_view(request):
    # Render a success page
    return render(request, 'account/success.html')
