
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return "Main hola"

@app.route('/saluda/clase')
def saluda():
    return "<marquee><h1>HOLA CLASE</h1></marquee>"
if __name__ == '__main__':
    app.run()