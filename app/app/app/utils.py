import subprocess
from difflib import SequenceMatcher
import pysrt
import whisper

def extract_audio(video_file, output_audio):
    subprocess.run(["ffmpeg", "-i", video_file, "-q:a", "0", "-map", "a", output_audio, "-y"])
    return output_audio

def transcribe_audio(audio_file, model="base"):
    whisper_model = whisper.load_model(model)
    result = whisper_model.transcribe(audio_file)
    return result["text"], result["segments"]

def align_subtitles(subtitles, transcript_segments):
    aligned_subtitles = []
    for subtitle in subtitles:
        subtitle_text = subtitle.text.strip()
        best_match = None
        best_score = 0
        best_segment = None

        for segment in transcript_segments:
            audio_text = segment["text"].strip()
            score = SequenceMatcher(None, subtitle_text, audio_text).ratio()
            if score > best_score:
                best_score = score
                best_match = segment["start"]
                best_segment = segment

        if best_match is not None:
            offset = best_segment["start"] - subtitle.start.seconds
            subtitle.shift(seconds=offset)
        aligned_subtitles.append(subtitle)

    return aligned_subtitles
```
