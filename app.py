from flask import Flask, request, render_template_string, redirect, jsonify
import requests

app = Flask(__name__)

backend_url = 'https://icv-backend.onrender.com/download'

@app.route('/')
def index():
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>iConverter ♻️</title>
            <link rel="stylesheet" href="/static/styles.css">
        </head>
        <body>
            <div class="container">
                <h1>iConverter ♻️</h1>
                <p>With this Youtube -> MP4 converter, <br>you can download any YouTube video<br> for completely <b>FREE</b>!</p>
                <form id="download-form">
                    <input type="text" id="url" name="url" placeholder="Enter YouTube URL" required>
                    <br><br>
                    <button type="submit" class="submit" id="submit">Download</button>
                </form>
            </div>
            <script src="/static/main.js"></script>
        </body>
        </html>
    ''')

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    url = data['url']
    response = requests.post(backend_url, json={'url': url})
    
    if response.status_code == 200:
        return jsonify({'message': 'Download started successfully'}), 200
    else:
        return jsonify({'error': 'Failed to start download'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
