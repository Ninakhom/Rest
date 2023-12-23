import tkinter as tk
from tkinter import messagebox
import sys
import os
from PIL import ImageTk, Image

def open_employee_management():
    frm1.destroy()
    os.system("python insertstaff.py")

def open_menuitems_management():
    frm1.destroy()
    os.system("python insertitems.py")

def open_orderchef():
    frm1.destroy()
    os.system("python kitchen.py")

def on_exit():
    frm1.destroy()

def hide_menu_items():
    # Convert user_author to lowercase for case-insensitive comparison
    lower_user_author = user_author.lower()

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
    elif lower_user_author == "biller":
        management_menu.entryconfigure("Employee Management", state='disabled')
        management_menu.entryconfigure("Menuitems Management", state='disabled')
        edit_menu.entryconfigure("Order", state='disabled')
        Bill_menu.entryconfigure("Bill", state='normal')

def set_user_author(job_title, username):
    global user_author
    global user_username
    user_author = job_title.lower()  # Convert to lowercase for consistent comparison
    user_username = username

# Retrieve the job_title and username from command-line arguments
job_title = sys.argv[1].lower() if len(sys.argv) > 1 else "default"
username = sys.argv[2] if len(sys.argv) > 2 else "Guest"

# Set user_author based on job_title (you can modify this logic based on your needs)
set_user_author(job_title, username)

# Main code for dash window
frm1 = tk.Tk()
frm1.geometry('1500x1000')
frm1.title('DashBord')

# Label to display welcome message
welcome_label = tk.Label(frm1, text=f"Welcome, {user_username}!", font=('Times New Roman', 16))
welcome_label.pack()

frm1.resizable(0,0)
frm1.state('zoomed')
bg_frame=Image.open('images\\pexels-chan-walrus-958545 (1).jpg')
photo =ImageTk.PhotoImage(bg_frame)
bg_panel=tk.Label(frm1,image=photo)
bg_panel.image = photo
bg_panel.pack(fill='both',expand='yes')

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
Bill_menu.add_command(label="Bill", command=lambda: messagebox.showinfo("Click Me", "You clicked the 'Bill' menu item."))

hide_menu_items()

frm1.mainloop()
