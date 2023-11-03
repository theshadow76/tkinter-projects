import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="lagunaVerde03",
    database="sys"
)
cursor = db.cursor()
cursor.execute("CREATE TABLE People (Name varchar(50), Age int, City varchar(50))")