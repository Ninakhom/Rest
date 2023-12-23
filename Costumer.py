#import 
import tkinter as Tk
from tkinter import *
from PIL import Image, ImageTk



#setup from

frm = Tk.Tk()
frm.title("Obee Resturant")
frm.geometry("1000x800")
frm.config(bg = "#008000")

#image
label  = Tk.Label(frm)
image = Image.open("C:/Users/Advice/Desktop/restuarant/Sapageti.jpg")
photo = ImageTk.PhotoImage(image)
label.image = photo
label.place(x=0, y=0)

#button
btn_menu = Tk.Button(text="Menu" , fg = "white" , bg = "black")
btn_menu.place(x = "10" , y = "100")

btn_order = Tk.Button(text="Order" , fg = "white" , bg = "black")
btn_order.place(x = "10" , y = "150")

btn_pay = Tk.Button(text="Pay" , fg = "white" , bg = "black")
btn_pay.place(x = "10" , y = "200")

btn_exit = Tk.Button(text="Exit" , fg = "white" , bg = "black")
btn_exit.place(x = "10" , y = "250")


#GUI
lb_wel = Tk.Label(text="Welcome To Obee Resturant" ,fg = "White")
lb_wel.place( x = "10" , y = "20")

frm.mainloop()