from database import connect

def test_database_connection():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    conn.close()

    assert ('items',) in tables
    assert ('transactions',) in tables
