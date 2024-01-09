#import 
import tkinter 
from tkinter import *
from PIL import Image, ImageTk
import tkinter.ttk as ttk
import mysql.connector  # Import the MySQL connector module
from ConectDB import connect, close_connection
from tkinter import messagebox
import sys
from PIL import Image, ImageTk
import os
connection = connect()
cursor = connection.cursor()
c1='#020f12'
c2='#508CF7'
c3='#508CF7'
c4='black'


username = sys.argv[1] if len(sys.argv) > 1 else "Guest"
user_id = sys.argv[2] if len(sys.argv) > 2 else "0"

# ... (rest of your code)

# Create the main window
frm = tkinter.Tk()
#set blackground to green 

frm.title("Obee Restaurant")
frm.geometry("1500x1000")
frm.resizable(0,0)
frm.state('zoomed')
frm.config(bg='#CFD5E2')

lgn_frame = tkinter.Frame(frm, bg='#508CF7', width=2000, height=80)
lgn_frame.place(x=0, y=0)


# Create a list of food items
food_items = ['Hamburger', 'Sapageti', 'Kapao', 'Phutthai', 'Kaophut', 'Papayapokpok', 'Coke', 'Chocolate', 'Greentea']

# Create a list of drink items
drink_items = ['Coke', 'Chocolate', 'Greentea']

# Create a list of table numbers
table_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# Create a list of quantities
quantities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a list of prices for each food item

# Prices for each food item
food_prices = {
    'Hamburger': 40000,
    'Sapageti': 40000,
    'Kapao': 30000,
    'Phutthai': 35000,
    'Kaophut': 30000,
    'Papayapokpok': 40000,
    'Coke': 10000,
    'Chocolate': 15000,
    'Greentea': 15000,
}

def set_user_author(job_title, username, lbname):
    global user_author
    global user_username
    user_author = job_title.lower()  # Convert to lowercase for consistent comparison
    user_username = username


