document.addEventListener('DOMContentLoaded', function () {
    const stars = document.querySelectorAll('.rating-stars i');

    stars.forEach(star => {
        star.addEventListener('mouseover', function () {
            const rating = this.getAttribute('data-rating');
            highlightStars(rating);
            this.style.cursor = 'pointer'; // Change cursor to pointer
        });

        star.addEventListener('mouseout', function () {
            resetStars();
        });

        star.addEventListener('click', function () {
            const rating = this.getAttribute('data-rating');
            alert('You rated ' + rating + ' stars!');
        });
    });

    function highlightStars(rating) {
        stars.forEach(star => {
            const starRating = star.getAttribute('data-rating');
            if (starRating <= rating) {
                star.style.color = '#FF9529';
            }
        });
    }

    function resetStars() {
        stars.forEach(star => {
            star.style.color = '';
            star.style.cursor = ''; // Reset cursor to default
        });
    }

   
});

