from unittest import loader
import uuid
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt  # new
from django.contrib import messages

from .models import Payment, PromoCode, Order
# from orders.models import Order
# import stripe

# stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request, order_id):
    # try:
    order = Order.objects.get(id=order_id)
    # Calculate the total amount
    total_amount = order.total_amount()
    discounted_amount = total_amount
    # discounted_amount = 0.0  # Initialize the discounted amount
    # Check if the order has already been paid
    if order.status == 'Completed':  # Replace 'paid' with your actual status value for a paid order
        messages.error(
            request, "This order payment has already been completed.")
        # Redirect to the dashboard or an appropriate page
        return redirect('/accounts/dashboard')

    if request.method == 'POST':

        card_number = request.POST.get('card_number')
        card_name = request.POST.get('card_name')
        expiry_month = request.POST.get('expiry_month')
        expiry_year = request.POST.get('expiry_year')
        cvv = request.POST.get('cvv')
        promo_code_input = request.POST.get('promo_code', None)

        if request.user.is_authenticated:
            user_id = request.user.id
        else:
            # User is not logged in, assign a default or generated user ID
            user_id = generate_visitor_id()

        # Apply promo code if available
        if promo_code_input:
            try:
                promo_code_obj = PromoCode.objects.get(
                    promo_code=promo_code_input, is_active=True)
                if promo_code_obj.is_valid():
                    discount = (
                        promo_code_obj.discount_percentage * 0.01) * total_amount
                    discounted_amount = total_amount - discount
                else:
                    messages.error(
                        request, 'Promo code is not valid or expired')
            except PromoCode.DoesNotExist:
                messages.error(request, 'Invalid promo code')

        payment = Payment.objects.create(
            order=order,
            amount=total_amount,
            discounted_amount=discounted_amount,  # Save discounted amount
            promo_code=promo_code_input if promo_code_input else "",  # Save promo code

            card_number=card_number,
            cardholder_name=card_name,
            expiry_month=expiry_month,
            expiry_year=expiry_year,
            cvv=cvv,
        )

        # Additional logic for successful payment (e.g., updating order status, sending confirmation emails)
        payment.save()

        order.status = 'Completed'  # Update this according to your defined status choices
        order.save()
        messages.success(
            request, 'Your order has been submitted, see you shortly.')

        # Redirect to a success page
        # Prepare context data for rendering
        # context = {
        #     'order': order,
        #     'payment': payment,
        #     'user': request.user
        # }
        # return render(request, 'accounts/dashboard.html', context)
        # Redirect to the dashboard instead of rendering it directly
        # return redirect('/accounts/dashboard')
    return redirect('/accounts/dashboard')


def generate_visitor_id():
    # Your logic to generate or provide a default user ID
    # This could be a static ID, a random ID, or whatever suits your application's needs
    # For example, return a static ID like -1 or generate a random one
    # Generate a new UUID
    new_id = uuid.uuid4()

    # Return the new ID
    return new_id


def apply_promo_code(request, order_id):
    if request.method == 'POST':
        promo_code_input = request.POST.get('promo_code', "")

        try:
            order = Order.objects.get(id=order_id)
            promo_code_obj = PromoCode.objects.get(
                promo_code=promo_code_input, is_active=True)

            if promo_code_obj.is_valid():
                # Calculate the potential discount
                discount_percentage = promo_code_obj.discount_percentage
                new_total = order.total_amount()*(1 - (discount_percentage * 0.01))
                return JsonResponse({
                    'success': True,
                    'new_total': new_total,
                    'promo_code_applied': True
                })
            else:
                return JsonResponse({'success': False, 'error': 'Promo code is not valid or expired'})
        except PromoCode.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Invalid promo code'})

    return JsonResponse({'success': False, 'error': 'Invalid request'})


def remove_order(request, order_id):
    # Ensure only authenticated users can remove orders
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to remove an order.")
        return redirect('login')
    # order = Order.objects.get(id=order_id)

    order = get_object_or_404(Order, id=order_id)

    # Check if the order is already completed, prevent removal
    if order.status == "Completed":
        messages.error(request, "Completed orders cannot be removed.")
    else:
        order.delete()
        messages.success(request, "Order removed successfully.")

    return redirect('/accounts/dashboard')


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


def success_view(request):
    # Render a success page
    return render(request, 'account/success.html')
