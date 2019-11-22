#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk 
import sqlite3 as sq 

import time
import os
import tkinter
from tkinter import *
import sys
import time
from Adafruit_IO import Client, Feed, Data
import requests


oldState=0;


# In[2]:


window = Tk()
window.title("Hospital Database") 

window.geometry('480x320+0+0')

header = Label(window, text="Hospital Database System", font=("arial",20,"bold"), fg="black").pack()



L1 = Label(window, text = "PATIENT INFO", font=("arial", 14)).place(x=10,y=50)
L2 = Label(window, text = "Patient Name", font=("arial",14)).place(x=10,y=75)
L3 = Label(window, text = "Patient ID", font=("arial",14)).place(x=10,y=100)
L4 = Label(window, text = "Age", font=("arial",14)).place(x=10,y=125)
L5 = Label(window, text = "Sex", font=("arial",14)).place(x=10,y=150)
L6 = Label(window, text = "Blood Group", font=("arial",14)).place(x=10,y=175)
L7=  Label(window, text = "Contact Info", font=("arial",14)).place(x=10,y=200)
L8=  Label(window, text=  "Email-Id", font=("arial",14)).place(x=10,y=225)


# In[3]:


name=StringVar(window)
id = StringVar(window)
age = StringVar(window)
sex = StringVar(window)
blood = StringVar(window)
contact = StringVar(window)
email=StringVar(window)


# In[4]:


nameT = Entry(window, textvariable=name)
nameT.place(x=220,y=80)

idT = Entry(window, textvariable=id)
idT.place(x=220,y=105)

ageT = Entry(window, textvariable=age)
ageT.place(x=220,y=130)

sexT = Entry(window, textvariable=sex)
sexT.place(x=220,y=155)

bloodT = Entry(window, textvariable=blood)
bloodT.place(x=220,y=180)

contactT=Entry(window,textvariable=contact)
contactT.place(x=220,y=205)

emailT=Entry(window,textvariable=email)
emailT.place(x=220,y=230)


# In[5]:


con = sq.connect('patient.db') #dB browser for sqlite needed
c = con.cursor() #SQLite command, to connect to db so 'execute' method can be called


# In[6]:


def get():
        print("You have submitted a record")
        
        c.execute('CREATE TABLE IF NOT EXISTS '+ 'PATIENT'+ ' (Pname TEXT, Pid INTEGER , Age INTEGER, Sex TEXT,Blood TEXT, Contact INTEGER,email TEXT)') #SQL syntax
        

        c.execute('INSERT INTO ' + 'PATIENT'+ ' (Pname, Pid, Age, Sex, Blood, Contact,email) VALUES (?, ?, ?,?,?,?,?)' , (name.get(),id.get(),age.get(),sex.get(),blood.get(),contact.get(),email.get())) #Insert record into database.
        con.commit()
        #Clear boxes when submit button is hit
        name.set('')
        id.set('')
        age.set('')
        sex.set('')
        blood.set('')
        contact.set('')
        email.set('')
        


# In[7]:


#Clear boxes when submit button is hit
def clear():
    name.set('')
    id.set('')
    age.set('')
    sex.set('')
    blood.set('')
    contact.set('')
    email.set('')


# In[8]:


#to delete entry from the database
def delete():
    c.execute('DELETE FROM PATIENT WHERE Pid=?' ,(id.get(),))
    con.commit()


# In[9]:


