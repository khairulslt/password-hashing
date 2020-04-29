from setup_db import DB_NAME
import sqlite3
import hashlib


def is_username_available(username):
	conn = sqlite3.connect(DB_NAME)
	c = conn.cursor()

	res = c.execute("""
	            SELECT *
	            FROM users
	            WHERE
	            	username = ?
	        """, (username,))
	return res


def add_user(username, password):
	conn = sqlite3.connect(DB_NAME)
	c = conn.cursor()

	password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

	c.execute("""
		INSERT INTO
		    users (username, password_hash)
		VALUES
		    (?, ?)
	""", (username, password_hash))
	conn.commit()


if __name__ == '__main__':
	print("Let's add some users!")

	while True:
		username = input("username: ")

		if is_username_available(username):
			print("Username is available!")
			break
		else:
			print("Username is unavailable, choose another username!")

	password = input("password: ")

	add_user(username, password)
	print("Added username: %s to the database" % username,)