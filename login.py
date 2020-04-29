import hashlib
from setup_db import DB_NAME
import sqlite3


def is_valid_credentials(username, password):
	conn = sqlite3.connect(DB_NAME)
	c = conn.cursor()

	password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

	res = c.execute("""
	    SELECT *
	    FROM users
	    WHERE
	      username = ? AND
	      password_hash = ?
	""", (username, password_hash)).fetchone()

	return res is not None

if __name__ == '__main__':
	username = input("What is your username?\n")
	password = input("What is your password?\n")

	if is_valid_credentials(username, password):
		print("ENTER MY LAIR")
	else:
		print("NOPE")