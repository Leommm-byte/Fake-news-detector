const form = document.getElementById('predictionForm');

form.addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent default submission

    // Collect form data
    const formData = new FormData(form);

    // Send form data to server using fetch (example)
    fetch('/', {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            const prediction = data.prediction;

            // Create or get the resultElement
            let resultElement = document.getElementById('result');
            if (!resultElement) {
                resultElement = document.createElement('p');
                resultElement.id = 'result';
                document.body.appendChild(resultElement);
            }

            // Determine color based on prediction
            const predictionColor = prediction.includes('Fake news') ? '#f8d7da' : '#d4edda';

            // Update UI based on prediction
            document.body.style.backgroundColor = predictionColor;
            resultElement.textContent = prediction;  // Display prediction text
            resultElement.style.color = prediction.includes('Fake news') ? '#FF3838' : '#388038';
            resultElement.classList.add('fade-in'); // Trigger animation
        })
        .catch(error => console.error('Error:', error));
});
