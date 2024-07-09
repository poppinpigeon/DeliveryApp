import tkinter as tk
from tkinter import ttk, messagebox
import manageorders
import welcome

# Classes for menu items
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return self.name + " - ¥" + self.price

# Main application class
class CafeMenuApp:
    def __init__(self, master=None):
        if master is None:
            self.root = tk.Tk()
        else:
            self.root = master
        
        #self.master = master
        self.root.title("Cafe Menu")

        # Create main frame that will hold menu and cart
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Sample data organized by sub-categories
        self.menu_categories = {
            "Drinks": {
                "Coffee": [MenuItem("Blend", 400), MenuItem("Café au Lait", 400), MenuItem("Cappuccino", 400)],
                "Tea": [MenuItem("Tea", 400)],
                "Juice": [MenuItem("Juice", 400)]
            },
            "Food": [MenuItem("Toast", 250), MenuItem("Hot Dog", 400), MenuItem("Tuna Sub", 400), MenuItem("Biscotti", 250), MenuItem("Cake", 450)]
        }

        self.cart = []

        # Tabs for categories
        tab_control = ttk.Notebook(main_frame)
        tab_control.pack(side="left", fill="both", expand=True, padx=10)

        # Drinks tab with nested tabs
        drinks_tab = ttk.Frame(tab_control)
        drinks_tab_control = ttk.Notebook(drinks_tab)
        drinks_categories = self.menu_categories["Drinks"]

        for sub_category, items in drinks_categories.items():
            sub_tab = ttk.Frame(drinks_tab_control)
            drinks_tab_control.add(sub_tab, text=sub_category)
            self.build_menu(sub_tab, items)
        drinks_tab_control.pack(expand=1, fill="both")
        tab_control.add(drinks_tab, text="Drinks")

        # Food tab
        food_tab = ttk.Frame(tab_control)
        tab_control.add(food_tab, text="Food")
        self.build_menu(food_tab, self.menu_categories["Food"])

        # Cart frame setup on the right
        self.cart_frame = tk.Frame(main_frame, borderwidth=2, relief="sunken")
        self.cart_frame.pack(side="right", fill="both", padx=10)

        self.cart_label = tk.Label(self.cart_frame, text="My Cart", font=("Arial", 16))
        self.cart_label.pack()

        self.cart_listbox = tk.Listbox(self.cart_frame)
        self.cart_listbox.pack(fill="both", expand=True)

        # Display total price
        self.total_price_label = tk.Label(self.cart_frame, text="Total: 0 Yen")
        self.total_price_label.pack()

        self.delete_button = tk.Button(self.cart_frame, text="Delete Selected", command=self.delete_from_cart)
        self.delete_button.pack()

        self.clear_cart_button = tk.Button(self.cart_frame, text="Clear Cart", command=self.clear_cart)
        self.clear_cart_button.pack()

        self.checkout_button = tk.Button(self.cart_frame, text="Checkout", command=self.open_order_details)
        self.checkout_button.pack()
        
        # in progress!!
        self.back_button = tk.Button(self.cart_frame, text="Back to Main", command=self.back_to_main)
        self.back_button.pack()

        self.update_cart()

    def build_menu(self, parent, items):
        for item in items:
            item_text = f"{item.name} - ¥{item.price}"

            label = tk.Label(parent, text=item_text, padx=10, pady=10)
            label.pack(side="top", fill="x")

            add_button = tk.Button(parent, text="Add", command=lambda i=item: self.add_to_cart(i))
            add_button.pack(side="top")
    
    def back_to_main(self):
        self.root.destroy()
        welcome.welcome_page()

    def add_to_cart(self, item):
        self.cart.append(item)
        self.update_cart()

    def delete_from_cart(self):
        if self.cart_listbox.curselection():
            index = self.cart_listbox.curselection()[0]
            self.cart.pop(index)
            self.update_cart()

    def clear_cart(self):
        self.cart.clear()
        self.update_cart()

    def update_cart(self):
        # Clear the current cart display
        self.cart_listbox.delete(0, tk.END)
        total_price = 0
        for item in self.cart:
            self.cart_listbox.insert(tk.END, f"{item.name} - ¥{item.price}")
            total_price += item.price
        self.total_price_label.config(text=f"Total: ¥{total_price}")

    def open_order_details(self):
        if not self.cart:
            messagebox.showinfo("Empty Cart", "Please add items to your cart before checking out.")
            return
        
        # Create a new top-level window for order details - in progress!!
        order_details_window = tk.Toplevel(self.root)
        order_details_window.title("Order Details")
        order_details_list = tk.Listbox(order_details_window)
        order_details_list.pack(fill="both", expand=True)
        
        total_price = sum(item.price for item in self.cart)
        for item in self.cart:
            order_details_list.insert(tk.END, f"{item.name} - ¥{item.price}")

        total_label = tk.Label(order_details_window, text=f"Total: ¥{total_price}")
        total_label.pack()
        
        proceed_button = tk.Button(order_details_window, text="Proceed to User Info", command=lambda: self.open_user_info(order_details_window, total_price))
        proceed_button.pack()

    def open_user_info(self, order_details_window, total_price):
        order_details_window.destroy()
        
        user_info_window = tk.Toplevel(self.root)
        user_info_window.title("User Information")

        tk.Label(user_info_window, text="Name:").pack(pady=5)
        name_entry = tk.Entry(user_info_window)
        name_entry.pack(pady=5)

        tk.Label(user_info_window, text="Address:").pack(pady=5)
        address_entry = tk.Entry(user_info_window)
        address_entry.pack(pady=5)

        tk.Label(user_info_window, text="Phone Number:").pack(pady=5)
        phone_entry = tk.Entry(user_info_window)
        phone_entry.pack(pady=5)

        confirm_button = tk.Button(user_info_window, text="Confirm", command=lambda: self.confirm_order(user_info_window, name_entry.get(), address_entry.get(), phone_entry.get(), total_price))
        confirm_button.pack(pady=5)
    
    def confirm_order(self, user_info_window, name, address, phone, total_price):
        user_info = {
            "name": name,
            "address": address,
            "phone": phone,
            "order": [(item.name, item.price) for item in self.cart],
            "total": total_price
        }
        
        if (not user_info["name"]) or (not user_info["address"]) or (not user_info["phone"]):
            messagebox.showinfo("Incomplete Information", f"Please enter all information.")
        else:
            messagebox.showinfo("Order Confirmed", f"Your order has been confirmed!")
            # Save user_info to firebase
            manageorders.addOrder(user_info)
            
            self.cart.clear()
            self.update_cart()
            user_info_window.destroy()
        
    def show_menu(self):
        self.root.mainloop()

# Run program
if __name__ == "__main__":
    app = CafeMenuApp()
    app.show_menu()