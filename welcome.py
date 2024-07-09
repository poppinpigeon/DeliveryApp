import tkinter as tk
import menu
import manager
from tkinter import messagebox
    
def welcome_page():
    root = tk.Tk()
    root.title("Coffee Alpine Welcome Page")
    root.geometry("800x600")

    try:
        image_path = r"alpine_coffee.png"
        background_image = tk.PhotoImage(file=image_path)
    except Exception as e:
        print(f"Error loading image: {e}")

    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    # Add welcome text
    welcome_label = tk.Label(root, text="Welcome to", font=("Helvetica", 36))
    welcome_label.place(relx=0.5, rely=0.2, anchor="center")

    # Add café name
    cafe_name_label = tk.Label(root, text="Alpine Coffee", font=("Helvetica", 48, "bold"))
    cafe_name_label.place(relx=0.5, rely=0.3, anchor="center")

    # Add address
    address_label = tk.Label(root, text="97 Tanaka Monzencho, Sakyo Ward, Kyoto, 606-8225", font=("Helvetica", 20))
    address_label.place(relx=0.5, rely=0.8, anchor="center")

    # Add contact information
    contact_label = tk.Label(root, text="Contact Info: 0757019610 | cafe@delight.com", font=("Helvetica", 18))
    contact_label.place(relx=0.5, rely=0.9, anchor="center")

    # Add menu button
    menu_button = tk.Button(root, text="Go to Menu", font=("Helvetica", 24), command=lambda:show_menu(root))
    menu_button.place(relx=0.5, rely=0.5, anchor="center")

    manager_button = tk.Button(root, text="Manager Login", font=("Helvetica", 16), command=lambda:open_managerlogin(root))
    manager_button.place(relx=0.5, rely=0.7, anchor="center")

    root.mainloop()

# Connects to the menu page
def show_menu(root):
    root.destroy()
    app = menu.CafeMenuApp()
    app.show_menu()

# Create a new top-level window for manager login
def open_managerlogin(root):
    manager_login_window = tk.Toplevel(root)
    manager_login_window.title("Manager Login")
    
    # Username input
    username_label = tk.Label(manager_login_window, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(manager_login_window)
    username_entry.pack()

    # Password input
    password_label = tk.Label(manager_login_window, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(manager_login_window, show="*")
    password_entry.pack()

    # Login button
    login_button = tk.Button(manager_login_window, text="Login", command=lambda:validate_login(root, username_entry, password_entry))
    login_button.pack()

# Validates the username and password from the manager login pop-up
def validate_login(root, username_entry, password_entry):
    username = username_entry.get()
    password = password_entry.get()

    # Uses hardcoded credentials for now
    if username == "admin" and password == "password":
        messagebox.showinfo("Login", "Login Successful!")
        open_manager_page(root)
    else:
        messagebox.showerror("Login", "Invalid username or password")

# Connects to the manager page
def open_manager_page(root):
    root.destroy()  # Close the login window
    app = manager.OrderManagerApp()
    app.show_manager()
    
if __name__ == "__main__":
    welcome_page()