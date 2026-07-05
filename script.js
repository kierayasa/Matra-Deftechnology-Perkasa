const contactForm = document.getElementById('contact-form');

contactForm.addEventListener('submit', function(event) {
    event.preventDefault(); 

    // Create a new empty FormData object
    const formData = new FormData();
    
    // Explicitly grab the values and append them to match worker.js expectations
    formData.append('name', document.getElementsByName('name')[0].value);
    formData.append('email', document.getElementsByName('email')[0].value);
    formData.append('message', document.getElementsByName('message')[0].value);

    fetch('https://contact-form-api.elson-matra.workers.dev', {
        method: 'POST',
        body: formData // Browser automatically structures this as multipart/form-data
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