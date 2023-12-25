# from ConnectDB import create_connection, close_connection, get_cursor
# conn = create_connection()
# cursor = get_cursor(conn)
from tkinter import ttk
from code import interact
import tkinter
from tkinter import messagebox
import os
from PIL import Image, ImageTk
from ConectDB import connect, close_connection
import os
import mysql.connector as mysql
frm = tkinter.Tk()
frm.geometry("1166x718")
frm.title("Login")

connection = connect()
cursor = connection.cursor()
bg_frame=Image.open('images\\bg.jpg')
photo =ImageTk.PhotoImage(bg_frame)
bg_panel=tkinter.Label(frm,image=photo)

def insert_employee():
    fname = entry_username.get()
    lname = entry_password.get()
    job="tomer"

    connection = connect()

    if connection:
        try:
            cursor = connection.cursor()

            # SQL query to insert an employee into the users table
            sql_query = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
            values = (fname, lname, job,)

            # Execute the query
            cursor.execute(sql_query, values)

            # Commit the changes to the database
            connection.commit()

            messagebox.showinfo("Success", "Employee information inserted successfully!")

        except mysql.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

        finally:
            # Close the cursor and connection
            if cursor:
                cursor.close()

            close_connection(connection)


def cancel():
    frm.destroy()
    os.system("python login.py")



def move_to_next(event):
    widget = event.widget
    widget.tk_focusNext().focus()
frm.resizable(0,0)
frm.state('zoomed')
bg_frame=Ige = photo
bg_panel.pack(fill='both',expand='yes')
lgn_frame = tkinter.Frame(frm, bg='#040405', width=950, height=600)
lgn_frame.place(x=500, y=230)
frm.txt = "WELCOME"
frm.heading = tkinter.Label(lgn_frame, text=frm.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief="flat")
frm.heading.place(x=80, y=30, width=300, height=30)


side_image = Image.open('images\\vector.png')
photo = ImageTk.PhotoImage(side_image)
side_image_label = tkinter.Label(lgn_frame, image=photo, bg='#040405')
side_image_label.image = photo
side_image_label.place(x=5, y=100)


sign_in_image = Image.open('images\\hyy.png')
photo = ImageTk.PhotoImage(sign_in_image)
sign_in_image_label = tkinter.Label(lgn_frame, image=photo, bg='#040405')
sign_in_image_label.image = photo
sign_in_image_label.place(x=620, y=130)


sign_in_label = tkinter.Label(lgn_frame, text="Sign In", bg="#040405", fg="white",
                            font=("yu gothic ui", 17, "bold"))
sign_in_label.place(x=650, y=240)


username_label = tkinter.Label(lgn_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
username_label.place(x=550, y=300)

entry_username = tkinter.Entry(lgn_frame, highlightthickness=0, relief="flat", bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
entry_username.place(x=580, y=335, width=270)

username_line = tkinter.Canvas(lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
username_line.place(x=550, y=359)
        # ===== Username icon =========
username_icon = Image.open('images\\username_icon.png')
photo = ImageTk.PhotoImage(username_icon)
username_icon_label = tkinter.Label(lgn_frame, image=photo, bg='#040405')
username_icon_label.image = photo
username_icon_label.place(x=550, y=332)


lgn_button = Image.open('images\\btn1.png')
photo = ImageTk.PhotoImage(lgn_button)
lgn_button_label = tkinter.Label(lgn_frame, image=photo, bg='#040405')
lgn_button_label.image = photo
lgn_button_label.place(x=550, y=450)
login = tkinter.Button(lgn_button_label, text='Register', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=insert_employee)
login.place(x=20, y=10)


register_button_image = Image.open('images\\btn1.png')
register_photo = ImageTk.PhotoImage(register_button_image)
register_button_label = tkinter.Label(lgn_frame, image=register_photo, bg='#040405')
register_button_label.image = register_photo
register_button_label.place(x=550, y=500)

register_button = tkinter.Button(register_button_label, text='Cancel', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                                 bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=cancel)
register_button.place(x=20, y=10)
password_label = tkinter.Label(lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
                            font=("yu gothic ui", 13, "bold"))
password_label.place(x=550, y=380)

entry_password = tkinter.Entry(lgn_frame, highlightthickness=0, relief="flat", bg="#040405", fg="#6b6a69",
                            font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#6b6a69')
entry_password.place(x=580, y=416, width=244)

password_line = tkinter.Canvas(lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
password_line.place(x=550, y=440)
        # ======== Password icon ================
password_icon = Image.open('images\\password_icon.png')
photo = ImageTk.PhotoImage(password_icon)
password_icon_label = tkinter.Label(lgn_frame, image=photo, bg='#040405')
password_icon_label.image = photo
password_icon_label.place(x=550, y=414)



       
frm.mainloop()