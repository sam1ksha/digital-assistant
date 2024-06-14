import tkinter as Tkinter
from tkinter import *
from tkinter.ttk import *
from datetime import datetime
import stopwatch
import alarm1
import cal
import winsound

root = Tkinter.Tk()
root.title("Digital Assisstant")
root.minsize(width=1000, height=800)

bg = Tkinter.PhotoImage(file = "C:\\Users\\91984\\OneDrive\\Desktop\\Samiksha\\projects\\mainbg.png")
label1 = Label(root, image = bg)
label1.pack()


def CreateStopwatchWindow(root):
    
    newWindow = Toplevel(root)
    newWindow.minsize(width=500, height=200)
    newWindow.title("Stopwatch")
    obj = stopwatch.Stopwatch(newWindow)

def CreateAlarmWindow(root):
    
    newWindow = Toplevel(root)
    newWindow.minsize(width=500, height=350)
    newWindow.title("Alarm")
    obj = alarm1.Alarm(newWindow)

def CreateCalendarWindow(root):
    
    newWindow = Toplevel(root)
    newWindow.minsize(width=500, height=200)
    newWindow.title("Calendar")
    obj = cal.Calendar1(newWindow)


stopwatchbutton = Tkinter.Button(root, text='Stopwatch', width=10,height=2,
                                 command=lambda:CreateStopwatchWindow(root),
                                 bg = "white", fg="black",
                                 activebackground="lightgoldenrodyellow",relief="groove",
                                 font = "Verdana 20 bold ", bd=4)
stopwatchbutton.place(x=408,y=450)

alarmbutton = Tkinter.Button(root, text='Alarm', width=10,height=2,
                             command=lambda:CreateAlarmWindow(root),
                             bg = "white", fg = "black", relief="groove",
                             font = "Verdana 20 bold ",
                             activebackground="lightgoldenrodyellow", bd=4)
alarmbutton.place(x=136,y=226)

calendarbutton = Tkinter.Button(root, text='Calendar', width=10,height=2,
                                command=lambda:CreateCalendarWindow(root),
                                bg = "white", fg = "black",
                                relief="groove",font = "Verdana 20 bold ",
                                activebackground="lightgoldenrodyellow", bd=4)
calendarbutton.place(x=682,y=217)

def VoiceFunc():
    winsound.PlaySound("C:\\Users\\91984\\OneDrive\\Desktop\\Samiksha\\projects\\lauravoice", winsound.SND_ASYNC)


mic = Tkinter.PhotoImage(file = "C:\\Users\\91984\\OneDrive\\Desktop\\Samiksha\\projects\\mic5.png")
laurabutton= Tkinter.Button(root,image = mic,command=VoiceFunc)
laurabutton.place(x=1150,y=220)

label2=Tkinter.Label(root,text="Message to the user: ", width=17, height=1,font="Verdana 15 bold")
label2.place(x=960,y=288)

label3=Tkinter.Label(root,text="Hey! \n I'm Laura \n I'm at your service. \n What can I do for you? ",
                     width=20, height=5, font="Verdana 13 bold")
label3.place(x=948,y=350)


root.state('zoomed')

root.mainloop()
