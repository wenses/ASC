import tkinter
from tkinter import *
from tkinter import messagebox

win=Tk()
win.geometry('700x500')
win.title('KIDESHENIS STOCK CARE SOFTWARE')
#win.resizable(FALSE,FALSE)
#win.config(bg='dark grey')

font_text=('Cambria',25,'bold')

title_text="KIDESHENI'S STOCK CARE"
title_label=Label(win,text=title_text,font=font_text)
title_label.place(x=10,y=10)



b1=Button(win,text='1.STOCK ADMINISTRATION',font=('Cambria',20,'bold'),fg='white',bg='purple')
b1.place(x=10,y=50)


b2=Button(win,text='2.STOCK EVALUATION',font=('Cambria',20,'bold'),fg='white',bg='purple')
b2.place(x=10,y=100)

b3=Button(win,text='3.PERSONAL ACCOUNTS',font=('Cambria',20,'bold'),fg='white',bg='purple')
b3.place(x=10,y=150)






win.mainloop()
