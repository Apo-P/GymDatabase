#Import the required Libraries
from tkinter import *
from tkinter import ttk

#Create an instance of Tkinter frame
win = Tk()

#Set the geometry of Tkinter frame
win.geometry("750x350")

#Define a function to submit the validate the value of Entry widget
def submit_name():
   Label(frame, text="Hello "+ entry1.get(), font=('Helvetica',12, 'bold')).pack(pady=20)
   Label(frame, text= "Your Email is : "+ entry2.get(), font=('Helvetica',12, 'bold')).pack(pady=12)

#Creates a Frame
frame = LabelFrame(win, width= 400, height= 180, bd=3)
frame.pack()


#Create an Entry widget in the Frame for Accepting the Username
entry1 = ttk.Entry(frame, width= 40)
entry1.insert(INSERT, "Enter Your Name")
entry1.pack(ipadx= 30, ipady=30)

#Set the focus on Entry1
#entry1.focus_set()

#Create an Entry Widget to accept the email Address of the User
entry2 = ttk.Entry(frame, width= 40)
entry2.insert(INSERT, "Enter Your Email")
entry2.pack(pady=10)

#Create a submit button
submit= ttk.Button(win, text= "submit",command=submit_name)
submit.pack(pady=10)

win.mainloop()