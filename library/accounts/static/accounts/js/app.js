<script>
    document.addEventListener('DOMContentLoaded', function() {
        // Focus on the first input field if there are errors
        const errors = document.querySelectorAll('.text-red-600');
        if (errors.length > 0) {
            const firstErrorField = errors[0].previousElementSibling;
            if (firstErrorField) {
                firstErrorField.focus();
            }
        }

        // Add transition effect to buttons
        const buttons = document.querySelectorAll('button');
        buttons.forEach(button => {
            button.addEventListener('mouseover', () => {
                button.classList.add('transition-transform', 'transform', 'scale-105');
            });
            button.addEventListener('mouseout', () => {
                button.classList.remove('transition-transform', 'transform', 'scale-105');
            });
        });
    });
</script>
