import tkinter as tk
from tkinter import ttk
from ConectDB import connect, close_connection
from PIL import Image, ImageTk
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
frm.state('zoomed')
frm.geometry('1166x718')
frm.title('Kitchen Orders')



# Display orders initially
display_orders()

frm.resizable(0,0)
frm.state('zoomed')
bg_frame=Image.open('images\\pexels-chan-walrus-958545 (1).jpg')
photo =ImageTk.PhotoImage(bg_frame)
bg_panel=tk.Label(frm,image=photo)
bg_panel.image = photo
bg_panel=tk.Label(frm,image=photo)
bg_panel.image = photo
bg_panel.pack(fill='both',expand='yes')
lgn_frame = tk.Frame(frm, bg='#ffffff', width=950, height=600)
lgn_frame.place(x=500, y=230)
frm.txt = "Orders"
frm.heading = tk.Label(lgn_frame, text=frm.txt, font=('yu gothic ui', 25, "bold"), bg="#ffffff",
                             
                             bd=5,
                             relief="flat")
frm.heading.place(x=350, y=30, width=300, height=30)
# Start the Tkinter main loop
frm.mainloop()

# Don't forget to close the database connection when the application exits
close_connection(connection)