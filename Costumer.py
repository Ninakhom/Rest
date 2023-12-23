
#import 
import tkinter 
from tkinter import *
from PIL import Image, ImageTk
import tkinter.ttk as ttk
from code import interact

#interact
#setup from
frm = tkinter.Tk()


#function

#function remove

def remove():
    mytree.delete(*mytree.selection())

def clear():
    mytree.delete(*mytree.get_children())

def pay():
    total_price = 0
    for row in mytree.get_children():
        food_price = mytree.item(row)['values'][1]
        food_amount = mytree.item(row)['values'][2]
        total_price += food_price * food_amount
    tkinter.messagebox.showinfo("Total Price" , total_price)
    mytree.delete(*mytree.get_children())


#set window sizeS
frm.geometry("1166x718")
frm.config(bg = "#008000")
frm.state("zoomed")

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

label_addtable = tkinter.Label(text="Choose Table" ,fg = "black")
label_addtable.place(x = "500" , y = "100")

#addtable use combobox
combo = ttk.Combobox(frm)
combo['values'] = ('1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10')
combo.place(x = "600" , y = "100")



btn_remove = tkinter.Button(text="Remove" , command = remove)
btn_remove.place(x = "700" , y = "450")

btn_clear = tkinter.Button(text="Clear" , command = clear)
btn_clear.place(x = "800" , y = "450")

btn_pay = tkinter.Button(text="Pay" , command = pay)
btn_pay.place(x = "900" , y = "450")

#create button add entry data from label image
btn_hamburger = tkinter.Button(text="Add" , command = add_food)
btn_hamburger.place(x = "100" , y = "200")
"""
btn_sapageti = tkinter.Button(text="Add" , command = add)
btn_sapageti.place(x = "250" , y = "200")

btn_kapao = tkinter.Button(text="Add" , command = add)
btn_kapao.place(x = "400" , y = "200")

btn_phutthai = tkinter.Button(text="Add" , command = add)
btn_phutthai.place(x = "100" , y = "370")

btn_kaophut = tkinter.Button(text="Add" , command = add)
btn_kaophut.place(x = "250" , y = "370")

btn_papayapokpok = tkinter.Button(text="Add" , command = add)
btn_papayapokpok.place(x = "400" , y = "370")

btn_coke = tkinter.Button(text="Add" , command = add)
btn_coke.place(x = "100" , y = "600")

btn_chocolate = tkinter.Button(text="Add" , command = add)
btn_chocolate.place(x = "250" , y = "600")

btn_greentea = tkinter.Button(text="Add" , command = add)
btn_greentea.place(x = "400" , y = "600")"""
#create a entry value get foodname form label form btn hamberger


 


#tree view
#create treeview


#treeview
columns = ('food_name' , 'food_price' , 'food_amount')
mytree = ttk.Treeview(frm , columns = columns , show = "headings") 
mytree.place(x = "500" , y = "150" , width ="600", height = "300")

mytree.heading('food_name', text='food_name')
mytree.heading('food_price', text='food_price')
mytree.heading('food_amount', text='food_amount')



frm.mainloop()