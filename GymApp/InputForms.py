import tkinter as tk

def makeInputForm(frame,fields):
    """Creates an input form at specified Frame, making a entry box for each field given"""

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
    """Returns the values in the input form (as a dictionary)"""

    currentEntries={}
    for entry in entries.keys():
        value=entries[entry].get()
        currentEntries[entry]=value

    return currentEntries

def clearInputForm(entries):
    """Clears all the fields, reseting them back to 0"""

    for entry in entries.keys():
        entries[entry].delete(0,"end") #deletes for first til last
        entries[entry].insert(0,"0")

def updateInputForm(entries, newdata):
    """Updates all the fields with the value given in the newdata dictionary"""

    for entry in entries.keys():
        entries[entry].delete(0,"end") 
        entries[entry].insert(0,newdata[entry])
  