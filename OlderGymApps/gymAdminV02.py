import tkinter as tk
from tkinter.font import names
from typing import Text
import sqlite3

import InputForms as forms

#THIS IS THE APP THAT WILL BE USED BY ADMINISTRATION


class GUI():

    def __init__(self) -> None:

        #tk.Tk.__init__(self) #Could use this to make the GUI a tkinter window
        self.mainWindow = tk.Tk()
        self.mainWindow.title("GYM-CHAIN ADMININISTRATOR")
        self.mainWindow.iconbitmap("icon.ico")

        self.mainWindow.minsize(500,400) #min window size
        self.mainWindow.maxsize(800,800) #max window size
        #self.mainWindow.geometry("400x400")#change window size

        self.mainMenuBar = tk.Menu(master=self.mainWindow)
        self.mainMenuBar.add_command(label="CLICK",command=self.foo)

        self.mainMenuBar.add_command(label="ReturnToMainWindow",command=lambda:self.changeFrame(MainWindow))

        self.mainMenuBar.add_command(label="AddNewCustomer",command=lambda:self.changeFrame(InputWindow))

        self.mainWindow.config(menu=self.mainMenuBar) #Attaches mainMenuBar to mainwindow

        #use the code if its not needed to retain frames
        self.frame = None
        self.changeFrame(MainWindow)
        #self.changeFrame(InputWindow)

        #use the code if its needed to retain frames
        '''self.frames = {}
        for F in (MainWindow): #Add more windows here
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")
        '''

        self.mainWindow.mainloop()


    def changeFrame(self, newFrameClass):
        """This will destroy previous Frame and replace it with a new one"""
        newframe = newFrameClass(self.mainWindow,self)
        if self.frame is not None:
            print("changing frame",self.frame.__class__.__name__,"to:",newFrameClass.__name__)
            self.frame.destroy()
        self.frame = newframe
        self.frame.pack(expand=True,fill=tk.BOTH) #New frame will take up all the screen it can find


    def foo(self):
        print("foo")
    

class MainWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, master=parent) #now this class is itself the mainframe /Couldnt use super here because tkinter is very old
        self.controller = controller

        label = tk.Label(master=self, text="Welcome to MainWindow")

        label.pack()

        idFrame = tk.Frame(master=self, bg ="red")

        idlabel = tk.Label(master=idFrame, text="Customer ID:")
        idlabel.pack(side=tk.LEFT)

        customerId = tk.StringVar(master=idFrame,value="")
        showIdlabel = tk.Label(master=idFrame, textvar=customerId)
        showIdlabel.pack(side=tk.LEFT)

        idFrame.pack(side=tk.TOP,fill=tk.BOTH)

        ButtonFrame = tk.Frame(master=self)
        ButtonFrame.pack(side=tk.TOP)

        infobutton = tk.Button(master=ButtonFrame, text="Show customer info", command= lambda : customerId.set("1234564574"))
        infobutton.pack(side=tk.LEFT)
        clearbutton = tk.Button(master=ButtonFrame, text="click to clear info", command= lambda : customerId.set(""))
        clearbutton.pack(side=tk.LEFT)

        moreinfobutton = tk.Button(master=ButtonFrame, text="Show more customer info", command= lambda : self.showMoreInfo(self,customerId))
        moreinfobutton.pack(side=tk.LEFT)


        entryboxvar =tk.StringVar(master=self)
        entrybox = tk.Entry(master=self, textvariable=entryboxvar)
        entrybox.bind('<Return>', lambda event : self.getentry(event,entrybox, customerId) ) #bind function forces to take into consideration the event that triggers the command
        entrybox.pack(side=tk.TOP)

        textbox = tk.Text(master=self)
        textbox.insert(tk.END,"Customer Information: \n Name: \n Id: \n Trainings left: \n")
        textbox.config(state="disabled")
        #textbox.pack()


    def showMoreInfo(self, frame, customerId):
        """Will create a textbox with more of the customers information"""
        #getinfo()
        fields = {"FirstName":1,"LastName":2,"AFM":3,"Sex":4,"Salary":5,"Supervisor":6,"Department":7} #for testing
        textframe = tk.Frame(master=frame)


        textbox = tk.Text(master=textframe)

        textbox.insert(tk.END,"gasgkasjgasjd\n")

        for field in fields.keys():

            textbox.insert(tk.END,str(fields[field])+"\n")

        textbox.pack(fill=tk.BOTH)
        textframe.pack(side=tk.TOP,fill=tk.BOTH)


    def getentry(self,event, entrybox, outvar):
        """Handles getting the entry when users presses enter
        event= the event that called the function (wont be used now)
        entrybox=the entrybox to get the variable from, outvar=the variable to save the entry to. """

        outvar.set(entrybox.get())
        


class InputWindow(tk.Frame):
    
    def __init__(self, parent, controller):
        """Makes a generic Input window with a Form"""
        tk.Frame.__init__(self, master=parent) #now this class is itself the mainframe /Couldnt use super here because tkinter is very old
        self.controller = controller

        label = tk.Label(master=self, text="Welcome to input window")

        label.pack()

        fields = ("FirstName","LastName","AFM","Sex","Salary","Supervisor","Department") #for testing
        newfields = {"FirstName":1,"LastName":2,"AFM":3,"Sex":4,"Salary":5,"Supervisor":6,"Department":7} #for testing

        self.makeForm(fields,print,lambda: newfields) #can change print to any command we want to take the new data, can change the lambda to any command tha will return the new data

    def makeForm(self, fields, dataHandlerCommand, dataUpdaterCommand=None, initialValues=None):
        """Makes a frame with a form and some buttons to control it.    
        fields=fields for the forms, dataHandlerCommand=the command to be executed when user has inputed new data,
        dataUpdaterCommand=the command to be executed when user wants to update data (It will be used to take data to update the form),
        initialValues= The initial values to be displayed in the form """

        entryFrame=tk.Frame(master=self)

        label = tk.Label(master=entryFrame, text="Please fill out the fields bellow") #change later to display what is being filled out
        label.pack(pady=5,side=tk.TOP)

        fields = ("FirstName","LastName","AFM","Sex","Salary","Supervisor","Department") #for testing
        entries=forms.makeInputForm(entryFrame,fields)

        if initialValues:
            forms.updateInputForm(entries,initialValues) #updating with values already in

        ButtonFrame = tk.Frame(master=entryFrame)

        confirmButton = tk.Button(master=ButtonFrame, text="CONFIRM", command=lambda: dataHandlerCommand(forms.getInputForm(entries))) #confirm button will give the datahandlercommand the data
        confirmButton.pack(padx=5,pady=5,side=tk.RIGHT)
        clearButton = tk.Button(master=ButtonFrame, text="Clear", command=lambda: forms.clearInputForm(entries))
        clearButton.pack(side=tk.LEFT)

        if dataUpdaterCommand is not None:
            updateButton = tk.Button(master=ButtonFrame, text="Update", command=lambda: forms.updateInputForm(entries,dataUpdaterCommand())) #update button will run the dataUpdaterCommand to take data, and update the form
            updateButton.pack(side=tk.LEFT)

        ButtonFrame.pack(fill=tk.BOTH,side=tk.BOTTOM)

        entryFrame.pack(padx=10,pady=10,fill=tk.X)

def main():
    app = GUI()

if __name__ =="__main__":main()