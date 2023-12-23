import tkinter as tk
from tkinter import ttk, messagebox
from ConectDB import connect, close_connection

# Connect to the database
connection = connect()

# Check if the connection is successful
if connection is None:
    print("Error: Unable to connect to the database.")
    exit()

cursor = connection.cursor()


# Function to retrieve order details for a specific order
def get_order_details(order_id):
    cursor.execute("SELECT user_id, table_number FROM orders WHERE order_id = %s", (order_id,))
    order_info = cursor.fetchone()

    if order_info:
        user_id, table_number = order_info
        order_items = get_order_items(order_id)
        total_price = sum(quantity * price for _, quantity, price in order_items)

        return {
            "user_id": user_id,
            "table_number": table_number,
            "order_items": order_items,
            "total_price": total_price
        }
    else:
        return None

# Function to display bill details in a new window
def print_bill(order_id):
    order_details = get_order_details(order_id)

    if order_details:
        bill_window = tk.Toplevel(frm)
        bill_window.title("Bill Details")

        tk.Label(bill_window, text=f"Order ID: {order_id}").pack()
        tk.Label(bill_window, text=f"User ID: {order_details['user_id']}").pack()
        tk.Label(bill_window, text=f"Table Number: {order_details['table_number']}").pack()

        tk.Label(bill_window, text="Order Items:").pack()
        for item in order_details["order_items"]:
            item_name, quantity, price = item
            tk.Label(bill_window, text=f"  {item_name} - Quantity: {quantity} - Price: {price}").pack()

        tk.Label(bill_window, text=f"Total Price: {order_details['total_price']}").pack()

        # Add an entry for cash received
        cash_entry_label = tk.Label(bill_window, text="Enter Cash Received:")
        cash_entry_label.pack()

        cash_entry = tk.Entry(bill_window)
        cash_entry.pack()

        # Function to calculate change and show it
        def calculate_change():
            try:
                cash_received = float(cash_entry.get())
                total_price = float(order_details['total_price'])  # Convert total_price to float
                change = cash_received - total_price

                # Insert data into the bills table
                insert_bill_data(order_id, total_price)

                tk.messagebox.showinfo("Change", f"Change: {change:.2f}")
                bill_window.destroy()  # Close the current order window
                display_all_orders()

            except ValueError:
                tk.messagebox.showerror("Error", "Invalid input for cash received.")

        # Add a button to calculate change
        calculate_button = ttk.Button(bill_window, text="Calculate Change", command=calculate_change)
        calculate_button.pack()

        # Add a button to close the current order window without calculating change
        close_button = ttk.Button(bill_window, text="Close", command=bill_window.destroy)
        close_button.pack()

    else:
        tk.messagebox.showinfo("Error", "Order not found.")

# Function to insert data into the bills table
def insert_bill_data(order_id, total_amount):
    cursor.execute("INSERT INTO bills (order_id, total_amount, payment_status) VALUES (%s, %s, %s)",
                   (order_id, total_amount, 'Paid'))
    connection.commit()

# Function to retrieve order items for a specific order
def get_order_items(order_id):
    cursor.execute("SELECT item_name, quantity, price FROM order_items WHERE order_id = %s", (order_id,))
    order_items = cursor.fetchall()
    return order_items

# Function to retrieve all orders from the database
def get_all_orders():
    cursor.execute("SELECT * FROM orders")
    all_orders = cursor.fetchall()
    return all_orders

# Function to display all orders and details in the Tkinter window
def display_all_orders():
    for widget in frm.winfo_children():
        widget.destroy()

    all_orders = get_all_orders()

    if not all_orders:
        label = tk.Label(frm, text="No orders found.")
        label.pack()
    else:
        for order in all_orders:
            order_id, _, table_number, _, _ = order

            # Check if the order has a corresponding bill with payment status 'Unpaid'
            cursor.execute("SELECT * FROM bills WHERE order_id = %s AND payment_status = %s", (order_id, 'Unpaid'))
            unpaid_bill = cursor.fetchone()

            if unpaid_bill:
                label = tk.Label(frm, text=f"Table Number: {table_number}, Order ID: {order_id}")
                label.pack()

                order_items = get_order_items(order_id)

                if not order_items:
                    label = tk.Label(frm, text="No items found for this order.")
                    label.pack()
                else:
                    total_price = 0

                    for item in order_items:
                        item_name, quantity, price = item
                        total_price += quantity * price

                        label = tk.Label(frm, text=f"Item: {item_name}, Quantity: {quantity}, Price: {price}")
                        label.pack()

                    label = tk.Label(frm, text=f"Total Price: {total_price}")
                    label.pack()

                    # Add a button to print the bill
                    print_bill_button = ttk.Button(frm, text="Print Bill", command=lambda order_id=order_id: print_bill(order_id))
                    print_bill_button.pack()

# Set up the main window
frm = tk.Tk()
frm.geometry('800x600')
frm.title('All Orders and Details')

# Display all orders and details
display_all_orders()

# Start the Tkinter main loop
frm.mainloop()

# Don't forget to close the database connection when the application exits
close_connection(connection)
