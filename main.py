from flask import Flask
import os


app = Flask(__name__)
app.secret_key = os.urandom(12).hex()

@app.route('/')
def index():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)
