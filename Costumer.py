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
connection = connect()
cursor = connection.cursor()
job_title = sys.argv[1].lower() if len(sys.argv) > 1 else "default"
username = sys.argv[2] if len(sys.argv) > 2 else "Guest"
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
user_id = sys.argv[3] if len(sys.argv) > 3 else "0"  # Set a default value if not provided
def set_user_author(job_title, username, lbname):
    global user_author
    global user_username
    user_author = job_title.lower()  # Convert to lowercase for consistent comparison
    user_username = username


# Function to add item to the treeview
def add_item():
    print(user_id)
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


user_author = sys.argv[1].lower() if len(sys.argv) > 1 else "default"
username = sys.argv[2] if len(sys.argv) > 2 else "Guest"

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

for col in columns:
    mytree.heading(col, text=col)

# GUI labels
#remove front ground of the label
# remove black gorund from text

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

label_addtable = tkinter.Label(text="Choose Table", fg="black",)
label_addtable.place(x="1000", y="100")

label_addmenu = tkinter.Label(text="Choose Menu", fg="black")
label_addmenu.place(x="1250", y="100")

label_addquantity = tkinter.Label(text="Choose Quantity", fg="black")
label_addquantity.place(x="1500", y="100")

# Create button + hamburger
button_add = tkinter.Button(text="Add Item", command=add_item)
button_add.place(x="1700", y="100")

button_confirm = tkinter.Button(text="Confirm Order", command=submit_order)
button_confirm.place(x="1700", y="500")

# Table number ComboBox
combo_table = ttk.Combobox(frm)
combo_table['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
combo_table.place(x="1100", y="100")


# Food ComboBox
combo_food = ttk.Combobox(frm)
combo_food['values'] = ('Hamburger', 'Sapageti', 'Kapao', 'Phutthai', 'Kaophut', 'Papayapokpok', 'Coke', 'Chocolate', 'Greentea')
combo_food.place(x="1350", y="100")

# Quantity Spinbox
spinbox_quantity = ttk.Spinbox(frm, from_=1, to=10)
spinbox_quantity.place(x="1600", y="100" , width="50")


welcome_label = tkinter.Label(frm, text=f"Welcome, {username}!", font=('Times New Roman', 16),bg='#508CF7')
welcome_label.pack()

# Close the database connection when the tkinter window is closed
frm.protocol("WM_DELETE_WINDOW", lambda: [connection.close(), frm.destroy()])
frm.mainloop()