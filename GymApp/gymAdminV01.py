import tkinter as tk
from tkinter.font import names
from typing import Text

#THIS IS THE APP THAT WILL BE USED BY ADMINISTRATION


#make a class to add and delete text
#add text by giving a list with start points to add or delete , and it will iterate the lines to start functioning

def makeInputForm(frame,fields):

    entries={}

    for field in fields:
        fieldFrame = tk.Frame(master=frame)
        fieldLabel = tk.Label(master=fieldFrame, width=12, text=field+": ", anchor="w")
        fieldEntry = tk.Entry(master=fieldFrame)
        fieldEntry.insert(0,"0")#maybe change to 'NULL' for string fields?

        fieldFrame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        fieldLabel.pack(side=tk.LEFT)
        fieldEntry.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)

        entries[field]=fieldEntry
    
    return entries

def getInputForm(entries):
    currentEntries={}
    for entry in entries.keys():
        value=entries[entry].get()
        currentEntries[entry]=value

    return currentEntries

def clearInputForm(entries):
    for entry in entries.keys():
        entries[entry].delete(0,"end") #deletes for first til last
        entries[entry].insert(0,"0")

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

        button = tk.Button(master=self, text="Show customer info", command= lambda : addinfo(textbox))
        button.pack()
        button2 = tk.Button(master=self, text="click to clear info", command= lambda : clearinfo(textbox))
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

        messageuser(self, "User has given name:"+entry)

class InputWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, master=parent, bg="green") #now this class is itself the mainframe /Couldnt use super here because tkinter is very old
        self.controller = controller

        label = tk.Label(master=self, text="Welcome to input window")

        label.pack()

        entryFrame=tk.Frame(master=self, bg="red")
        fields = ("FirstName","LastName","AFM","Sex","Salary","Supervisor","Department") #for testing
        entries=makeInputForm(entryFrame,fields)

        ButtonFrame = tk.Frame(master=entryFrame, bg="blue")

        confirmButton = tk.Button(master=ButtonFrame, text="CONFIRM", command=lambda: print(getInputForm(entries))) #add a function to handle confirming
        confirmButton.pack(padx=5,pady=5,side=tk.RIGHT)
        clearButton = tk.Button(master=ButtonFrame, text="Clear", command=lambda: clearInputForm(entries))
        clearButton.pack(side=tk.LEFT)

        ButtonFrame.pack(fill=tk.BOTH,side=tk.BOTTOM)

        entryFrame.pack(padx=10,pady=10)


def main():
    app = GUI()

if __name__ =="__main__":main()