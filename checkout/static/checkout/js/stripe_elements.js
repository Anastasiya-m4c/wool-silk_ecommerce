/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
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
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// safe helper to get a field value from the form (avoids undefined.value crashes)
function safeFieldValue(form, name) {
    if (!form || !name) return '';
    // try form.elements[name] first
    try {
        var el = form.elements[name];
        if (el) {
            // RadioNodeList or single element
            if (el.length && el[0]) return $.trim(el[0].value || '');
            return $.trim(el.value || '');
        }
    } catch (e) {
        // ignore and try next
    }
    // try Django-style id 'id_<name>'
    var idEl = document.getElementById('id_' + name);
    if (idEl && typeof idEl.value !== 'undefined') return $.trim(idEl.value || '');
    // try plain name selector
    var qs = document.querySelector('[name="' + name + '"]');
    if (qs && typeof qs.value !== 'undefined') return $.trim(qs.value || '');
    return '';
}

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    
    var saveInfo = Boolean($('#id_save_info').attr('checked'));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
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
                        country: safeFieldValue(form, 'country'),
                    }
                }
                
            },
        }).then(function(result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                card.update({ 'disabled': false});
                $('#submit-button').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function () {
        location.reload();
    })
});