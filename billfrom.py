from code import interact
import tkinter as tk
from tkinter import messagebox
from ConectDB import connect, close_connection
import os
connection = connect()
cursor = connection.cursor()
# Check if the connection is successful
if connection is None:
    print("Error: Unable to connect to the database.")
    exit()

cursor = connection.cursor()

# Create the window
window = tk.Tk()
window.title("Bill")
window.geometry("600x400")

# Create the labels
tk.Label(window, text="Order ID:").grid(row=0, column=0)
tk.Label(window, text="Table Number:").grid(row=1, column=0)
tk.Label(window, text="Customer Name:").grid(row=2, column=0)
tk.Label(window, text="Date:").grid(row=3, column=0)
tk.Label(window, text="Time:").grid(row=4, column=0)
tk.Label(window, text="Total Price:").grid(row=5, column=0)

# Create the entries
order_id_entry = tk.Entry(window)
order_id_entry.grid(row=0, column=1)
table_number_entry = tk.Entry(window)
table_number_entry.grid(row=1, column=1)
customer_name_entry = tk.Entry(window)
customer_name_entry.grid(row=2, column=1)
date_entry = tk.Entry(window)
date_entry.grid(row=3, column=1)
time_entry = tk.Entry(window)
time_entry.grid(row=4, column=1)
total_price_entry = tk.Entry(window)
total_price_entry.grid(row=5, column=1)

# Create the buttons
save_button = tk.Button(window, text="Save", command=save_bill)
save_button.grid(row=6, column=0)
cancel_button = tk.Button(window, text="Cancel", command=window.destroy)
cancel_button.grid(row=6, column=1)

# Function to save the bill
def save_bill():
    # Get the values from the entries
    order_id = order_id_entry.get()
    table_number = table_number_entry.get()
    customer_name = customer_name_entry.get()
    date = date_entry.get()
    time = time_entry.get()
    total_price = total_price_entry.get()
    
    # Insert the values into the database
    cursor.execute("INSERT INTO bill (order_id, table_number, customer_name, date, time, total_price) VALUES (%s, %s, %s, %s, %s, %s)",
    (order_id, table_number, customer_name, date, time, total_price))
    connection.commit()
    
    # Show a message to the user
    messagebox.showinfo("Success", "Bill saved successfully.")
    
    # Close the window
    window.destroy()

# Start the window
window.mainloop()

# Close the database connection
close_connection(connection)
