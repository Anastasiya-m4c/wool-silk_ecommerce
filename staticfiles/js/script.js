document.addEventListener('DOMContentLoaded', function() {
    const nav = document.querySelector('nav');
    const toasts = document.querySelectorAll('.toast');
    
    if (nav && toasts.length > 0) {
        nav.addEventListener('click', function() {
            toasts.forEach(function(toast) {
                const bsToast = bootstrap.Toast.getInstance(toast);
                if (bsToast) {
                    bsToast.hide();
                }
            });
        });
    }
});

