import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import mysql.connector as mysql
from ConectDB import connect, close_connection
import os
from PIL import ImageTk, Image

def insert_employee():
    fname = entry_first_name.get()
    lname = entry_last_name.get()
    job = val_major.get()

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
    os.system("python dash.py")



# GUI setup
frm = tk.Tk()
frm.geometry("1166x718")
frm.title("Employee Information")

# Entry widgets for employee details


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
frm.txt = "Add Staff"
frm.heading = tk.Label(lgn_frame, text=frm.txt, font=('yu gothic ui', 25, "bold"), bg="#ffffff",
                             
                             bd=5,
                             relief="flat")
frm.heading.place(x=350, y=30, width=300, height=30)

side_image = Image.open('images\\abstract_533.jpg')
photo = ImageTk.PhotoImage(side_image)
side_image_label = tk.Label(lgn_frame, image=photo, bg='#040405')
side_image_label.image = photo
side_image_label.place(x=950, y=460)

label_first_name = tk.Label(frm, text="username:")
label_first_name.place(x=550,y= 460)
entry_first_name = tk.Entry(frm,bg="#ffffff",width=22,)
entry_first_name.place(x=700,y= 460)
entry_first_name.config(font=('Times New Roman',16))

label_last_name = tk.Label(frm, text="password:")
label_last_name.place(x=550,y= 530)
entry_last_name = tk.Entry(frm,width=22,)
entry_last_name.place(x=700,y= 530)
entry_last_name.config(font=('Times New Roman',16))

label_job_title = tk.Label(frm, text="Job Title:")
label_job_title.place(x=550,y=600 )

val_major = tk.StringVar()
cbb = ttk.Combobox(frm, textvariable=val_major, state='readonly')
cbb.place(x=700, y=600)
cbb.config(font=("Times New Roman", 16))
cbb['values'] = ('Admin', 'Bill', 'Chef',)

# Button to insert employee information
button_insert_employee = tk.Button(frm, text="Insert Employee", command=insert_employee)
button_insert_employee.place(x=550,y= 670)

button_cancel = tk.Button(frm, text="Cancel", command=cancel)
button_cancel.place(x=650,y= 670)


frm.mainloop()
