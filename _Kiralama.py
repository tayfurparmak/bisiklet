from __main__ import app
from flask import Flask, jsonify, request
import veri
import fonksiyonlar as f

veri.CrateTable("""
    CREATE TABLE IF NOT EXISTS Kiralama (
        KiralamaID INTEGER PRIMARY KEY AUTOINCREMENT,
        KisiID TEXT NOT NULL,
        BisikletID TEXT NOT NULL,
        IstasyonID TEXT NOT NULL,
        TeslimTarihi TEXT NOT NULL,
        TeslimSaati TEXT NOT NULL,
        TeslimAlanGorevliID TEXT NOT NULL,
        IadeTarihi TEXT NOT NULL,
        IadeSaati TEXT NOT NULL,
        IadeEdilenIstasyonID TEXT NOT NULL,
        IadeEdilenGorevliID TEXT NOT NULL,
        KiralamaSuresi TEXT NOT NULL,
        KiraUcreti TEXT NOT NULL    

    )
""")

@app.route('/Kiralama', methods=["GET"])
def KiralamaGetAll():
    db = veri.GetDB()
    cursor = db.cursor()
    query = "SELECT KiralamaID, KisiID, BisikletID, IstasyonID, TeslimTarihi, TeslimSaati,TeslimAlanGorevliID,IadeTarihi,IadeSaati,IadeEdilenIstasyonID,IadeEdilenGorevliID,KiralamaSuresi,KiraUcreti FROM Kiralama"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    return f.ResJson(cursor.fetchall(), row_headers)


@app.route("/Kiralama/<id>", methods=["GET"])
def KiralamaGetById(id):
    db = veri.GetDB()
    cursor = db.cursor()
    statement = "SELECT KiralamaID, KisiID, BisikletID, IstasyonID, TeslimTarihi, TeslimSaati,TeslimAlanGorevliID,IadeTarihi,IadeSaati,IadeEdilenIstasyonID,IadeEdilenGorevliID,KiralamaSuresi,KiraUcreti FROM Kiralama WHERE KiralamaID = ?"
    cursor.execute(statement, [id])
    row_headers = [x[0] for x in cursor.description]
    return f.ResJsonOne(cursor.fetchone(), row_headers)


@app.route("/Kiralama", methods=["POST"])
def KiralamaAdd():
    details = request.get_json()

    KisiID = details["KisiID"]
    BisikletID = details["BisikletID"]
    IstasyonID = details["IstasyonID"]
    TeslimTarihi = details["TeslimTarihi"]
    TeslimSaati = details["TeslimSaati"]
    TeslimAlanGorevliID = details["TeslimAlanGorevliID"]
    IadeTarihi = details["IadeTarihi"]
    IadeSaati = details["IadeSaati"]
    IadeEdilenIstasyonID = details["IadeEdilenIstasyonID"]
    IadeEdilenGorevliID = details["IadeEdilenGorevliID"]
    KiralamaSuresi = details["KiralamaSuresi"]
    KiraUcreti = details["KiraUcreti"]
    db = veri.GetDB()
    cursor = db.cursor()
    statement = "INSERT INTO Kiralama(KisiID, BisikletID, IstasyonID, TeslimTarihi, TeslimSaati,TeslimAlanGorevliID,IadeTarihi,IadeSaati,IadeEdilenIstasyonID,IadeEdilenGorevliID,KiralamaSuresi,KiraUcreti) VALUES (?,  ?, ?, ?, ?, ?, ?,?, ?, ?,?, ?)"
    cursor.execute(statement, [KisiID, BisikletID, IstasyonID, TeslimTarihi, TeslimSaati,TeslimAlanGorevliID,IadeTarihi,IadeSaati,IadeEdilenIstasyonID,IadeEdilenGorevliID,KiralamaSuresi,KiraUcreti])
    db.commit()
    return jsonify(True)


@app.route("/Kiralama", methods=["PUT"])
def KiralamaSet():
    details = request.get_json()

    KiralamaID = details["KiralamaID"]
    KisiID = details["KisiID"]
    BisikletID = details["BisikletID"]
    IstasyonID = details["IstasyonID"]
    TeslimTarihi = details["TeslimTarihi"]
    TeslimSaati = details["TeslimSaati"]
    TeslimAlanGorevliID = details["TeslimAlanGorevliID"]
    IadeTarihi = details["IadeTarihi"]
    IadeSaati = details["IadeSaati"]
    IadeEdilenIstasyonID = details["IadeEdilenIstasyonID"]
    IadeEdilenGorevliID = details["IadeEdilenGorevliID"]
    KiralamaSuresi = details["KiralamaSuresi"]
    KiraUcreti = details["KiraUcreti"]

    db = veri.GetDB()
    cursor = db.cursor()
    statement = "UPDATE Kiralama SET KisiID = ?, BisikletID = ?, IstasyonID = ?, TeslimTarihi = ?, TeslimSaati = ? ,TeslimAlanGorevliID = ? , IadeTarihi = ?,IadeSaati = ?,IadeEdilenIstasyonID = ?,IadeEdilenGorevliID = ?,KiralamaSuresi = ?,KiraUcreti = ? WHERE KiralamaID = ?"
    cursor.execute(statement, [KisiID, BisikletID, IstasyonID, TeslimTarihi, TeslimSaati,TeslimAlanGorevliID,IadeTarihi,IadeSaati,IadeEdilenIstasyonID,IadeEdilenGorevliID,KiralamaSuresi,KiraUcreti, KiralamaID])
    db.commit()
    return jsonify(True)


@app.route("/Kiralama/<id>", methods=["DELETE"])
def KiralamaDelete(id):
    db = veri.GetDB()
    cursor = db.cursor()
    statement = "DELETE FROM Kiralama WHERE KiralamaID = ?"
    cursor.execute(statement, [id])
    db.commit()
    return jsonify(True)
