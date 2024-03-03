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
