<<<<<<< HEAD
import tkinter
=======
<<<<<<< HEAD
#import 
import tkinter 
>>>>>>> 75330e311463ef1fd9535dd12e9e2f035214b610
from tkinter import *
from PIL import Image, ImageTk
import tkinter.ttk as ttk
import mysql.connector  # Import the MySQL connector module
from ConectDB import connect, close_connection

connection = connect()
cursor = connection.cursor()

# ... (rest of your code)

# Create the main window
frm = tkinter.Tk()

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

# Function to add item to the treeview
def add_item():
    food_name = combo_food.get()
    food_quantity = spinbox_quantity.get()
    table_number = combo_table.get()

    # Retrieve the price based on the selected food item
    food_price = food_prices.get(food_name, 0)

    mytree.insert('', 'end', values=(table_number, food_name, food_price, food_quantity, food_price * int(food_quantity)))

    # Insert data into the database
    try:
        query = "INSERT INTO  (table_number, food_name, food_price, food_amount) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (table_number, food_name, food_price, food_quantity))
        conn.commit()
        print("Data inserted into the database.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Function to confirm menu 
def insert_order_item_to_database(order_id, item_name, quantity, price):
    try:
        # Assuming `cursor` and `conn` are already defined in your code
        query = "INSERT INTO order_items (order_id, item_name, quantity, price) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (order_id, item_name, quantity, price))
        conn.commit()
        print("Order item inserted into the database.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Set window title
frm.title("Obee Restaurant")

# Set window size
frm.geometry("1166x718")
frm.config(bg="#008000")
frm.state("zoomed")

# Image paths
img_paths = ["hamburger.jpg", "Sapageti.jpg.jpg", "kapao.jpg", "phutthai.jpg", "kaophut.jpg", "papayapokpok.jpg",
             "coke.jpg", "chocolate.jpg", "greentea.jpg"]

# Load and resize images
images = [ImageTk.PhotoImage(Image.open(img_path).resize((100, 100), Image.ANTIALIAS)) for img_path in img_paths]

# Create labels for images
for i, image in enumerate(images):
    label = tkinter.Label(image=image)
    label.place(x=(50 + 150 * (i % 3)), y=(150 + 170 * (i // 3)))

# Create treeview to show values    
columns = ('table_number', 'food_name', 'food_price', 'food_quantity', 'total_cost')
mytree = ttk.Treeview(frm, columns=columns, show="headings")
mytree.place(x="500", y="150", width="800", height="300")

for col in columns:
    mytree.heading(col, text=col)

# GUI labels
lb_wel = tkinter.Label(text="Welcome To Obee Restaurant", fg="black")
lb_wel.place(x="10", y="20")

label_food = tkinter.Label(text="Food", fg="black")
label_food.place(x="10", y="100")

label_drink = tkinter.Label(text="Drink", fg="black")
label_drink.place(x="10", y="500")

# Name labels for food items
label_hamburger = tkinter.Label(text="Hamburger", fg="black")
label_hamburger.place(x="70", y="280")

label_sapageti = tkinter.Label(text="Sapageti", fg="black")
label_sapageti.place(x="220", y="280")

label_kapao = tkinter.Label(text="Kapao", fg="black")
label_kapao.place(x="370", y="280")

label_phutthai = tkinter.Label(text="Phutthai", fg="black")
label_phutthai.place(x="70", y="450")

label_kaophut = tkinter.Label(text="Kaophut", fg="black")
label_kaophut.place(x="220", y="450")

label_papayapokpok = tkinter.Label(text="Papayapokpok", fg="black")
label_papayapokpok.place(x="370", y="450")

label_coke = tkinter.Label(text="Coke", fg="black")
label_coke.place(x="80", y="670")

label_chocolate = tkinter.Label(text="Chocolate", fg="black")
label_chocolate.place(x="230", y="670")

label_greentea = tkinter.Label(text="Greentea", fg="black")
label_greentea.place(x="380", y="670")

label_addtable = tkinter.Label(text="Choose Table", fg="black")
label_addtable.place(x="500", y="100")

label_addmenu = tkinter.Label(text="Choose Menu", fg="black")
label_addmenu.place(x="750", y="100")

label_addquantity = tkinter.Label(text="Choose Quantity", fg="black")
label_addquantity.place(x="1000", y="100")

# Create button + hamburger
button_add = tkinter.Button(text="Add Item", command=add_item)
button_add.place(x="1200", y="100")

button_confirm = tkinter.Button(text="Confirm Order", command=lambda: [insert_order_item_to_database(1, combo_food.get(), spinbox_quantity.get(), food_prices.get(combo_food.get(), 0)), mytree.delete(*mytree.get_children())])
button_confirm.place(x="1200", y="150")

# Table number ComboBox
combo_table = ttk.Combobox(frm)
combo_table['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
combo_table.place(x="600", y="100")

<<<<<<< HEAD
# Food ComboBox
combo_food = ttk.Combobox(frm)
combo_food['values'] = ('Hamburger', 'Sapageti', 'Kapao', 'Phutthai', 'Kaophut', 'Papayapokpok', 'Coke', 'Chocolate', 'Greentea')
combo_food.place(x="850", y="100")

# Quantity Spinbox
spinbox_quantity = ttk.Spinbox(frm, from_=1, to=10)
spinbox_quantity.place(x="1100", y="100" , width="50")

# Run the tkinter event loop
frm.mainloop()

# Close the database connection when the tkinter window is closed
frm.protocol("WM_DELETE_WINDOW", lambda: [close_connection(conn), frm.destroy()])
=======
#treeview
columns = ('food_name' , 'food_price')
mytree = ttk.Treeview(frm , columns = columns , show = "headings") 
mytree.place(x = "500" , y = "150" , width ="400", height = "300")

mytree.heading('food_name', text='food_name')
mytree.heading('food_price', text='food_price')




#mainloop

=======
#import 
import tkinter 
from tkinter import *
from PIL import Image, ImageTk
import tkinter.ttk as ttk




#setup from
frm = tkinter.Tk()

#set window sizeS
frm.geometry("1000x800")
frm.config(bg = "#008000")

#image
#create a label picture size 200 * 200 and put it in the window
img = Image.open("hamburger.jpg")
img = img.resize((100, 100), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(img)
label = tkinter.Label(image=photo)
label.place(x=50, y=150)

img1 = Image.open("Sapageti.jpg.jpg")
img1 = img1.resize((100, 100), Image.ANTIALIAS)
photo1 = ImageTk.PhotoImage(img1)
label1 = tkinter.Label(image=photo1)
label1.place(x=200, y=150)

img2 = Image.open("kapao.jpg")
img2 = img2.resize((100, 100), Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(img2)
label2 = tkinter.Label(image=photo2)
label2.place(x=350, y=150)

img3 = Image.open("phutthai.jpg")
img3 = img3.resize((100, 100), Image.ANTIALIAS)
photo3 = ImageTk.PhotoImage(img3)
label3 = tkinter.Label(image=photo3)
label3.place(x=50, y=320)

img4 = Image.open("kaophut.jpg")
img4 = img4.resize((100, 100), Image.ANTIALIAS)
photo4 = ImageTk.PhotoImage(img4)
label4 = tkinter.Label(image=photo4)
label4.place(x=200, y=320)

img5 = Image.open("papayapokpok.jpg")
img5 = img5.resize((100, 100), Image.ANTIALIAS)
photo5 = ImageTk.PhotoImage(img5)
label5 = tkinter.Label(image=photo5)
label5.place(x=350, y=320)

#Drink image

imgd1 = Image.open("coke.jpg")
imgd1 = imgd1.resize((100, 100), Image.ANTIALIAS)
photod1 = ImageTk.PhotoImage(imgd1)
labeld1 = tkinter.Label(image=photod1)
labeld1.place(x=50, y=550)

imgd2 = Image.open("chocolate.jpg")
imgd2 = imgd2.resize((100, 100), Image.ANTIALIAS)
photod2 = ImageTk.PhotoImage(imgd2)
label2 = tkinter.Label(image=photod2)
label2.place(x=200, y=550)

imgd3 = Image.open("greentea.jpg")
imgd3 = imgd3.resize((100, 100), Image.ANTIALIAS)
photod3 = ImageTk.PhotoImage(imgd3)
labeld3 = tkinter.Label(image=photod3)
labeld3.place(x=350, y=550)


#GUI
lb_wel = tkinter.Label(text="Welcome To Obee Resturant" ,fg = "black")
lb_wel.place( x = "10" , y = "20")

label_food = tkinter .Label(text="Food" ,fg = "black")
label_food.place( x = "10" , y = "100")

label_drink = tkinter .Label(text="Drink" ,fg = "black")
label_drink.place( x = "10" , y = "500")

#name label
label_hambuger = tkinter.Label(text="Hamburger" ,fg = "black")
label_hambuger.place(x = "70" , y = "280")

label_sapageti = tkinter.Label(text="Sapageti" ,fg = "black")
label_sapageti.place(x = "220" , y = "280")

label_kapao = tkinter.Label(text="Kapao" ,fg = "black")
label_kapao.place(x = "370" , y = "280")

label_phutthai = tkinter.Label(text="Phutthai" ,fg = "black")
label_phutthai.place(x = "70" , y = "450")

label_kaophut = tkinter.Label(text="Kaophut" ,fg = "black")
label_kaophut.place(x = "220" , y = "450")

label_papayapokpok = tkinter.Label(text="Papayapokpok" ,fg = "black")
label_papayapokpok.place(x = "370" , y = "450")

label_coke = tkinter.Label(text="Coke" ,fg = "black")
label_coke.place(x = "80" , y = "670")

label_chocolate = tkinter.Label(text="Chocolate" ,fg = "black")
label_chocolate.place(x = "230" , y = "670")

label_greentea = tkinter.Label(text="Greentea" ,fg = "black")
label_greentea.place(x = "380" , y = "670")

#treeview
columns = ('food_name' , 'food_price')
mytree = ttk.Treeview(frm , columns = columns , show = "headings") 
mytree.place(x = "500" , y = "150" , width ="400", height = "300")

mytree.heading('food_name', text='food_name')
mytree.heading('food_price', text='food_price')




#mainloop

>>>>>>> 309444aa6a4e6f1ab250ca51df73396d5b54e4e0
frm.mainloop()
>>>>>>> 75330e311463ef1fd9535dd12e9e2f035214b610
