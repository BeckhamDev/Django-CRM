import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost', 
    user = 'root',
    passwd = 'rootroot'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE website_DB")

print("Deu Bom mlk!")