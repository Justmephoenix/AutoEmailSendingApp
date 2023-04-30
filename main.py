
from ast import Str
from http import server
import tkinter
from tkinter import *
import smtplib
from tokenize import String
#Main screen
obj=Tk()
obj.title('Custom E-mail app')


#Functions
def Send():
    try:
        username=temp_username.get()
        password=temp_password.get()
        to=temp_receiver.get()
        subject=temp_subject.get()
        body=temp_body.get()
        if username=="" or password=="" or to=="" or subject=="" or body=="":
            notif.config(text="All fields are required to be fill up ...",fg="red")
            return
        else:
            finalMessage='Subject: {}\n\n{}'.format(subject,body)
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(username,password)
            server.send(username,to,finalMessage)
            notif.config(tetx='Email has been sent ',fg="green")
    except:
        notif.config(text='Error in sending email',fg="green")

def Reset():
    usernameEntry.delete(0,'end')
    passwordEntry.delete(0,'end')
    receiverEntry.delete(0,'end')
    subjectEntry.delete(0,'end')
    bodyEntry.delete(0,'end')

#Graphics
titleLabel=Label(obj,text="Custom E-mail App",font=('Calibri',15)).grid(row=0,sticky=N)
Label(obj,text="Use the form below to send an email",font=('Calibri',11)).grid(row=1,sticky=W,padx=5)

Label(obj,text="Email",font=('Calibri',11)).grid(row=2,sticky=W,padx=5)
Label(obj,text="Password",font=('Calibri',11)).grid(row=3,sticky=W,padx=5)
Label(obj,text="To",font=('Calibri',11)).grid(row=4,sticky=W,padx=5)
Label(obj,text="Subject",font=('Calibri',11)).grid(row=5,sticky=W,padx=5)
Label(obj,text="Body",font=('Calibri',11)).grid(row=6,sticky=W,padx=5)

notif=Label(obj,text="",font=('Calibri',11))
notif.grid(row=7,sticky=S,padx=5)

#Storage
temp_username=StringVar()
temp_password=StringVar()
temp_receiver=StringVar()
temp_subject=StringVar()
temp_body=StringVar()

#Entries
usernameEntry=Entry(obj,textvariable=temp_username)
usernameEntry.grid(row=2,column=0)

passwordEntry=Entry(obj,show="*",textvariable=temp_password)
passwordEntry.grid(row=3,column=0)

receiverEntry=Entry(obj,textvariable=temp_receiver)
receiverEntry.grid(row=4,column=0)

subjectEntry=Entry(obj,textvariable=temp_subject)
subjectEntry.grid(row=5,column=0)

bodyEntry=Entry(obj,textvariable=temp_body)
bodyEntry.grid(row=6,column=0)

#Buttons
Button(obj,text="Send",command=Send).grid(row=7,sticky=W,pady=15,padx=5)
Button(obj,text="Reset",command=Reset).grid(row=7,sticky=W,pady=45,padx=45)




obj.mainloop()