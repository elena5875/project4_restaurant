$(document).ready(function() {
    // Handle form submission
    $('#reservationForm').submit(function(event) {
        event.preventDefault(); // Prevent the form from submitting normally
        
        // Serialize form data
        var formData = $(this).serialize();
        
        // Send an AJAX request to handle form submission
        $.ajax({
            type: 'POST',
            url: '/reservation/', // Update the URL with your endpoint
            data: formData,
            success: function(response) {
                // Populate the modal with the confirmation details
                $('#confirmationModal .modal-body').html(response);
                // Show the modal
                $('#confirmationModal').modal('show');
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText); // Log any errors
            }
        });
    });
});
