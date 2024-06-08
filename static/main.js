document.getElementById('download-form').addEventListener('submit', async function (e) {
    e.preventDefault();
    const url = document.getElementById('url').value;
    const response = await fetch('/download', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url })
    });
    const result = await response.json();
    if (response.ok) {
        alert(result.message);
    } else {
        alert(result.error);
    }
});
