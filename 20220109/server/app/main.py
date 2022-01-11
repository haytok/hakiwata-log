from flask import Flask
from flask_cors import CORS 

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

@app.route('/')
def index():
    return app.send_static_file('html/server.html')

app.run(debug=True, host='0.0.0.0', port=8000)
