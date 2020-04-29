# Understanding Login Authentication

I created 3 python scripts to understand auth.


Most modern web apps do not store passwords in the form of plaintext in their databases. Passwords are usually hashed upon creation by a hash function (this repo uses SHA-256) and then stored in a database. The login function then hashes the input password and compares it with the password hash in the database.

## Usage:
- create sqlite db `(example.db)` in directory: `python3 setup_db.py`
- add username/pw to db: `python3 add_users.py`
- login using credentials, password stored as 256-bit hash: `python3 login.py`
