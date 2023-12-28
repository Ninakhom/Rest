import tkinter as tk
from tkinter import messagebox
import sys
import os
from PIL import ImageTk, Image

# Declare user_author as a global variable
user_author = ""

def open_employee_management():
    frm1.destroy()
    os.system("python insertstaff.py")

def open_menuitems_management():
    frm1.destroy()
    os.system("python insertitems.py")

def open_orderchef():
    frm1.destroy()
    os.system(f"python kitchen.py {staff_id} {staff_name}")

def open_bill():
    frm1.destroy()
    os.system(f"python billfrom.py {staff_id} {staff_name}")

# Exit the program
def on_exit():
    frm1.destroy()

def hide_menu_items():
    # Convert user_author to lowercase for case-insensitive comparison
    lower_user_author = position.lower()

    # Hide or disable menu items based on user_author
    if lower_user_author == "chef":
        management_menu.entryconfigure("Employee Management", state='disabled')
        management_menu.entryconfigure("Menuitems Management", state='disabled')
        edit_menu.entryconfigure("Order", state='normal')
        Bill_menu.entryconfigure("Bill", state='disabled')
    elif lower_user_author == "admin":
        management_menu.entryconfigure("Employee Management", state='normal')
        management_menu.entryconfigure("Menuitems Management", state='normal')
        edit_menu.entryconfigure("Order", state='normal')
        Bill_menu.entryconfigure("Bill", state='normal')
    elif lower_user_author == "bill":
        management_menu.entryconfigure("Employee Management", state='disabled')
        management_menu.entryconfigure("Menuitems Management", state='disabled')
        edit_menu.entryconfigure("Order", state='disabled')
        Bill_menu.entryconfigure("Bill", state='normal')

def set_user_author(position, username, lbname):
    global user_author
    global user_username
    user_author = position.lower()  # Convert to lowercase for consistent comparison
    user_username = username
    lbname.config(text=f"Welcome, {staff_name}!")
    


if len(sys.argv) >= 4:
    position = sys.argv[1]
    staff_name = sys.argv[2]
    staff_id = sys.argv[3]
    
    # Additional processing with position, staff_name, and staff_id
    
    # Call bill.py with the necessary data
    
else:
    print("Insufficient command-line arguments.")

# Main code for dash window
frm1 = tk.Tk()
frm1.geometry('1500x1000')
frm1.title('DashBord')

# Label to display welcome message
welcome_label = tk.Label(frm1, text=f"Welcome, {staff_name}!", font=('Times New Roman', 16))
welcome_label.pack()

frm1.resizable(0, 0)
frm1.state('zoomed')


menu_bar = tk.Menu(frm1)
menu_bar.config(font=('Times New Roman', 16))
frm1.config(menu=menu_bar)

management_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Management", menu=management_menu)
management_menu.add_command(label="Employee Management", command=open_employee_management)
management_menu.add_command(label="Menuitems Management", command=open_menuitems_management)

edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Chef", menu=edit_menu)
edit_menu.add_command(label="Order", command=open_orderchef)

Bill_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Bill", menu=Bill_menu)
Bill_menu.add_command(label="Bill", command=open_bill)


lbname = tk.Label(frm1, text="")
lbname.pack()
hide_menu_items()

# Pass lbname to the set_user_author function
set_user_author(position, staff_name, lbname)
print(position)
frm1.mainloop()
