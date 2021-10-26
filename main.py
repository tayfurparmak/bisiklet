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
        <div><a href="Bisiklet.html">Bisiklet</a></div>
        <div><a href="Kisi.html">Kisi</a></div>
        <div><a href="Istasyon.html">Istasyon</a></div>
        <div><a href="Gorevli.html">Gorevli</a></div>
        <div><a href="Zimmet.html">Zimmet</a></div>
        <div><a href="Kiralama.html">Kiralama</a></div>
        <div><a href="Ucret.html">Ucret</a></div> 
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
