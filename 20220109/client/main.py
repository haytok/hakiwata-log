from flask import Flask

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    return app.send_static_file('html/client.html')


app.run(debug=True, host='0.0.0.0', port=8000)
