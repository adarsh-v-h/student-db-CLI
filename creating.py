import sqlite3
connect = sqlite3.connect('Database.db')
cursor = connect.cursor()
cursor.execute("""CREATE TABLE students(
			Full_name TEXT NOT NULL,
			email TEXT NOT NULL UNIQUE,
			password TEXT NOT NULL)

""")
connect.commit()
connect.close()