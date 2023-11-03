import sqlite3 as sql
import html as ht

server = sql.Connection(
    database = 'TheShadowTech',
    host = 'localhost',
    user = 'root',
    password = 'lagunaVerde03',
)
server.execute()
print("good to go!")
server.close()