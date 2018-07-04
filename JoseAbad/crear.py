import sqlite3

conexion=sqlite3.connect('database.db')
cursor=conexion.cursor()

cursor.execute('''CREATE TABLE Persona
					(id integer primary key autoincrement,
					nombre text,
					apellido text)''')

conexion.close()