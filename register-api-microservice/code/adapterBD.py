import mysql.connector
from flask import jsonify
import os

your_db_host = os.getenv('YOUR_DB_HOST')
your_db_user = os.getenv('YOUR_DB_USER')
your_db_pass = os.getenv('YOUR_DB_PASS')
your_db = os.getenv('YOUR_DB')

mydb = mysql.connector.connect(
  host=your_db_host,
  user=your_db_user,
  password=your_db_pass,
  database=your_db
)

mycursor = mydb.cursor(buffered=True)

#registrar usuario nuevo en la bd de nuestro operador
def addnewUser(id_num, password, id_type, name, address, email, telephone, bool_emp, operatorID, operatorName):
    print(id_num)
    temp = False
    sql = "INSERT INTO carpeta_operador (id, id_type, name, address, email, telephone, bool_emp, operatorID, operatorName) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (id_num, id_type, name, address, email, telephone, bool_emp, operatorID, operatorName)
    mycursor.execute(sql, val)
    mydb.commit()
    temp = True
    return temp

#consultar la existencia de un usuario en la bd de nuestro operador
def consultarUser(user):
    sql = "SELECT id FROM `carpeta_operador`"
    mycursor.execute(sql)
    res = mycursor.fetchall()
    temp = False
    for x in res:

        if user in x:
            temp = True
    return temp

def loginUser(user, password):
    sql = "SELECT id FROM `carpeta_operador`"
    mycursor.execute(sql)
    res = mycursor.fetchall()
    temp = False
    for x in res:
        if user in x:
            temp = True
    
    sql= "SELECT password FROM `carpeta_operador`"
    mycursor.execute(sql)
    res = mycursor.fetchall()
    for x in res:
        if password in x:
            temp = True
        else:
            temp = False
    return temp

    # mycursor.execute(sql,val)
    # mydb.commit()






# mycursor.execute("SHOW DATABASES")
# sql = "INSERT INTO citizen (id, id_type, name, address, email, telephone, bool_emp, operatorID, operatorName) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
# val = (4598762454, "Cedula", "Carlos Andres Caro", "Cra 54 # 45 -67", "caro@mymail.com", 3183249781, 1, 1, "Operador Ciudadano")
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, 'Record inserted')

