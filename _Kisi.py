from __main__ import app
from flask import Flask, jsonify, request
import veri
import fonksiyonlar as f

veri.CrateTable("""
    CREATE TABLE IF NOT EXISTS Kisi (
        KisiID INTEGER PRIMARY KEY AUTOINCREMENT,
        TcKimlikNo TEXT NOT NULL,
        Adi TEXT NOT NULL,
        Soyadi TEXT NOT NULL,
        BabaAdi TEXT NOT NULL,
        DogumYeri TEXT NOT NULL,
        DogumTarihi TEXT NOT NULL,
        IkahmetkahAdresi TEXT NOT NULL


    )
""")

@app.route('/Kisi', methods=["GET"])
def KisiGetAll():
    db = veri.GetDB()
    cursor = db.cursor()
    query = "SELECT KisiID, TcKimlikNo, Adi, Soyadi, BabaAdi, DogumYeri, DogumTarihi, IkahmetkahAdresi FROM Kisi"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    return f.ResJson(cursor.fetchall(), row_headers)


@app.route("/Kisi/<id>", methods=["GET"])
def KisiGetById(id):
    db = veri.GetDB()
    cursor = db.cursor()
    statement = "SELECT KisiID, TcKimlikNo, Adi, Soyadi, BabaAdi, DogumYeri,DogumTarihi,IkahmetkahAdresi FROM Kisi WHERE KisiID = ?"
    cursor.execute(statement, [id])
    row_headers = [x[0] for x in cursor.description]
    return f.ResJsonOne(cursor.fetchone(), row_headers)


@app.route("/Kisi", methods=["POST"])
def KisiAdd():
    details = request.get_json()

    TcKimlikNo = details["TcKimlikNo"]
    Adi = details["Adi"]
    Soyadi = details["Soyadi"]
    BabaAdi = details["BabaAdi"]
    DogumYeri = details["DogumYeri"]
    DogumTarihi = details["DogumTarihi"]
    IkahmetkahAdresi = details["IkahmetkahAdresi"]

    db = veri.GetDB()
    cursor = db.cursor()
    statement = "INSERT INTO Kisi(TcKimlikNo, Adi, Soyadi, BabaAdi, DogumYeri, DogumTarihi, IkahmetkahAdresi) VALUES (?,  ?, ?, ?, ?, ?, ?)"
    cursor.execute(statement, [TcKimlikNo, Adi, Soyadi, BabaAdi, DogumYeri, DogumTarihi, IkahmetkahAdresi])
    db.commit()
    return jsonify(True)


@app.route("/Kisi", methods=["PUT"])
def KisiSet():
    details = request.get_json()

    KisiID = details["KisiID"]
    TcKimlikNo = details["TcKimlikNo"]
    Adi = details["Adi"]
    Soyadi = details["Soyadi"]
    BabaAdi = details["BabaAdi"]
    DogumYeri = details["DogumYeri"]
    DogumTarihi = details["DogumTarihi"]
    IkahmetkahAdresi = details["IkahmetkahAdresi"]


    db = veri.GetDB()
    cursor = db.cursor()
    statement = "UPDATE Kisi SET TcKimlikNo = ?, Adi = ?, Soyadi = ?, BabaAdi = ?, DogumYeri = ? ,DogumTarihi = ? , IkahmetkahAdresi = ?  WHERE KisiID = ?"
    cursor.execute(statement, [TcKimlikNo, Adi, Soyadi, BabaAdi, DogumYeri,DogumTarihi,IkahmetkahAdresi, KisiID])
    db.commit()
    return jsonify(True)


@app.route("/Kisi/<id>", methods=["DELETE"])
def KisiDelete(id):
    db = veri.GetDB()
    cursor = db.cursor()
    statement = "DELETE FROM Kisi WHERE KisiID = ?"
    cursor.execute(statement, [id])
    db.commit()
    return jsonify(True)
