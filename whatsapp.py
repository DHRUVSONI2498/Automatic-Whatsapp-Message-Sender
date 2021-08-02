from tkinter import *
import pywhatkit as kit
import time as t

root = Tk()

def getvals():
    print("it works")
    kit.sendwhatmsg(phoneValue.get(),msgValue.get(),hrValue.get(),minValue.get())

root.geometry("500x300")

Label(root, text="Wellcome to whatsapp automation programm ", font=" Arial 13 bold",pady=25).grid(row=0,column=3)
phone = Label(root,text="Enter the phone No")
msg = Label(root,text="Enter your message")
hr = Label(root,text="Enter time hour    ")
min = Label(root,text="Enter time minute  ")

phone.grid(row= 1 , column=2)
msg.grid(row= 2 , column=2)
hr.grid(row= 3 , column=2)
min.grid(row= 4 , column=2)

phoneValue = StringVar()
msgValue = StringVar()
hrValue = IntVar()
minValue = IntVar()


phoneEntry = Entry(root,textvariable=phoneValue)
msgEntry = Entry(root,textvariable=msgValue)
hrEntry = Entry(root,textvariable=hrValue)
minEntry = Entry(root,textvariable=minValue)

phoneEntry.grid(row = 1 ,column=3)
msgEntry.grid(row = 2,column=3)
hrEntry.grid(row = 3,column=3)
minEntry.grid(row = 4,column=3)

Button(text="SEND MESSAGE",command=getvals).grid(row=7,column=3)

root.mainloop()