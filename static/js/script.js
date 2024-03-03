// script.js

// Smooth scrolling for anchor links
document.addEventListener('DOMContentLoaded', function() {
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    
    for (let anchorLink of anchorLinks) {
        anchorLink.addEventListener('click', function(e) {
            e.preventDefault();

            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                const offsetTop = targetElement.offsetTop;
                const scrollOptions = {
                    top: offsetTop,
                    behavior: 'smooth'
                };
                window.scrollTo(scrollOptions);
            }
        });
    }
});
 

//time function

$(document).ready(function() {
    // Generate time options from 5 pm to 11 pm
    var selectTime = $('#time');
    for (var hour = 17; hour <= 23; hour++) {
        var displayHour = (hour % 12 == 0) ? 12 : hour % 12; // Convert to 12-hour format
        var ampm = (hour < 12 || hour == 24) ? 'AM' : 'PM';
        selectTime.append($('<option>').val(hour).text(displayHour + ':00 ' + ampm));
    }
});
</script>
