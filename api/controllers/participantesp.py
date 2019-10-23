from flask import jsonify, request
from bd.db import cnx

class TipoCultivo():
    global cur
    cur = cnx.cursor()
    def list():
        lista = []
        cur.execute("SELECT * FROM cultivos")
        rows = cur.fetchall()
        columns = [i[0] for i in cur.description]
        for row in rows:
            registro = zip(columns,row)
            json = dict(registro)
            lista.append(json)
        return jsonify(lista)
        cnx.close
        
    def create(body):
        data = (body['codigo'],body['latitud'],body['longitud'], body['area'],body['producto'])
        sql = "INSERT INTO cultivos(codigo, latitud, longitud, area, producto) VALUES(%s, %s, %s, %s, %s)"
        cur.execute(sql,data)
        cnx.commit()
        return {'estado': "insertado"}, 200
        