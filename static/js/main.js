document.addEventListener('DOMContentLoaded', function () {
    const stars = document.querySelectorAll('.rating-stars i');
    let selectedRating = 0;
    let userHasRated = false; // Variable to track whether the user has already rated

    stars.forEach(star => {
        star.addEventListener('mouseover', function () {
            if (!userHasRated) {
                const rating = this.getAttribute('data-rating');
                highlightStars(rating);
                this.style.cursor = 'pointer'; // Change cursor to pointer
            }
        });

        star.addEventListener('mouseout', function () {
            if (!userHasRated) {
                resetStars();
            }
        });

        star.addEventListener('click', function () {
            if (!userHasRated) {
                const rating = this.getAttribute('data-rating');
                alert('You rated ' + rating + ' stars!');
                userHasRated = true; // Set the flag to indicate that the user has rated
                // Additional logic to update the UI or send the rating to the server if needed
            }
        });
    });


    // Function to check if the user has already rated
    function checkUserRating() {
        fetchUserRating(); // Fetch user's previous rating

        // If the user has already rated, highlight the stars and disable rating
        if (selectedRating > 0) {
            highlightStars(selectedRating);
            disableRating();
        }
    }

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

    function disableRating() {
        stars.forEach(star => {
            star.style.pointerEvents = 'none'; // Disable hovering and clicking
        });
    }

    function sendRatingRequest(rating) {
        const courseId = document.getElementById('courseId').value;
        const url = `/course/${courseId}/rate`;
        const params = `value=${rating}`;

        const xhr = new XMLHttpRequest();
        xhr.open('POST', url, true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

        // Get the CSRF token from the web core context
        const csrfTokenInput = document.querySelector('input[name="csrf_token"]');
        const csrfToken = csrfTokenInput ? csrfTokenInput.value : '';
        xhr.setRequestHeader('X-CSRF-Token', csrfToken);

        xhr.onload = function () {
            if (xhr.status === 200) {
                alert('You rated ' + rating + ' stars!');
                selectedRating = rating;
                highlightStars(selectedRating);
                disableRating();
            } else {
                alert('Error: ' + xhr.statusText);
            }
        };

        xhr.onerror = function () {
            alert('Network error');
        };

        xhr.send(params);
    }

    // Function to fetch user's previous rating
    function fetchUserRating() {
        try {
            const courseId = document.getElementById("courseId").value; // Replace with your actual course ID
            const xhr = new XMLHttpRequest();
            xhr.open('GET', `/course/${courseId}/user_rating`, true);

            xhr.onreadystatechange = function () {
                if (xhr.readyState === XMLHttpRequest.DONE) {
                    if (xhr.status === 200) {
                        try {
                            const data = JSON.parse(xhr.responseText);
                            if (data.result === 'success') {
                                selectedRating = data.average_rating;
                                if(data.user_rating != 0){
                                    highlightStars(selectedRating);
                                    disableRating();
                                }
                            } else {
                                // Handle the error case if needed
                                console.error('Error fetching user rating:', data.message);
                            }
                        } catch (error) {
                            console.error('Error parsing JSON:', error.message);
                        }
                    } else {
                        // Handle the error case if needed
                        console.error('Error fetching user rating:', xhr.statusText);
                    }
                }
            };

            xhr.onerror = function () {
                // Handle any other errors that may occur during the request
                console.error('Error fetching user rating:', 'Network error');
            };

            xhr.send();
        } catch (error) {
            // Handle any other errors that may occur
            console.error('Error fetching user rating:', error.message);
        }
    }

    // Check if the user has already rated when the page loads
    checkUserRating();
});
