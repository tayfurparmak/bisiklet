from __main__ import app
from flask import Flask, jsonify, request
import veri
import fonksiyonlar as f

veri.CrateTable("""
    CREATE TABLE IF NOT EXISTS Istasyon (
        IstasyonID INTEGER PRIMARY KEY AUTOINCREMENT,
        IstasyonAdi TEXT NOT NULL,
        IstasyonKodu TEXT NOT NULL,
        Mahalle TEXT NOT NULL,
        Sokak TEXT NOT NULL
      


    )
""")

@app.route('/Istasyon', methods=["GET"])
def IstasyonGetAll():
    db = veri.GetDB()
    cursor = db.cursor()
    query = "SELECT IstasyonID, IstasyonAdi, IstasyonKodu, Mahalle, Sokak FROM Istasyon"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    return f.ResJson(cursor.fetchall(), row_headers)


@app.route("/Istasyon/<id>", methods=["GET"])
def IstasyonGetById(id):
    db = veri.GetDB()
    cursor = db.cursor()
    statement = "SELECT IstasyonID, IstasyonAdi, IstasyonKodu, Mahalle, Sokak FROM Istasyon WHERE IstasyonID = ?"
    cursor.execute(statement, [id])
    row_headers = [x[0] for x in cursor.description]
    return f.ResJsonOne(cursor.fetchone(), row_headers)


@app.route("/Istasyon", methods=["POST"])
def IstasyonAdd():
    details = request.get_json()

    IstasyonAdi = details["IstasyonAdi"]
    IstasyonKodu = details["IstasyonKodu"]
    Mahalle = details["Mahalle"]
    Sokak = details["Sokak"]

    db = veri.GetDB()
    cursor = db.cursor()
    statement = "INSERT INTO Istasyon(IstasyonAdi, IstasyonKodu, Mahalle, Sokak) VALUES ( ?, ?,?, ?)"
    cursor.execute(statement, [IstasyonAdi, IstasyonKodu, Mahalle, Sokak])
    db.commit()
    return jsonify(True)


@app.route("/Istasyon", methods=["PUT"])
def IstasyonSet():
    details = request.get_json()

    IstasyonID = details["IstasyonID"]
    IstasyonAdi = details["IstasyonAdi"]
    IstasyonKodu = details["IstasyonKodu"]
    Mahalle = details["Mahalle"]
    Sokak = details["Sokak"]


    db = veri.GetDB()
    cursor = db.cursor()
    statement = "UPDATE Istasyon SET IstasyonAdi = ?, IstasyonKodu = ?, Mahalle = ?, Sokak = ? WHERE IstasyonID = ?"
    cursor.execute(statement, [IstasyonAdi, IstasyonKodu, Mahalle, Sokak, IstasyonID])
    db.commit()
    return jsonify(True)


@app.route("/Istasyon/<id>", methods=["DELETE"])
def IstasyonDelete(id):
    db = veri.GetDB()
    cursor = db.cursor()
    statement = "DELETE FROM Istasyon WHERE IstasyonID = ?"
    cursor.execute(statement, [id])
    db.commit()
    return jsonify(True)
