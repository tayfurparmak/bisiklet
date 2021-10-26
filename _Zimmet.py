from __main__ import app
from flask import Flask, jsonify, request
import veri
import fonksiyonlar as f

veri.CrateTable("""
    CREATE TABLE IF NOT EXISTS Zimmet (
        ZimmetID INTEGER PRIMARY KEY AUTOINCREMENT,
        IstasyonID TEXT NOT NULL,
        BisikletID TEXT NOT NULL,
        IstasyonaGelisTarihi TEXT NOT NULL,
        IstasyonaGelisSaati TEXT NOT NULL,
        TeslimAlanGorevliID TEXT NOT NULL
       


    )
""")

@app.route('/Zimmet', methods=["GET"])
def ZimmetGetAll():
    db = veri.GetDB()
    cursor = db.cursor()
    query = "SELECT ZimmetID, IstasyonID, BisikletID, IstasyonaGelisTarihi, IstasyonaGelisSaati, TeslimAlanGorevliID FROM Zimmet"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    return f.ResJson(cursor.fetchall(), row_headers)


@app.route("/Zimmet/<id>", methods=["GET"])
def ZimmetGetById(id):
    db = veri.GetDB()
    cursor = db.cursor()
    statement = "SELECT ZimmetID, IstasyonID, BisikletID, IstasyonaGelisTarihi, IstasyonaGelisSaati, TeslimAlanGorevliID FROM Zimmet WHERE ZimmetID = ?"
    cursor.execute(statement, [id])
    row_headers = [x[0] for x in cursor.description]
    return f.ResJsonOne(cursor.fetchone(), row_headers)


@app.route("/Zimmet", methods=["POST"])
def ZimmetAdd():
    details = request.get_json()

    IstasyonID = details["IstasyonID"]
    BisikletID = details["BisikletID"]
    IstasyonaGelisTarihi = details["IstasyonaGelisTarihi"]
    IstasyonaGelisSaati = details["IstasyonaGelisSaati"]
    TeslimAlanGorevliID = details["TeslimAlanGorevliID"]
   
    db = veri.GetDB()
    cursor = db.cursor()
    statement = "INSERT INTO Zimmet(IstasyonID, BisikletID, IstasyonaGelisTarihi, IstasyonaGelisSaati, TeslimAlanGorevliID) VALUES ( ?, ?, ?,?, ?)"
    cursor.execute(statement, [IstasyonID, BisikletID, IstasyonaGelisTarihi, IstasyonaGelisSaati, TeslimAlanGorevliID])
    db.commit()
    return jsonify(True)


@app.route("/Zimmet", methods=["PUT"])
def ZimmetSet():
    details = request.get_json()

    ZimmetID = details["ZimmetID"]
    IstasyonID = details["IstasyonID"]
    BisikletID = details["BisikletID"]
    IstasyonaGelisTarihi = details["IstasyonaGelisTarihi"]
    IstasyonaGelisSaati = details["IstasyonaGelisSaati"]
    TeslimAlanGorevliID = details["TeslimAlanGorevliID"]
  


    db = veri.GetDB()
    cursor = db.cursor()
    statement = "UPDATE Zimmet SET IstasyonID = ?, BisikletID = ?, IstasyonaGelisTarihi = ?, IstasyonaGelisSaati = ?, TeslimAlanGorevliID = ?   WHERE ZimmetID = ?"
    cursor.execute(statement, [IstasyonID, BisikletID, IstasyonaGelisTarihi, IstasyonaGelisSaati, TeslimAlanGorevliID, ZimmetID])
    db.commit()
    return jsonify(True)


@app.route("/Zimmet/<id>", methods=["DELETE"])
def ZimmetDelete(id):
    db = veri.GetDB()
    cursor = db.cursor()
    statement = "DELETE FROM Zimmet WHERE ZimmetID = ?"
    cursor.execute(statement, [id])
    db.commit()
    return jsonify(True)
