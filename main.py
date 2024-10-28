import tkinter as tk
from tkinter import simpledialog, messagebox
import gui
from user_authentification import register_user, login_user

def show_login():
    # Create a temporary login window instead of using the main `root`
    login_window = tk.Tk()
    login_window.withdraw()  # Hide the main window initially

    while True:
        action = simpledialog.askstring("Login or Register", "Type 'login' to log in or 'register' to register:", parent=login_window)
        
        if action == "login":
            username = simpledialog.askstring("Login", "Username:", parent=login_window)
            password = simpledialog.askstring("Login", "Password:", show="*", parent=login_window)
            if login_user(username, password):
                messagebox.showinfo("Login Success", "Welcome to the Inventory Management System!", parent=login_window)
                login_window.destroy()  # Close the login window on successful login
                gui.root.deiconify()  # Show the main GUI window
                gui.root.mainloop()  # Start the main loop for the GUI
                break
            else:
                messagebox.showerror("Login Failed", "Incorrect username or password. Try again.", parent=login_window)
        
        elif action == "register":
            username = simpledialog.askstring("Register", "Choose a username:", parent=login_window)
            password = simpledialog.askstring("Register", "Choose a password:", show="*", parent=login_window)
            if register_user(username, password):
                messagebox.showinfo("Registration Success", "User registered successfully! Please log in.", parent=login_window)
            else:
                messagebox.showerror("Registration Failed", "Username already exists. Choose a different username.", parent=login_window)

if __name__ == "__main__":
    show_login()
