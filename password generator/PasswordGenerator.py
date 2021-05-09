############# password generator ############
from tkinter.ttk import Combobox
from tkinter import *
from genfunct import Generate
# sets all of the variables an calls the class to generate the password
def gen():
    capital = v1.get()
    lower = v2.get()
    number = v3.get()
    character = v4.get()
    length = int(cb.get())

    password = Generate(capital, lower, number, character, length)
    Outbox.delete(0, 'end')
    Outbox.insert(0, password.generation_funct())

win = Tk()

# all labels on window 
lbl1 = Label(win, text="PASSWORD GENERATOR", font=("Tahoma", 16), bg = 'cyan')
lbl1.place(x=220, y=40 )
lbl2 = Label(win, text="Choose a length 6 - 20", font=("Tahoma", 10), bg='light blue')
lbl2.place(x=50, y=190)
lbl3 = Label(win, text="choose what is needed from the boxes below you can choose multiple", font=("Tahoma", 10),  bg='light blue')
lbl3.place(x=50, y=80)
lbl4 =Label(win, text="This is a simple password generator fill out \n the nesesary infomation on the right and then \n press the generate button this will create you \n a random password with the right parameters", font=("Tahoma", 12), bg='light blue')
lbl4.place(x=220, y=140)

# button to generate the password
genBttn = Button(win, text="GENERATE", fg='blue', command=gen)
genBttn.place(x=500, y=300)

# check bp boxes
v1 = IntVar()
CheckCapital = Checkbutton(win, text = " -- ABCDEF, capital letters", variable = v1,onvalue=1, offvalue=0, bg='light blue')

v2 = IntVar()
CheckLowerCase = Checkbutton(win, text = " -- abcdef, lower case letters", variable = v2, onvalue=1, offvalue=0, bg='light blue')

v3 = IntVar()
CheckNumber  = Checkbutton(win, text = " -- 123456, numbers", variable = v3, onvalue=1, offvalue=0, bg='light blue')

v4 = IntVar()
CheckCharacter = Checkbutton(win, text= " -- £$%^&*(), characters", variable = v4, onvalue=1, offvalue=0, bg='light blue')

# drop down box
lengths = ["6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
cb =Combobox(win, values=lengths)

Outbox = Entry(win, bd=3)
Outbox.place(x=250, y=250, width=300)
Outbox.insert(0, "password will apear here")

# placing all widgets 

cb.place(x=50, y=215)
CheckCapital.place(x=50, y = 100)
CheckLowerCase.place(x=50, y = 120)
CheckNumber.place(x=50, y = 140)
CheckCharacter.place(x=50, y = 160)

# setting all of the paramerters of the window
win.title("Password Generator")
win.geometry("600x350")
win.resizable(0, 0) #Don't allow resizing in the x or y direction
win.configure(bg='light blue')

win.mainloop()
    
    
    
    