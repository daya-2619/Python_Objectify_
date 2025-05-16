document.getElementById('contact-form').addEventListener('submit', function(e) {
    e.preventDefault();  // Prevent the form from refreshing the page
    
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    fetch('/api/contact', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, email, message })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('status').innerText = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
