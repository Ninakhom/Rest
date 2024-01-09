import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ConectDB import connect, close_connection
from datetime import datetime
import sys
from tkinter import ttk, messagebox
import os
connection = connect()
cursor = connection.cursor()
frm = tk.Tk()
frm.state('zoomed')
frm.geometry('1166x718')
frm.title('Kitchen Orders')
lgn_frame = tk.Frame(frm, bg='#508CF7', width=2000, height=80)
lgn_frame.place(x=0, y=0)
lbFrame1 = tk.LabelFrame(frm, text='Kitchen Orders',width=900, height=500,background='#CFD5E2')
lbFrame1.place(x=500, y=150)
lbFrame1.config(font=("Times New Roman", 14, "bold"), fg="darkblue")

def update_label():

    current_datetime = datetime.now()  
    lbdate.config(text=current_datetime.strftime("%d-%m-%Y %H:%M:%S"),font=("Helvetica", 16))
    lbdate.after(1000, update_label)
def get_orders():
    connection = connect()
    if connection is None:
        return []

    cursor = connection.cursor()
    cursor.execute("SELECT orders.order_id, orders.table_number, orders.order_date, orders.status, order_items.item_name, order_items.quantity FROM orders INNER JOIN order_items ON orders.order_id = order_items.order_id WHERE orders.status = 'Pending'")
    orders = cursor.fetchall()
    close_connection(connection)
    return orders

def calculate_total_amount(order_id):
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("SELECT SUM(quantity * price) FROM order_items WHERE order_id = %s", (order_id,))
    total_amount = cursor.fetchone()[0]

    close_connection(connection)
    return total_amount

def update_order_status(order_id):
    connection = connect()
    if connection is None:
        return

    cursor = connection.cursor()
    cursor.execute("UPDATE orders SET status = 'Completed' WHERE order_id = %s", (order_id,))

    # Insert data into the bills table
    total_amount = calculate_total_amount(order_id)
    cursor.execute("INSERT INTO bills (order_id, total_amount) VALUES (%s, %s)", (order_id, total_amount))

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

def Logout():
    # Ask for confirmation using a messagebox
    confirmed = messagebox.askyesno("Confirm Logout", "Are you sure you want to logout?")

    if confirmed:
        # Perform any logout-related actions here
        print("Logging out...")

        # Optionally, destroy the main Tkinter window
        frm.destroy()
        os.system(f"python Stafflogin.py ")

if len(sys.argv) >= 4:
    position = sys.argv[1]
    staff_name = sys.argv[2]
    staff_id = sys.argv[3]
    print(f"Position: {position}, Staff Name: {staff_name}, Staff ID: {staff_id}")
    print("Print statement reached.")

# Set up the main window


# Create a Treeview widget
columns = ("Order ID", "Table", "Status", "Item", "Quantity")
tree = ttk.Treeview(lbFrame1, columns=columns, show="headings", height=15)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)


c1='#020f12'
c2='#508CF7'
c3='#508CF7'
c4='black'

tree.place(x=70,y=20)
welcome_label = tk.Label(frm, text=f"Kitchen Page", font=('Times New Roman', 26),bg='#508CF7')
welcome_label.place(x=800,y=20)

current_datetime = datetime.now()
lbdate=tk.Label(frm,text=current_datetime,bg='#CFD5E2')

lbdate.place(x=800,y=100)
# Display orders initially
display_orders()

# Bind the click event to the on_tree_click function
tree.bind("<ButtonRelease-1>", on_tree_click)
frm.config(bg='#CFD5E2')
frm.resizable(0, 0)
frm.state('zoomed')



# Add any additional UI elements if needed
button_Logout = tk.Button(text="Logout", command=Logout, bg=c2,
    fg=c4,
    activebackground=c3,
    activeforeground=c4,
    highlightthickness=2,
    highlightbackground=c2,
    highlightcolor='white',
    
    border=5,
    cursor='hand1',
    
    )
button_Logout.place(x="1250", y="650")
# Start the Tkinter main loop
update_label()
frm.mainloop()
