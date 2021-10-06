import sqlite3
connection = sqlite3.connect('users.db')
cursor = connection.cursor()

cursor.execute('''
            CREATE TABLE passwords (username TEXT, password TEXT)
    ''')
connection.commit()
connection.close()