const contactForm = document.getElementById('contact-form');

contactForm.addEventListener('submit', function(event) {
    event.preventDefault(); 

    const formData = new URLSearchParams(new FormData(contactForm));

    fetch('https://contact-form-api.elson-matra.workers.dev', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: formData
    })
    .then(response => {
        if (response.ok) {
            alert('Message sent successfully!');
            contactForm.reset(); 
        } else {
            alert('Something went wrong. Please try again.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Could not connect to the server.');
    });
});