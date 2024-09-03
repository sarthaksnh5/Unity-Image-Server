document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();

    let formData = new FormData(this);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        if (data.image_id) {
            this.reset();
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Image upload failed.');
    });
});
