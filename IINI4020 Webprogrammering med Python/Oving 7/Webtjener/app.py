"""
        Øving 7
        24.10.2018
        Anders Kvanvig

    Python 3
"""

import os
from flask import Flask, request, render_template, make_response
from flask_bootstrap import Bootstrap

video_dir = '/Users/Ander/OneDrive - NTNU/Python-Oving/IINI4020 Webprogrammering med Python/Oving 7/Webtjener/static/video'
template_dir = '/Users/Ander/OneDrive - NTNU/Python-Oving/IINI4020 Webprogrammering med Python/Oving 7/Webtjener/templates'

app = Flask(__name__)
Bootstrap(app)
app.config.from_object(__name__)

@app.route('/')
def index():
    video_files = [f for f in os.listdir(video_dir) if f.endswith('mp4')]
    svg_files = [f for f in os.listdir(template_dir) if f.endswith('svg')]
    return render_template('index.html',
                            title = 'Hovedside øving 7',
                            video_files = video_files,
                            svg_files = svg_files)


@app.route('/video/<filename>')
def video(filename):
    return render_template('video.html',
                            title = filename.replace('.mp4', ''),
                            video_file = filename,
                            video_file_ogg = filename.replace('.mp4', '.ogg'))

@app.route('/svg/<filename>')
def svg(filename):
    return render_template('svg.html',
                            svg_navn = filename)

if __name__ == '__main__':
    app.run(debug = True)
