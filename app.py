from flask import Flask, request, send_file, render_template_string, after_this_request, redirect
from pytube import YouTube
import tempfile
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>YouTube to MP4</title>
            <link rel="stylesheet" href="/static/styles.css">
        </head>
        <body>
            <div class="container">
                <h1>YT -> MP4 🎥</h1>
                <p>With this Youtube -> MP4 converter, <br>you can download any YouTube video<br> for completely <b>FREE</b>!</p>
                <form action="/download" method="post">
                    <input type="text" name="url" placeholder="Enter YouTube URL" required>
                    <br><br>
                    <button type="submit">Download</button>
                </form>
            </div>
            <script src="static/main.js"></script>
        </body>
        </html>
    ''')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
    
    # Create a temporary file
    temp_dir = tempfile.gettempdir()
    temp_file_path = os.path.join(temp_dir, f"{yt.title}.mp4")
    stream.download(output_path=temp_dir, filename=f"{yt.title}.mp4")
    
    @after_this_request
    def remove_file(response):
        try:
            os.remove(temp_file_path)
        except Exception as error:
            app.logger.error("Error removing downloaded file: %s", error)
        return response

    return send_file(temp_file_path, as_attachment=True, download_name=f"{yt.title}.mp4")

if __name__ == '__main__':
    app.run(debug=True)
