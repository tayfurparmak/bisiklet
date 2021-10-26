from __main__ import app
from flask import Flask, jsonify, request
import veri
import fonksiyonlar as f

veri.CrateTable("""
    CREATE TABLE IF NOT EXISTS Gorevli (
        GorevliID INTEGER PRIMARY KEY AUTOINCREMENT,
        TcKimlikNo TEXT NOT NULL,
        Adi TEXT NOT NULL,
        Soyadi TEXT NOT NULL,
        Gorevi TEXT NOT NULL,
        GorevYeri TEXT NOT NULL
    


    )
""")

@app.route('/Gorevli', methods=["GET"])
def GorevliGetAll():
    db = veri.GetDB()
    cursor = db.cursor()
    query = "SELECT GorevliID, TcKimlikNo, Adi, Soyadi, Gorevi, GorevYeri FROM Gorevli"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    return f.ResJson(cursor.fetchall(), row_headers)


@app.route("/Gorevli/<id>", methods=["GET"])
def GorevliGetById(id):
    db = veri.GetDB()
    cursor = db.cursor()
    statement = "SELECT GorevliID, TcKimlikNo, Adi, Soyadi, Gorevi, GorevYeri FROM Gorevli WHERE GorevliID = ?"
    cursor.execute(statement, [id])
    row_headers = [x[0] for x in cursor.description]
    return f.ResJsonOne(cursor.fetchone(), row_headers)


@app.route("/Gorevli", methods=["POST"])
def GorevliAdd():
    details = request.get_json()

    TcKimlikNo = details["TcKimlikNo"]
    Adi = details["Adi"]
    Soyadi = details["Soyadi"]
    Gorevi = details["Gorevi"]
    GorevYeri = details["GorevYeri"]
  
    db = veri.GetDB()
    cursor = db.cursor()
    statement = "INSERT INTO Gorevli(TcKimlikNo, Adi, Soyadi, Gorevi, GorevYeri) VALUES ( ?, ?, ?,?, ?)"
    cursor.execute(statement, [TcKimlikNo, Adi, Soyadi, Gorevi, GorevYeri])
    db.commit()
    return jsonify(True)


@app.route("/Gorevli", methods=["PUT"])
def GorevliSet():
    details = request.get_json()

    GorevliID = details["GorevliID"]
    TcKimlikNo = details["TcKimlikNo"]
    Adi = details["Adi"]
    Soyadi = details["Soyadi"]
    Gorevi = details["Gorevi"]
    GorevYeri = details["GorevYeri"]
  


    db = veri.GetDB()
    cursor = db.cursor()
    statement = "UPDATE Gorevli SET TcKimlikNo = ?, Adi = ?, Soyadi = ?, Gorevi = ?, GorevYeri = ?   WHERE GorevliID = ?"
    cursor.execute(statement, [TcKimlikNo, Adi, Soyadi, Gorevi, GorevYeri, GorevliID])
    db.commit()
    return jsonify(True)


@app.route("/Gorevli/<id>", methods=["DELETE"])
def GorevliDelete(id):
    db = veri.GetDB()
    cursor = db.cursor()
    statement = "DELETE FROM Gorevli WHERE GorevliID = ?"
    cursor.execute(statement, [id])
    db.commit()
    return jsonify(True)
