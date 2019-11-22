#!/usr/bin/env python
# coding: utf-8

# In[3]:


#!/usr/bin/python3

import time
import os
import tkinter
from tkinter import *
import sys
import time
from Adafruit_IO import Client, Feed, Data
import requests


oldState=0;


def sendSMS(message):
    

    url = "https://www.fast2sms.com/dev/bulk"

    payload = "sender_id=FSTSMS&message={}&language=english&route=p&numbers=7814238088".format(message)
    headers = {
    'authorization': "NeOYAt03bx8ljDkwX65R1sTLZQ9Jympi4uSoKvWaghdHrVIU7PNztHIw86r5TM3b2EfhxWgFV7naRqlm",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)


root = Tk()
root.geometry('480x320+0+0')
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
            sendSMS("message 1 doctor")
        elif(newState == 2):
            var1.set("message 2")
            sendSMS("message 2 doctor")
            oldState=newState
        elif(newState == 3):
            var1.set("message 3")
            sendSMS("message 3 doctor")
            oldState=newState
        elif(newState == 4):
            var1.set("message 4")
            sendSMS("message 4 doctor")
            oldState=newState
        elif(newState == 5):
            var1.set("message 5")
            sendSMS("message 5 doctor")
            #time.sleep(120)
            oldState=newState
        elif(newState == 6):
            var1.set("message 6")
            sendSMS("message 6 doctor")
            #time.sleep(120)
            oldState=newState
        elif(newState == 7):
            var1.set("message 7")
            sendSMS("message 7 doctor")
            #time.sleep(120)
            oldState=newState
        elif(newState == 8):
            var1.set("message 8")
            sendSMS("message 8 doctor")
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


# In[ ]:




