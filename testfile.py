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

def submit_order():
    table_number = entry_table_number.get()
    item_name = entry_item_name.get()
    quantity = entry_quantity.get()

    # Insert order into orders table
    cursor.execute("INSERT INTO orders (table_number) VALUES (%s)", (table_number,))
    connection.commit()

    # Get the order_id of the newly inserted order
    order_id = cursor.lastrowid

    # Insert items into order_items table
    cursor.execute("INSERT INTO order_items (order_id, item_name, quantity, price) VALUES (%s, %s, %s, %s)",
                   (order_id, item_name, quantity, 10.99))  # Replace 10.99 with the actual price
    connection.commit()

    clear_entries()

def clear_entries():
    entry_table_number.delete(0, tk.END)
    entry_item_name.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)

# Set up the main window
frm = tk.Tk()
frm.geometry('400x300')
frm.title('Customer Order Form')

# Labels and Entry widgets
label_table_number = tk.Label(frm, text='Table Number:')
label_table_number.grid(row=0, column=0, padx=10, pady=10)
entry_table_number = tk.Entry(frm)
entry_table_number.grid(row=0, column=1, padx=10, pady=10)

label_item_name = tk.Label(frm, text='Item Name:')
label_item_name.grid(row=1, column=0, padx=10, pady=10)
entry_item_name = tk.Entry(frm)
entry_item_name.grid(row=1, column=1, padx=10, pady=10)

label_quantity = tk.Label(frm, text='Quantity:')
label_quantity.grid(row=2, column=0, padx=10, pady=10)
entry_quantity = tk.Entry(frm)
entry_quantity.grid(row=2, column=1, padx=10, pady=10)

# Button to submit order
btn_submit = ttk.Button(frm, text='Submit Order', command=submit_order)
btn_submit.grid(row=3, column=0, columnspan=2, pady=10)

# Start the Tkinter main loop
frm.mainloop()

# Don't forget to close the database connection when the application exits
close_connection(connection)
