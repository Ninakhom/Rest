import tkinter as tk
from tkinter import ttk
from ConectDB import connect, close_connection

# Connect to the database
connection = connect()

# Check if the connection is successful
if connection is None:
    print("Error: Unable to connect to the database.")
    exit()

cursor = connection.cursor()

# Function to retrieve orders from the database
def get_orders():
    cursor.execute("SELECT orders.order_id, orders.table_number, orders.order_date, orders.status, order_items.item_name, order_items.quantity, order_items.price FROM orders INNER JOIN order_items ON orders.order_id = order_items.order_id WHERE orders.status = 'Pending'")
    orders = cursor.fetchall()
    return orders

# Function to update order status (e.g., mark as "Completed")
def update_order_status(order_id):
    cursor.execute("UPDATE orders SET status = 'Completed' WHERE order_id = %s", (order_id,))
    connection.commit()
    display_orders()

# Function to display orders in the Tkinter window
def display_orders():
    for widget in frm.winfo_children():
        widget.destroy()

    orders = get_orders()

    for order in orders:
        order_id, table_number, order_date, status, item_name, quantity, price = order

        label = tk.Label(frm, text=f"Order ID: {order_id}, Table: {table_number}, Status: {status}")
        label.pack()

        item_label = tk.Label(frm, text=f"Item: {item_name}, Quantity: {quantity}, Price: {price}")
        item_label.pack()

        complete_button = ttk.Button(frm, text="Mark as Completed", command=lambda order_id=order_id: update_order_status(order_id))
        complete_button.pack()

# Set up the main window
frm = tk.Tk()
frm.geometry('800x600')
frm.title('Kitchen Orders')

# Display orders initially
display_orders()

# Start the Tkinter main loop
frm.mainloop()

# Don't forget to close the database connection when the application exits
close_connection(connection)
