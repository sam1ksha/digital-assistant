from pickle import NONE
import tkinter as Tkinter
from datetime import datetime


class Stopwatch: 
     counter = 66600
     running = False
     frame = None
     start = None
     stop = None
     reset= None
     label = None
     label3=None
     bg2=None
     display = "Starting"
     def __init__(self, root):


         self.bg2 = Tkinter.PhotoImage(file = "C:\\Users\\91984\\OneDrive\\Desktop\\Samiksha\\projects\\blanckbg.png")
         self.label3 = Tkinter.Label(root, image = self.bg2)
         self.label3.place(x=0,y=0)
 
         self.label = Tkinter.Label(root, text="Welcome!", bg="brown", fg="thistle", font="Verdana 30 bold", width=10, height=2)
         self.label.pack()
         self.frame = Tkinter.Frame(root)
         self.start = Tkinter.Button(self.frame, text='Start', width=10, height=3, bg="honeydew3",
                                     activebackground="powderblue", bd=5, relief="raised", command=lambda:self.Start(self.label))
         self.stop = Tkinter.Button(self.frame, text='Stop',width=10, height=3, state='disabled', bg="honeydew3",
                                    activebackground="powderblue", bd=5, relief="raised", command=self.Stop)
         self.reset = Tkinter.Button(self.frame, text='Reset',width=10, height=3, state='disabled', bg="honeydew3",
                                     activebackground="powderblue", bd=5, relief="raised", command=lambda:self.Reset(self.label))
         self.frame.pack(anchor = 'center',pady=10)
         self.start.pack(side="left")
         self.stop.pack(side ="left")
         self.reset.pack(side="left")


     def counter_label(self):

        def count(self):
            if self.running:
                tt = datetime.fromtimestamp(self.counter)
                self.display = tt.strftime("%H:%M:%S")
                self.label['text']=self.display  
                self.label.after(1000, lambda:count(self)) 
                self.counter += 1
                #print(self.counter)
                
       
        # Triggering the start of the counter.
        count(self)     
       
    # start function of the stopwatch
     def Start(self, label):
        self.running=True
        self.counter_label()
        self.start['state']='disabled'
        self.stop['state']='normal'
        self.reset['state']='normal'
       
    # Stop function of the stopwatch
     def Stop(self):
        self.start['state']='normal'
        self.stop['state']='disabled'
        self.reset['state']='normal'
        self.running = False
       
    # Reset function of the stopwatch
     def Reset(self, label):
        self.counter=66600
       
        # If reset is pressed after pressing stop.
        if self.running==False:      
            self.reset['state']='disabled'
            self.label['text']='Welcome!'
       
        # If reset is pressed while the stopwatch is running.
        else:               
            self.label['text']='Starting...'
     
