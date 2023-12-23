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

# Function to retrieve all bills from the database
def get_all_bills():
    cursor.execute("SELECT * FROM bills")
    all_bills = cursor.fetchall()
    return all_bills

# Function to display all bills in a new window
def display_all_bills():
    all_bills = get_all_bills()

    if not all_bills:
        tk.messagebox.showinfo("Info", "No bills found.")
    else:
        bill_window = tk.Toplevel(frm)
        bill_window.title("All Bills")

        for bill in all_bills:
            bill_id, order_id, total_amount, payment_status, bill_date = bill

            tk.Label(bill_window, text=f"Bill ID: {bill_id}").pack()
            tk.Label(bill_window, text=f"Order ID: {order_id}").pack()
            tk.Label(bill_window, text=f"Total Amount: {total_amount}").pack()
            tk.Label(bill_window, text=f"Payment Status: {payment_status}").pack()
            tk.Label(bill_window, text=f"Bill Date: {bill_date}").pack()
            tk.Label(bill_window, text="").pack()

# Set up the main window
frm = tk.Tk()
frm.geometry('800x600')
frm.title('All Orders and Details')

# Button to display all bills
show_bills_button = ttk.Button(frm, text="Show All Bills", command=display_all_bills)
show_bills_button.pack()

# Start the Tkinter main loop
frm.mainloop()

# Don't forget to close the database connection when the application exits
close_connection(connection)
