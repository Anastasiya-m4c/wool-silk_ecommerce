/*
Core logic/payment flow for Stripe
*/

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

var card = elements.create('card', {
    style: style,
    hidePostalCode: true
});
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function(event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        $(errorDiv).html(`
            <span class="icon" role="alert"><i class="fas fa-times"></i></span>
            <span>${event.error.message}</span>
        `);
    } else {
        errorDiv.textContent = '';
    }
});

// Helper to safely get a field value
function safeFieldValue(form, name) {
    if (!form || !name) return '';
    var el = form.elements[name] || document.getElementById('id_' + name) || document.querySelector('[name="' + name + '"]');
    if (el) return $.trim(el.value || '');
    return '';
}

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true });
    $('#submit-button').attr('disabled', true);

    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var saveInfo = Boolean($('#id_save_info').prop('checked'));
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo
    };
    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: safeFieldValue(form, 'full_name'),
                    phone: safeFieldValue(form, 'phone_number'),
                    email: safeFieldValue(form, 'email'),
                    address: {
                        line1: safeFieldValue(form, 'street_address1'),
                        line2: safeFieldValue(form, 'street_address2'),
                        city: safeFieldValue(form, 'town_or_city'),
                        country: safeFieldValue(form, 'country')
                    }
                }
            }
        }).then(function(result) {
            if (result.error) {
                $('#card-errors').html(`
                    <span class="icon" role="alert"><i class="fas fa-times"></i></span>
                    <span>${result.error.message}</span>
                `);
                card.update({ 'disabled': false });
                $('#submit-button').attr('disabled', false);
            } else if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        });
    }).fail(function () {
        location.reload();
    });
});
