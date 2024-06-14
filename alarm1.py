
from tkinter import *
import tkinter as Tkinter
import datetime
import time
import winsound
import threading

class Alarm:
    time_format=None 
    addTime=None 
    setYourAlarm=None  
    hour=None  
    minn=None  
    sec=None  
    hourTime=None  
    minTime=None  
    secTime=None  
    submit=None
    message=None
    mess=None
    bg3=None
    label4=None

    def __init__(self, window):

        self.bg3 = Tkinter.PhotoImage(file = "C:\\Users\\91984\\OneDrive\\Desktop\\Samiksha\\projects\\blanckbg.png")
        self.label4 = Tkinter.Label(window, image = self.bg3)
        self.label4.place(x=0,y=0)
         
        self.time_format=Label(window, text= "Remember to set time in 24 hour format!", fg="papaya whip",bg="midnight blue",
                               font=("Arial",15)).place(x=20,y=80)
        self.addTime = Label(window,text = "Hour     Min     Sec",font=60,fg="papaya whip",bg="red3").place(x = 210)
        self.setYourAlarm = Label(window,text = "Set Time for Alarm: ",fg="papaya whip",bg="deepskyblue4",relief = "solid",
                                  font=("Helevetica",15,"bold")).place(x=10, y=40)
        self.typeText=Label(window,text="Type your text: ",fg="papaya whip",bg="deepskyblue4",relief = "solid",
                                  font=("Helevetica",15,"bold")).place(x=10,y=130)
         
        self.hour = StringVar()
        self.minn = StringVar()
        self.sec = StringVar()
        self.message=StringVar()

        self.mess=Entry(window,textvariable=self.message,font=60,fg="midnight blue",bg="powder blue")
        self.mess.place(x=180,y=130)

        self.hourTime= Entry(window,textvariable = self.hour,fg="midnight blue",bg="powder blue",width = 4,font=(20)).place(x=210,y=40)
        self.minTime= Entry(window,textvariable = self.minn,fg="midnight blue",bg="powder blue",width = 4,font=(20)).place(x=270,y=40)
        self.secTime = Entry(window,textvariable = self.sec,fg="midnight blue",bg="powder blue",width = 4,font=(20)).place(x=330,y=40)


        self.submit = Button(window,text = "Set Your Alarm",fg="Black",bg="#D4AC0D",width = 15, height=1, font=(18),
                             relief="groove", bd=4, command = lambda:[self.SetAlarm(), self.TextMsg(window)]).place(x=170,y=180)

    def Count(self, set_alarm_timer):
          time.sleep(1)
          actual_time = datetime.datetime.now()
          cur_time = actual_time.strftime("%H:%M:%S")
          cur_date = actual_time.strftime("%d/%m/%Y")
          msg= "Current Time: " + str(cur_time)
          if cur_time < set_alarm_timer:
              self.Count(set_alarm_timer)

    def SetAlarm(self):
         alarm_set_time = f"{self.hour.get()}:{self.minn.get()}:{self.sec.get()}"
         t1 = threading.Thread(target = self.Count, args=(alarm_set_time,))
         t1.start()
         t1.join()
         
         winsound.PlaySound("C:\\Users\\91984\\OneDrive\\Desktop\\Samiksha\\projects\\alarmaudio", winsound.SND_ASYNC)
         

    def TextMsg(self,window):
         newtext=f"{self.mess.get()}"
         new=Label(window, text= newtext,fg="papaya whip",bg="midnight blue",
                               font=("Arial",20)).place(x=170,y=250)

    
        
   

