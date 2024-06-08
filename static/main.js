document.getElementById('submit').addEventListener('click', async function (e) {
    e.preventDefault();
    const url = document.getElementById('url').value;
    const response = await fetch('https://icv-backend.onrender.com/download', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url })
    });
    const blob = await response.blob();
    const link = document.createElement('a');
    link.href = window.URL.createObjectURL(blob);
    link.download = 'video.mp4';
    link.click();
});
