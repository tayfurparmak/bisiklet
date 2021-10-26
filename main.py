from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__)

import _Bisiklet
import _Zimmet
import _Ucret
import _Kisi
import _Kiralama
import _Istasyon
import _Gorevli
@app.route('/', methods=["GET"])
def Base():
    return """
        <link rel="stylesheet" href="bootstrap.min.css" />
        <div class="container mt-3">
            <div class="list-group">
                <a href="Bisiklet.html" class="list-group-item list-group-item-action">Bisiklet</a>
                <a href="Kisi.html" class="list-group-item list-group-item-action">Kisi</a>
                <a href="Istasyon.html" class="list-group-item list-group-item-action">Istasyon</a>
                <a href="Gorevli.html" class="list-group-item list-group-item-action">Gorevli</a>
                <a href="Zimmet.html" class="list-group-item list-group-item-action">Zimmet</a>
                <a href="Kiralama.html" class="list-group-item list-group-item-action">Kiralama</a>
                <a href="Ucret.html" class="list-group-item list-group-item-action">Ucret</a>
            </div>
        </div>
    """

@app.route('/<path:path>')
def send_public(path):
    return send_from_directory('public', path)

@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4040, debug=True)
