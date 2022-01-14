import tkinter as tk
from tkinter.font import names
from typing import Text

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

        labels=[]

        label = tk.Label(master=self, text="Welcome to MainWindow")

        label.pack()

        label2 = tk.Label(master=self, text="Customer ID:")
        label2.pack()

        textbox = tk.Text(master=self)
        textbox.insert(tk.END,"Customer Information: \n Name: \n Id: \n Trainings left: \n")
        textbox.config(state="disabled")

        button = tk.Button(master=self, text="Show customer info", command= lambda : print('addinfo(textbox)'))
        button.pack()
        button2 = tk.Button(master=self, text="click to clear info", command= lambda : print('clearinfo(textbox)'))
        button2.pack()
        self.name=""
        self.entrybox = tk.Entry(master=self, textvariable=self.name)
        self.entrybox.bind('<Return>',self.getentry)
        self.entrybox.pack()

        textbox.pack()



    def getentry(self, event):
        """Handles getting the entry when users presses enter"""

        #print("bruh")
        entry=self.entrybox.get()
        if entry =="":entry="name not given"
        print(entry)
        self.entrybox.delete("0","end")

        print("messageuser")#messageuser(self, "User has given name:"+entry)


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