def record():
    c.execute('SELECT * FROM PATIENT') #Select from which ever compound lift is selected
    
    window=Tk()
    window.title("Database") 

    window.geometry('480x320+0+0')

    header = Label(window, text="Database", font=("arial",20,"bold"), fg="black").pack()
    
    frame = Frame(window)
    frame.place(x= 10, y = 50)
    
    Lb = Listbox(frame, height = 12, width = 50,font=("arial", 12)) 
    Lb.pack(side = LEFT, fill = Y)
    
    scroll = Scrollbar(frame, orient = VERTICAL) # set scrollbar to list box for when entries exceed size of list box
    scroll.config(command = Lb.yview)
    scroll.pack(side = RIGHT, fill = Y)
    Lb.config(yscrollcommand = scroll.set) 
    

    Lb.insert(0, 'name,id,age,sex,blood,contact,email') #first row in listbox
    
    data = c.fetchall() # Gets the data from the table
    
    for row in data:
        Lb.insert(1,row) # Inserts record row by row in list box

    L7 = Label(window, text = '      ', 
               font=("arial", 12)).place(x=400,y=100) # Title of list box, given which compound lift is chosen

    L8 = Label(window, text = "They are ordered from most recent", 
               font=("arial", 12)).place(x=400,y=350)
    con.commit()


# In[10]:


def message():
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


    PatientFeed = Label( root, text='Patient Feed', fg='white', bg='black', font='Impact 20')
    PatientFeed.pack()
    
    #var1 = StringVar()
    
    #var1.set()

    
    
    
    
    
    
    
 
    def update(): 

        aio = Client("agatanish","eece6c6aa3304338a2349d3c1e0e56f1")

        global oldState



        newState = int(aio.receive("state").value)



        if(oldState != newState):

            if(newState == 1):
                label1 = Label(root, text="Message 1", width=10, fg='white', bg='black',font=("Helvetica", 44)).place(x=80,y=120)
                oldState=newState
                sendSMS("message 1 doctor")
            elif(newState == 2):
                label1 = Label(root, text="Message 2", width=10, fg='white', bg='black',font=("Helvetica", 44)).place(x=80,y=120)
                sendSMS("message 2 doctor")
                oldState=newState
            elif(newState == 3):
                label1 = Label(root, text="Message 3", width=10, fg='white', bg='black',font=("Helvetica", 44)).place(x=80,y=120)
                sendSMS("message 3 doctor")
                oldState=newState
            elif(newState == 4):
                label1 = Label(root, text="Message 4", width=10, fg='white', bg='black',font=("Helvetica", 44)).place(x=80,y=120)
                sendSMS("message 4 doctor")
                oldState=newState
            elif(newState == 5):
                label1 = Label(root, text="Message 5", width=10, fg='white', bg='black',font=("Helvetica", 44)).place(x=80,y=120)
                sendSMS("message 5 doctor")
                #time.sleep(120)
                oldState=newState
            elif(newState == 6):
                #var1.set("message 6")
                label1 = Label(root, text="Message 6", width=10, fg='white', bg='black',font=("Helvetica", 44)).place(x=80,y=120)
                #time.sleep(120)
                oldState=newState
            elif(newState == 7):
                #var1.set("message 7")
                label1 = Label(root, text="Message 7", width=10, fg='white', bg='black',font=("Helvetica", 44)).place(x=80,y=120)
                #time.sleep(120)
                oldState=newState
            elif(newState == 8):
                #var1.set("message 8")
                label1 = Label(root, text="Message 8", width=10, fg='white', bg='black',font=("Helvetica", 44)).place(x=80,y=120)
                #time.sleep(120)
                oldState=newState




        else:
            label1 = Label(root, text="No message", width=10, fg='white', bg='black',font=("Helvetica", 44)).place(x=80,y=120)
            print("no")

    
    
        root.after(1000, update)




    root.after(1000, update)
   
    
    
    


# In[11]:


button_1 = Button(window, text="Submit",command=get)
button_1.place(x=100,y=260)

button_2 = Button(window,text= "Clear",command=clear)
button_2.place(x=10,y=260)
button_3 = Button(window,text="Open DB",command=record)
button_3.place(x=10,y=290)
button_4= Button(window,text="Delete Entry",command=delete)
button_4.place(x=190,y=260)

button_5=Button(window,text="Message",command=message)
button_5.place(x=100,y=290)

button_6=Button(window,text="Visualisation")
button_6.place(x=190,y=290)


# In[12]:



window.mainloop()


# In[ ]:




