document.getElementById('submit').addEventListener('click', function() {
    var prompt = document.getElementById('prompt').value;
    fetch('/generate-text', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ prompt: prompt })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').innerText = data;
    })
    .catch(error => console.error('Error:', error));
});
