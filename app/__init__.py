from flask import Flask
import tempfile

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = tempfile.gettempdir()

from app import routes
```
