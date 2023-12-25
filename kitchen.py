import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ConectDB import connect, close_connection




connection = connect()
cursor = connection.cursor()

def get_orders():
    connection = connect()
    if connection is None:
        return []

    cursor = connection.cursor()
    cursor.execute("SELECT orders.order_id, orders.table_number, orders.order_date, orders.status, order_items.item_name, order_items.quantity FROM orders INNER JOIN order_items ON orders.order_id = order_items.order_id WHERE orders.status = 'Pending'")
    orders = cursor.fetchall()
    close_connection(connection)
    return orders

def update_order_status(order_id):
    connection = connect()
    if connection is None:
        return

    cursor = connection.cursor()
    cursor.execute("UPDATE orders SET status = 'Completed' WHERE order_id = %s", (order_id,))
    connection.commit()
    close_connection(connection)
    display_orders()

def on_tree_click(event):
    item = tree.selection()[0]
    order_id = tree.item(item, "values")[0]
    update_order_status(order_id)

def display_orders():
    for item in tree.get_children():
        tree.delete(item)

    orders = get_orders()

    for order in orders:
        order_id, table_number, order_date, status, item_name, quantity = order

        tree.insert("", "end", values=(order_id, table_number, status, item_name, quantity))

# Set up the main window
frm = tk.Tk()
frm.state('zoomed')
frm.geometry('1166x718')
frm.title('Kitchen Orders')

# Create a Treeview widget
columns = ("Order ID", "Table", "Status", "Item", "Quantity")
tree = ttk.Treeview(frm, columns=columns, show="headings", height=15)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)

tree.pack()

# Display orders initially
display_orders()

# Bind the click event to the on_tree_click function
tree.bind("<ButtonRelease-1>", on_tree_click)

frm.resizable(0, 0)
frm.state('zoomed')

# Add your background image code here

# Add any additional UI elements if needed

# Start the Tkinter main loop
frm.mainloop()
