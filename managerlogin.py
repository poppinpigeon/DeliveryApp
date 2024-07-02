import tkinter as tk
from tkinter import messagebox
import manager

class ManagerLoginApp:
    def __init__(self, master=None):
        if master is None:
            self.root = tk.Tk()
        else:
            self.root = master
        
        #self.root = root
        self.root.title("Manager Login")
        self.root.geometry("300x200")

        tk.Label(self.root, text="Username:").pack(pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        tk.Label(self.root, text="Password:").pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        login_button = tk.Button(self.root, text="Login", command=self.validate_login)
        login_button.pack(pady=20)

    def validate_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Using hardcoded credentials
        if username == "admin" and password == "password":
            messagebox.showinfo("Login", "Login Successful!")
            self.open_manager_page()
        else:
            messagebox.showerror("Login", "Invalid username or password")

    def open_manager_page(self):
        self.root.destroy()  # Close the login window
        app = manager.OrderManagerApp()
        app.show_manager()
    
    def show_login(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = ManagerLoginApp(root)
    app.show_login()
