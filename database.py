import sqlite3

def connect():
    return sqlite3.connect('inventory.db')

def setup_database():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS items (
                        item_id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        price REAL NOT NULL,
                        quantity INTEGER NOT NULL
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                        transaction_id INTEGER PRIMARY KEY,
                        item_id INTEGER,
                        date TEXT,
                        type TEXT,
                        quantity INTEGER,
                        FOREIGN KEY(item_id) REFERENCES items(item_id)
                    )''')
    conn.commit()
    conn.close()

setup_database()  # Initialize the database tables if they don’t exist
