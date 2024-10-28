import tkinter as tk
from tkinter import messagebox
from item_management import add_item, view_items
from stock_management import update_stock

def add_item_gui():
    name = name_entry.get()
    price = float(price_entry.get())
    quantity = int(quantity_entry.get())
    add_item(name, price, quantity)
    messagebox.showinfo("Success", "Item added successfully!")
    refresh_inventory()

def refresh_inventory():
    inventory_list.delete(0, tk.END)
    items = view_items()
    for item in items:
        inventory_list.insert(tk.END, f"ID: {item[0]}, Name: {item[1]}, Price: {item[2]}, Stock: {item[3]}")

# Initialize main window (but don’t start the main loop yet)
root = tk.Tk()
root.title("Inventory Management System")

# Hide the main window initially; it will be shown after successful login in `main.py`
root.withdraw()

# Create input fields for item details
tk.Label(root, text="Name").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Price").grid(row=1, column=0)
price_entry = tk.Entry(root)
price_entry.grid(row=1, column=1)

tk.Label(root, text="Quantity").grid(row=2, column=0)
quantity_entry = tk.Entry(root)
quantity_entry.grid(row=2, column=1)

# Add button for adding item
add_button = tk.Button(root, text="Add Item", command=add_item_gui)
add_button.grid(row=3, column=0, columnspan=2)

# Inventory list display
inventory_list = tk.Listbox(root, width=50)
inventory_list.grid(row=4, column=0, columnspan=2)

# Refresh inventory list on load
refresh_inventory()
