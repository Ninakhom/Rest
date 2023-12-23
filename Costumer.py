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

frm.mainloop()