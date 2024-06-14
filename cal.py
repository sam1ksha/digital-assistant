
from tkinter import *
from tkcalendar import Calendar
import datetime as dt
import tkinter as Tkinter
 

class Calendar1:
    
    cal=None
    date=None
    bg1=None
    label2=None
    
    def __init__(self,root):

        root.geometry('800x500')

        self.bg1 = Tkinter.PhotoImage(file = "C:\\Users\\91984\\OneDrive\\Desktop\\Samiksha\\projects\\blanckbg.png")
        self.label2 = Tkinter.Label(root, image = self.bg1)
        self.label2.place(x=0,y=0)
 
        self.cal = Calendar(root, selectmode = 'day', year = 2023, month = 1, day = 1,
                            background = "dodgerblue4", disabledbackground = "blue" ,
                            borderbackground = "blue" ,headersbackground = "powderblue" ,
                            normalbackground = "white")
 
        self.cal.pack(pady = 10)

        Button(root, text = "Get Date", command = self.grad_date,bg = "lavenderblush3",
               fg = "black").pack(pady = 40, side=BOTTOM)

        self.date = dt.datetime.now()
        Label(root, text=f"{self.date:%A, %B %d, %Y}", font="Times 15 italic bold").pack(pady=50)
        
 
        self.date = Label(root, text = "")
        self.date.pack(pady = 20)

        #root.state('zoomed')
 
    def grad_date(self):
        self.date.config(text = "Selected Date is: " + self.cal.get_date())
 

    
 
