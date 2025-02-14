async function embedMessage() {
    const message = document.getElementById('embedMessage').value;
    const imageFile = document.getElementById('embedImage').files[0];
    const reader = new FileReader();

    reader.onload = async function(event) {
        const response = await fetch('/embed', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                image_path: event.target.result,
                secret_message: message
            })
        });

        const result = await response.json();
        document.getElementById('result').innerText = `Image saved at: ${result.result_image}`;
    };

    reader.readAsDataURL(imageFile);
}

async function extractMessage() {
    const imageFile = document.getElementById('extractImage').files[0];
    const reader = new FileReader();

    reader.onload = async function(event) {
        const response = await fetch('/extract', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                image_path: event.target.result
            })
        });

        const result = await response.json();
        document.getElementById('result').innerText = `Extracted Message: ${result.secret_message}`;
    };

    reader.readAsDataURL(imageFile);
}

async function classifyData() {
    const inputData = document.getElementById('classifyInput').value;

    const response = await fetch('/classify', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            input_data: inputData
        })
    });

    const result = await response.json();
    document.getElementById('result').innerText = `Classification Result: ${result.classification}`;
}
