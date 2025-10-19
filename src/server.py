from flask import Flask
from flask import request, jsonify
from .routes.testi import testi_bp

app = Flask(__name__)
app.register_blueprint(testi_bp)

def main():
    app.run(debug=True)