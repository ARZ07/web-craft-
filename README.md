# web-craft-


## Overview
This project provides an automated solution to synchronize subtitle files with video files by aligning subtitle timing with the transcribed audio. It uses Flask for the API, FFmpeg for audio extraction, Whisper for transcription, and Python libraries for subtitle adjustments.

---

### File Structure
Organize your repository as follows:

```
subtitle-sync-tool/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── utils.py
├── requirements.txt
├── README.md
├── .gitignore
├── run.py
└── tests/
    ├── test_routes.py
    ├── test_utils.py
```

---

### Project Files

1. **`app/__init__.py`**: Initializes the Flask app.
2. **`app/routes.py`**: Contains API routes and core logic.
3. **`app/utils.py`**: Includes utility functions such as audio extraction, transcription, and subtitle alignment.
4. **`requirements.txt`**: Lists all Python dependencies.
5. **`README.md`**: Provides an overview and usage instructions.
6. **`run.py`**: Entry point to start the Flask application.
7. **`tests/`**: Contains test cases for the API and utility functions.
8. **`.gitignore`**: Specifies files and directories to exclude from Git.

---