# Function to add item to the treeview
def add_item():
    
    global user_username  # Declare user_username as a global variable

    food_name = combo_food.get()
    food_quantity = spinbox_quantity.get()
    table_number = combo_table.get()

    # Retrieve the price based on the selected food item
    food_price = food_prices.get(food_name, 0)

    # Insert item into the treeview
    mytree.insert('', 'end', values=(table_number, food_name, food_price, food_quantity, food_price * int(food_quantity)))

    # Insert data into the database
    try:
        query = "INSERT INTO orders (user_id, table_number, order_date, status) VALUES (%s, %s, CURRENT_TIMESTAMP, 'Pending')"
        cursor.execute(query, (user_id, table_number))
        connection.commit()
        print("Data inserted into the database.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
def Logout():
    # Ask for confirmation using a messagebox
    confirmed = messagebox.askyesno("Confirm Logout", "Are you sure you want to logout?")

    if confirmed:
        # Perform any logout-related actions here
        print("Logging out...")

        # Optionally, destroy the main Tkinter window
        frm.destroy()
        os.system(f"python login.py ")

# Function to submit order
def submit_order():
    # Get the table number
    table_number = combo_table.get()
    # Get the order_id of the newly inserted order
    order_id = cursor.lastrowid

    # Iterate over items in mytree and insert into order_items table
    for row_id in mytree.get_children():
        food_name = mytree.item(row_id, 'values')[1]
        quantity = mytree.item(row_id, 'values')[3]
        food_price = mytree.item(row_id, 'values')[2]

        # Insert items into order_items table
        cursor.execute("INSERT INTO order_items (order_id, item_name, quantity, price) VALUES (%s, %s, %s, %s)",
                       (order_id, food_name, quantity, food_price))
        connection.commit()

    # Show a message or perform any additional actions as needed
    tkinter.messagebox.showinfo("Order Submitted", "Order submitted successfully.")
    mytree.delete(*mytree.get_children())  # Clear the mytree

def cancel():
    selected_item = mytree.selection()
    if selected_item:
        mytree.delete(selected_item)
def update_selected_item(event):
    # Get the selected item
    selected_item = mytree.selection()

    if selected_item:
        # Get the current values of the selected item
        current_values = mytree.item(selected_item, 'values')

        # Create a new Toplevel window for editing
        edit_window = tkinter.Toplevel(frm)

        # Add Combo box for food name
        tkinter.Label(edit_window, text="Food Name:").grid(row=1, column=0, padx=5, pady=5)
        combo_food_var = tkinter.StringVar(value=current_values[1])
        combo_food = ttk.Combobox(edit_window, textvariable=combo_food_var)
        combo_food['values'] = ('Hamburger', 'Sapageti', 'Kapao', 'Phutthai', 'Kaophut', 'Papayapokpok', 'Coke', 'Chocolate', 'Greentea')
        combo_food.grid(row=1, column=1, padx=5, pady=5)

        # Add Entry widget for quantity
        tkinter.Label(edit_window, text="Quantity:").grid(row=3, column=0, padx=5, pady=5)
        entry_quantity_var = tkinter.StringVar(value=current_values[3])
        entry_quantity = tkinter.Entry(edit_window, textvariable=entry_quantity_var)
        entry_quantity.grid(row=3, column=1, padx=5, pady=5)

        # Function to update the values in mytree when the "Update" button is clicked
        def update_values():
            # Get the updated values from the Combo box and Entry widget
            updated_food_name = combo_food_var.get()
            updated_quantity = entry_quantity_var.get()

            # Update the values in mytree
            mytree.item(selected_item, values=(current_values[0], updated_food_name, food_prices[updated_food_name], updated_quantity, int(food_prices[updated_food_name]) * int(updated_quantity)))

            # Destroy the Toplevel window
            edit_window.destroy()

        # Add an "Update" button to apply the changes
        tkinter.Button(edit_window, text="Update", command=update_values).grid(row=4, columnspan=2, pady=10)






# Image paths
img_paths = ["hamburger.jpg", "Sapageti.jpg.jpg", "kapao.jpg.", "phutthai.jpg", "kaophut.jpg", "papayapokpok.jpg",
             "coke.jpg", "chocolate.jpg", "greentea.jpg"]

# Load and resize images
images = [ImageTk.PhotoImage(Image.open(img_path).resize((200, 200), Image.ANTIALIAS)) for img_path in img_paths]

# Create labels for images
for i, image in enumerate(images):
    label = tkinter.Label(image=image)
    label.place(x=(50 + 250 * (i % 3)), y=(150 + 250 * (i // 3)))

# Create treeview to show values
columns = ('table_number', 'food_name', 'food_price', 'food_quantity', 'total_cost')
mytree = ttk.Treeview(frm, columns=columns, show="headings")
mytree.place(x="1000", y="150", width="800", height="300")
mytree.bind("<Double-Button-1>", update_selected_item)
for col in columns:
    mytree.heading(col, text=col)



lb_wel = tkinter.Label(text="Welcome To Obee Restaurant", fg="black", )
lb_wel.configure(bg='#508CF7')
lb_wel.configure(fg='Black')
lb_wel.configure(font=('times new roman', 20, 'bold'))
lb_wel.place(x="10", y="20")

label_food = tkinter.Label(text="Food", fg="black",)
label_food.configure(bg='#CFD5E2')
label_food.configure(fg='Black')
label_food.configure(font=('times new roman',16, 'bold'))
label_food.place(x="10", y="120")

label_drink = tkinter.Label(text="Drink", fg="black",)
label_drink.configure(bg='#CFD5E2')
label_drink.configure(fg='Black')
label_drink.configure(font=('times new roman', 16, 'bold'))
label_drink.place(x="10", y="620")

# Name labels for food items
label_hamburger = tkinter.Label(text="Hamburger   40.000kip", fg="black",bg='#CFD5E2')
label_hamburger.place(x="90", y="360")

label_sapageti = tkinter.Label(text="Sapageti   40.000kip", fg="black",bg='#CFD5E2')
label_sapageti.place(x="340", y="360")

label_kapao = tkinter.Label(text="Kapao    30.000kip", fg="black",bg='#CFD5E2')
label_kapao.place(x="600", y="360")

label_phutthai = tkinter.Label(text="Phutthai   35.000kip", fg="black",bg='#CFD5E2')
label_phutthai.place(x="90", y="610")

label_kaophut = tkinter.Label(text="Kaophut   30.000kip", fg="black",bg='#CFD5E2')
label_kaophut.place(x="340", y="610")

label_papayapokpok = tkinter.Label(text="Papayapokpok   40.000kip", fg="black",bg='#CFD5E2')
label_papayapokpok.place(x="600", y="610")

label_coke = tkinter.Label(text="Coke    10.000kip", fg="black",bg='#CFD5E2')
label_coke.place(x="90", y="860")

label_chocolate = tkinter.Label(text="Chocolate  15.000kip", fg="black",bg='#CFD5E2')
label_chocolate.place(x="340", y="860")

label_greentea = tkinter.Label(text="Greentea  15.000kip", fg="black",bg='#CFD5E2')
label_greentea.place(x="600", y="860")

label_addtable = tkinter.Label(text="Choose Table", fg="black",bg='#CFD5E2')
label_addtable.place(x="880", y="100")

label_addmenu = tkinter.Label(text="Choose Menu", fg="black",bg='#CFD5E2')
label_addmenu.place(x="1180", y="100")

label_addquantity = tkinter.Label(text="Choose Quantity", fg="black",bg='#CFD5E2')
label_addquantity.place(x="1480", y="100")

# Create button + hamburger
button_add = tkinter.Button(text="Add Item", command=add_item, bg=c2,
    fg=c4,
    activebackground=c3,
    activeforeground=c4,
    highlightthickness=2,
    highlightbackground=c2,
    highlightcolor='white',
    
    border=5,
    cursor='hand1',
    
    )
button_add.place(x="1670", y="100")

button_confirm = tkinter.Button(text="Confirm Order", command=submit_order, bg=c2,
    fg=c4,
    activebackground=c3,
    activeforeground=c4,
    highlightthickness=2,
    highlightbackground=c2,
    highlightcolor='white',
    
    border=5,
    cursor='hand1',
    
    )
button_confirm.place(x="1700", y="500")


button_cancel = tkinter.Button(text="Cancel", command=cancel, bg=c2,
    fg=c4,
    activebackground=c3,
    activeforeground=c4,
    highlightthickness=2,
    highlightbackground=c2,
    highlightcolor='white',
    
    border=5,
    cursor='hand1',
    
    )
button_cancel.place(x="1770", y="100")
# Table number ComboBox
combo_table = ttk.Combobox(frm)
combo_table['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
combo_table.place(x="980", y="100")


# Food ComboBox
combo_food = ttk.Combobox(frm)
combo_food['values'] = ('Hamburger', 'Sapageti', 'Kapao', 'Phutthai', 'Kaophut', 'Papayapokpok', 'Coke', 'Chocolate', 'Greentea')
combo_food.place(x="1280", y="100")

# Quantity Spinbox
spinbox_quantity = ttk.Spinbox(frm, from_=1, to=10)
spinbox_quantity.place(x="1600", y="100" , width="50")


welcome_label = tkinter.Label(frm, text=f"Welcome, {username}!", font=('Times New Roman', 16),bg='#508CF7')
welcome_label.pack()

button_Logout = tkinter.Button(text="Logout", command=Logout, bg=c2,
    fg=c4,
    activebackground=c3,
    activeforeground=c4,
    highlightthickness=2,
    highlightbackground=c2,
    highlightcolor='white',
    
    border=5,
    cursor='hand1',
    
    )
button_Logout.place(x="1750", y="1000")

# Close the database connection when the tkinter window is closed
frm.protocol("WM_DELETE_WINDOW", lambda: [connection.close(), frm.destroy()])
frm.mainloop()