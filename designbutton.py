import tkinter
frm=tkinter.Tk()
frm.geometry('300x300')
c1='#020f12'
c2='#05d7ff'
c3='#65e7ff'
c4='black'
btn=tkinter.Button(
    frm,
    bg=c2,
    fg=c4,
    activebackground=c3,
    activeforeground=c4,
    highlightthickness=2,
    highlightbackground=c2,
    highlightcolor='white',
    width=13,
    height=2,
    border=5,
    cursor='hand1',
    text='Login',
    font=('Arial',16,'bold')
    
    )
btn.pack()
frm.mainloop()