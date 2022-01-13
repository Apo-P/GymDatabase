import tkinter as tk
from tkinter.font import names
from typing import Text

#THIS IS THE APP THAT WILL BE USED BY REGULAR EMPLOYEES


#make a class to add and delete text
#add text by giving a list with start points to add or delete , and it will iterate the lines to start functioning

class GUI():

    def __init__(self) -> None:

        #tk.Tk.__init__(self) #Could use this to make the GUI a tkinter window
        self.mainWindow = tk.Tk()
        self.mainWindow.title("GYM-CHAIN ADMININISTRATOR")
        self.mainWindow.iconbitmap(self.mainWindow,default="icon.ico")

        self.mainWindow.minsize(500,400) #min window size
        self.mainWindow.maxsize(800,800) #max window size
        #self.mainWindow.geometry("400x400")#change window size

        self.mainMenuBar = tk.Menu(master=self.mainWindow)
        self.mainMenuBar.add_command(label="CLICK",command=self.foo)

        self.mainMenuBar.add_command(label="ReturnToMainWindow",command=lambda:self.changeFrame(MainWindow))


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
        self.frame.pack()


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


def main():
    app = GUI()

if __name__ =="__main__":main()