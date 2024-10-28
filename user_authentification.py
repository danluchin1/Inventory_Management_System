import sqlite3
import hashlib
from database import connect

def setup_user_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY,
                        username TEXT UNIQUE NOT NULL,
                        password_hash TEXT NOT NULL
                    )''')
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    conn = connect()
    cursor = conn.cursor()
    try:
        password_hash = hash_password(password)
        cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, password_hash))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        conn.close()
        return False  # Username already exists

def login_user(username, password):
    conn = connect()
    cursor = conn.cursor()
    password_hash = hash_password(password)
    cursor.execute('SELECT * FROM users WHERE username=? AND password_hash=?', (username, password_hash))
    user = cursor.fetchone()
    conn.close()
    return user is not None  # Returns True if user is found, False otherwise

# Setup user table when the module is first run
setup_user_table()
