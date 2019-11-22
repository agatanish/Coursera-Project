#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/python3

import time
import os
import tkinter
from tkinter import *
import sys
import time
from Adafruit_IO import Client, Feed, Data

oldState=0;

root = Tk()
root.geometry('1360x768+0+0')
root.title('PatientFeed')
root.configure(background='black')
H = 10

PatientFeed = Label( root, text='Patient Feed', fg='white', bg='black', font='Impact 20')
PatientFeed.pack()
    
def update(): 
    
    aio = Client("agatanish","eece6c6aa3304338a2349d3c1e0e56f1")
 
    global oldState
    
    
    
    newState = int(aio.receive("state").value)
    
    
    
    if(oldState != newState):
        
        if(newState == 1):
            var1.set("message 1")
            oldState=newState
        elif(newState == 2):
            var1.set("message 2")
            oldState=newState
        elif(newState == 3):
            var1.set("message 3")
            oldState=newState
        elif(newState == 4):
            var1.set("message 4")
            oldState=newState
        elif(newState == 5):
            var1.set("message 5")
            #time.sleep(120)
            oldState=newState
        elif(newState == 6):
            var1.set("message 6")
            #time.sleep(120)
            oldState=newState
        elif(newState == 7):
            var1.set("message 7")
            #time.sleep(120)
            oldState=newState
        elif(newState == 8):
            var1.set("message 8")
            #time.sleep(120)
            oldState=newState
    
    
    
    
    else:
        var1.set("No Message")
        print("no")
    
    
    
    root.after(1000, update)

var1 = StringVar()
        
label1 = Label(root, textvariable=var1, width=10)
label1.pack()
    
    


root.after(1000, update)


root.mainloop()

