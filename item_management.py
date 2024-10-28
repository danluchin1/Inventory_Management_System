from database import connect

def add_item(name, price, quantity):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO items (name, price, quantity) VALUES (?, ?, ?)', (name, price, quantity))
    conn.commit()
    conn.close()

def update_item(item_id, name, price, quantity):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('UPDATE items SET name=?, price=?, quantity=? WHERE item_id=?', (name, price, quantity, item_id))
    conn.commit()
    conn.close()

def delete_item(item_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM items WHERE item_id=?', (item_id,))
    conn.commit()
    conn.close()

def view_items():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM items')
    items = cursor.fetchall()
    conn.close()
    return items
