document.addEventListener('DOMContentLoaded', function() {
    // Attach a submit event listener to each promo code form
    document.querySelectorAll('.promo-code-form').forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();

            var orderId = this.getAttribute('data-order-id');
            var promoCode = this.querySelector('input[name="promo_code"]').value;
            var csrfToken = this.querySelector('input[name="csrfmiddlewaretoken"]').value;

            // Construct the URL for the AJAX request
            var url = "/payments/apply_promo_code/" + orderId + "/";

            // AJAX request
            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': csrfToken
                },
                body: 'promo_code=' + encodeURIComponent(promoCode)
            })
            .then(response => response.json())
            .then(data => {
                // Handle the response
                var responseElement = document.getElementById('promoResponse' + orderId);
                if(data.success) {
                    document.getElementById('discountedAmount' + orderId).innerText = '$' + data.new_total;
                    document.getElementById('discountedAmount_checkout' + orderId).innerText = '$' + data.new_total;

                    // Optionally, update the response element to show success message
                    var responseElement = document.getElementById('promoResponse' + orderId);
                    responseElement.innerText = 'Discount applied successfully';
                
                } else {
                    // Handle errors
                    document.getElementById('promoResponse' + orderId).innerText = 'Error: ' + data.error;
              
                }
            })
            .catch(error => {
                console.error('Error:', error);
                document.getElementById('promoResponse' + orderId).innerText = 'Error: ' + error;
            });

        });
    });
});
document.addEventListener("DOMContentLoaded", function () {
    // Find all Check Out buttons by their class name
    const checkoutButtons = document.querySelectorAll(".checkout-button");
    const checkoutForm = document.getElementById("checkoutForm");

    // Add a click event listener to each Check Out button
    checkoutButtons.forEach(function (checkoutButton) {
        checkoutButton.addEventListener("click", function () {
            // Get the specific order ID from the clicked button's data attribute
            const specificOrderId = this.getAttribute("data-order-id");

            // Get the data-action attribute value (URL) from the button
            const dataAction = this.getAttribute("data-action");

            // Set the value of the hidden input field to the specific order ID
            document.querySelector("#specificOrderIdInput").value = specificOrderId;

            // Set the form action to the data-action URL
            checkoutForm.action = dataAction;
               });
    });
});

