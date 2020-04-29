import sqlite3
import os

DB_NAME = 'example.db'

if __name__ == '__main__':
	if os.path.isfile(DB_NAME):
		while True:
			ans = input("Database file %s already exists. Want to overwrite it? [y/n]" % DB_NAME)
			if ans.lower() == "y":
				print("Deleting %s and recreating it" % DB_NAME)
				os.remove(DB_NAME)
				break
			elif ans.lower() == "n":
				print("Exiting...")
				exit(0)
			else:
				print("Sorry, I don't understand that command")

	conn = sqlite3.connect('example.db')
	c = conn.cursor()

	c.execute(
	            "CREATE TABLE IF NOT EXISTS 'users' ("
	            + "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
	            + "username VARCHAR NOT NULL,"
	            + "password_hash VARCHAR NOT NULL"
	            + ");"
	        )
	conn.commit()

	print("Database created")