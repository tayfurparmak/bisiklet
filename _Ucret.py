from __main__ import app
from flask import Flask, jsonify, request
import veri
import fonksiyonlar as f

veri.CrateTable("""
    CREATE TABLE IF NOT EXISTS Ucret (
        UcretID INTEGER PRIMARY KEY AUTOINCREMENT,
        UcretBaslangicTarihi TEXT NOT NULL,
        SaatlikUcret TEXT NOT NULL
        
       


    )
""")

@app.route('/Ucret', methods=["GET"])
def UcretGetAll():
    db = veri.GetDB()
    cursor = db.cursor()
    query = "SELECT UcretID, UcretBaslangicTarihi, SaatlikUcret FROM Ucret"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    return f.ResJson(cursor.fetchall(), row_headers)


@app.route("/Ucret/<id>", methods=["GET"])
def UcretGetById(id):
    db = veri.GetDB()
    cursor = db.cursor()
    statement = "SELECT UcretID, UcretBaslangicTarihi, SaatlikUcret FROM Ucret WHERE UcretID = ?"
    cursor.execute(statement, [id])
    row_headers = [x[0] for x in cursor.description]
    return f.ResJsonOne(cursor.fetchone(), row_headers)


@app.route("/Ucret", methods=["POST"])
def UcretAdd():
    details = request.get_json()

    UcretBaslangicTarihi = details["UcretBaslangicTarihi"]
    SaatlikUcret = details["SaatlikUcret"]
  
  
    db = veri.GetDB()
    cursor = db.cursor()
    statement = "INSERT INTO Ucret(UcretBaslangicTarihi, SaatlikUcret) VALUES ( ?, ?)"
    cursor.execute(statement, [UcretBaslangicTarihi, SaatlikUcret])
    db.commit()
    return jsonify(True)


@app.route("/Ucret", methods=["PUT"])
def UcretSet():
    details = request.get_json()

    UcretID = details["UcretID"]
    UcretBaslangicTarihi = details["UcretBaslangicTarihi"]
    SaatlikUcret = details["SaatlikUcret"]
 


    db = veri.GetDB()
    cursor = db.cursor()
    statement = "UPDATE Ucret SET UcretBaslangicTarihi = ?, SaatlikUcret = ? WHERE UcretID = ?"
    cursor.execute(statement, [UcretBaslangicTarihi, SaatlikUcret, UcretID])
    db.commit()
    return jsonify(True)


@app.route("/Ucret/<id>", methods=["DELETE"])
def UcretDelete(id):
    db = veri.GetDB()
    cursor = db.cursor()
    statement = "DELETE FROM Ucret WHERE UcretID = ?"
    cursor.execute(statement, [id])
    db.commit()
    return jsonify(True)
