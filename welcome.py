import tkinter as tk
import menu
import managerlogin
    
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

    manager_button = tk.Button(root, text="Manager Login", font=("Helvetica", 16), command=lambda:open_managerlogin_page(root))
    manager_button.place(relx=0.5, rely=0.7, anchor="center")

    root.mainloop()

# Connects to the menu page
def show_menu(root):
    root.destroy()
    app = menu.CafeMenuApp()
    app.show_menu()

def open_managerlogin_page(root):
    root.destroy()  # Close the login window
    app = managerlogin.ManagerLoginApp()
    app.show_login()
    
if __name__ == "__main__":
    welcome_page()