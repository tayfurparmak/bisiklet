from __main__ import app
from flask import Flask, jsonify, request
import veri
import fonksiyonlar as f

veri.CrateTable("""
    CREATE TABLE IF NOT EXISTS Bisiklet (
        BisikletID INTEGER PRIMARY KEY AUTOINCREMENT,
        Marka TEXT NOT NULL,
        Model TEXT NOT NULL,
        CipNo TEXT NOT NULL,
        TeminTarihi TEXT NOT NULL,
        DigerOzellikler TEXT NOT NULL
        
    )
""")

@app.route('/Bisiklet', methods=["GET"])
def BisikletGetAll():
    db = veri.GetDB()
    cursor = db.cursor()
    query = "SELECT BisikletID, Marka, Model, CipNo, TeminTarihi, DigerOzellikler FROM Bisiklet"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    return f.ResJson(cursor.fetchall(), row_headers)


@app.route("/Bisiklet/<id>", methods=["GET"])
def BisikletGetById(id):
    db = veri.GetDB()
    cursor = db.cursor()
    statement = "SELECT BisikletID, Marka, Model, CipNo, TeminTarihi, DigerOzellikler FROM Bisiklet WHERE BisikletID = ?"
    cursor.execute(statement, [id])
    row_headers = [x[0] for x in cursor.description]
    return f.ResJsonOne(cursor.fetchone(), row_headers)


@app.route("/Bisiklet", methods=["POST"])
def BisikletAdd():
    details = request.get_json()

    Marka = details["Marka"]
    Model = details["Model"]
    CipNo = details["CipNo"]
    TeminTarihi = details["TeminTarihi"]
    DigerOzellikler = details["DigerOzellikler"]
   

    db = veri.GetDB()
    cursor = db.cursor()
    statement = "INSERT INTO Bisiklet(Marka, Model, CipNo, TeminTarihi, DigerOzellikler) VALUES (?,  ?, ?, ?, ?)"
    cursor.execute(statement, [Marka, Model, CipNo, TeminTarihi, DigerOzellikler])
    db.commit()
    return jsonify(True)


@app.route("/Bisiklet", methods=["PUT"])
def BisikletSet():
    details = request.get_json()

    BisikletID = details["BisikletID"]
    Marka = details["Marka"]
    Model = details["Model"]
    CipNo = details["CipNo"]
    TeminTarihi = details["TeminTarihi"]
    DigerOzellikler = details["DigerOzellikler"]
  

    db = veri.GetDB()
    cursor = db.cursor()
    statement = "UPDATE Bisiklet SET Marka = ?, Model = ?, CipNo = ?, TeminTarihi = ?, DigerOzellikler = ? WHERE BisikletID = ?"
    cursor.execute(statement, [Marka, Model, CipNo, TeminTarihi, DigerOzellikler, BisikletID])
    db.commit()
    return jsonify(True)


@app.route("/Bisiklet/<id>", methods=["DELETE"])
def BisikletDelete(id):
    db = veri.GetDB()
    cursor = db.cursor()
    statement = "DELETE FROM Bisiklet WHERE BisikletID = ?"
    cursor.execute(statement, [id])
    db.commit()
    return jsonify(True)
