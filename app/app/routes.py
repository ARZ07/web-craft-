from flask import request, jsonify, send_file
import os
import pysrt
from werkzeug.utils import secure_filename
from app.utils import extract_audio, transcribe_audio, align_subtitles
from app import app

@app.route('/sync-subtitles', methods=['POST'])
def sync_subtitles():
    if 'video' not in request.files or 'subtitle' not in request.files:
        return jsonify({"error": "Video and subtitle files are required."}), 400

    video_file = request.files['video']
    subtitle_file = request.files['subtitle']

    video_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(video_file.filename))
    subtitle_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(subtitle_file.filename))

    video_file.save(video_path)
    subtitle_file.save(subtitle_path)

    audio_path = os.path.join(app.config['UPLOAD_FOLDER'], 'temp_audio.wav')
    extract_audio(video_path, audio_path)

    transcript_text, transcript_segments = transcribe_audio(audio_path)
    subtitles = pysrt.open(subtitle_path)
    adjusted_subtitles = align_subtitles(subtitles, transcript_segments)

    corrected_subtitle_path = os.path.join(app.config['UPLOAD_FOLDER'], 'corrected_' + subtitle_file.filename)
    adjusted_subtitles.save(corrected_subtitle_path, encoding="utf-8")

    return send_file(corrected_subtitle_path, as_attachment=True)
```
