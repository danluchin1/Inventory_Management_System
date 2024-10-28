import datetime
from database import connect

def update_stock(item_id, quantity, transaction_type):
    conn = connect()
    cursor = conn.cursor()
    
    # Fetch current stock
    cursor.execute('SELECT quantity FROM items WHERE item_id=?', (item_id,))
    current_quantity = cursor.fetchone()[0]
    
    # Update quantity based on transaction type
    if transaction_type == 'sale':
        new_quantity = current_quantity - quantity
    elif transaction_type == 'purchase':
        new_quantity = current_quantity + quantity
    
    cursor.execute('UPDATE items SET quantity=? WHERE item_id=?', (new_quantity, item_id))
    
    # Log the transaction
    transaction_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('INSERT INTO transactions (item_id, date, type, quantity) VALUES (?, ?, ?, ?)', 
                   (item_id, transaction_date, transaction_type, quantity))
    
    conn.commit()
    conn.close()
