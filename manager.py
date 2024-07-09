import manageorders
import tkinter as tk
from tkinter import messagebox
import welcome

class OrderManagerApp:
    def __init__(self, master=None):
        if master is None:
            self.root = tk.Tk()
        else:
            self.root = master
        
        self.root.title("Manage Orders")
        self.root.geometry("800x600")
        
        # Set scrollbar
        scrollbar = tk.Scrollbar(self.root)
        scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
        
        # Orders List
        self.orders_listbox = tk.Listbox(self.root, yscrollcommand = scrollbar.set)
        self.orders_listbox.pack(fill="both", expand=True)
        scrollbar.config(command = self.orders_listbox.yview)

        # Delete Order Button
        delete_button = tk.Button(self.root, text="Delete Completed Order (Click on ID)", command=self.delete_order)
        delete_button.pack()

        # Refresh Button
        refresh_button = tk.Button(self.root, text="Refresh Orders", command=self.load_orders)
        refresh_button.pack()
        
        # Back to Main Button
        back_button = tk.Button(self.root, text="Back to Main", command=self.back_to_main)
        back_button.pack()

        # Load initial orders
        self.load_orders()

    # Loads user information and order details from Firebase
    def load_orders(self):
        self.orders_listbox.delete(0, tk.END)
        orders = manageorders.db.child("Orders").get()

        if orders:
            for order in orders.each():
                order_str = f"ID: {order.key()}\n   Name: {order.val()["name"]} \n   Address: {order.val()["address"]} \n   Phone: {order.val()["phone"]} \n   Order: {order.val()["order"]} \n   Total: ¥{order.val()["total"]}"
                lines = order_str.split("\n")
                for line in lines:
                    self.orders_listbox.insert(tk.END, line)
    
    # Deletes selected order
    def delete_order(self):
        selected_order = self.orders_listbox.curselection()
        if (not selected_order) or (not (selected_order[0]%6 == 0)):
            messagebox.showwarning("Select Order", "Please select the order ID to delete.")
            return
        
        order_index = selected_order[0]
        order_text = self.orders_listbox.get(order_index)
        order_id = order_text.replace("ID: ", "")

        # Remove order from Firebase
        print(order_id)
        manageorders.db.child("Orders").child(order_id).remove()

        # Update orders listbox
        self.load_orders()
    
    # Connects to the welcome page
    def back_to_main(self):
        self.root.destroy()
        welcome.welcome_page()

    def show_manager(self):
        self.root.mainloop()

# Run the application
if __name__ == "__main__":
    app = OrderManagerApp()
    app.show_manager()