import tkinter as tk
from tkinter.font import names
from typing import Text

def clearinfo(textbox:tk.Text):
    textbox.config(state="normal")
    #print("deleting")
    textbox.delete("2.7","2.end") #deleting name
    textbox.delete("3.5","3.end") #deleting id
    textbox.delete("4.17","4.end") #deleting trainings

    textbox.config(state="disabled")

def addinfo(textbox:tk.Text):
    textbox.config(state="normal")
    #print("inserting")
    textbox.insert("2.7","ALSDKASLD") #inserting name
    textbox.insert("3.5","6465465") #inserting id
    textbox.insert("4.17","6969") #inserting trainings

    textbox.config(state="disabled")

def messageuser(frame:tk.Frame, msg:str):
    """display a message notification to user"""
    return
    msgbox=tk.Message(master=frame, text=msg)
    msgbox.pack()
    message = tk.Toplevel(tk.Tk())

#make a class to add and delete text
#add text by giving a list with start points to add or delete , and it will iterate the lines to start functioning

class GUI():

    def __init__(self) -> None:

        window = tk.Tk()
        self.frame = tk.Frame()

        labels=[]

        label = tk.Label(master=self.frame, text="Hello there")

        label.pack()

        label2 = tk.Label(master=self.frame, text="Customer ID:")
        label2.pack()

        textbox = tk.Text(master=self.frame)
        textbox.insert(tk.END,"Customer Information: \n Name: \n Id: \n Trainings left: \n")
        textbox.config(state="disabled")

        button = tk.Button(master=self.frame, text="Show customer info", command= lambda : addinfo(textbox))
        button.pack()
        button2 = tk.Button(master=self.frame, text="click to clear info", command= lambda : clearinfo(textbox))
        button2.pack()
        self.name=""
        self.entrybox = tk.Entry(master=self.frame, textvariable=self.name)
        self.entrybox.bind('<Return>',self.getentry)
        self.entrybox.pack()

        textbox.pack()



        self.frame.pack()

        window.mainloop()

    def getentry(self, event):
        """Handles getting the entry when users presses enter"""

        #print("bruh")
        entry=self.entrybox.get()
        if entry =="":entry="name not given"
        print(entry)
        self.entrybox.delete("0","end")

        messageuser(self.frame, "User has given name:"+entry)

def main():
    app = GUI()

if __name__ =="__main__":main()