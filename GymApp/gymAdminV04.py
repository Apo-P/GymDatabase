import tkinter as tk
from tkinter.font import names
from typing import Text
import tkinter.messagebox #import messagebox (it isnt included by default)

import sqlite3

import InputForms as forms

#THIS IS THE APP THAT WILL BE USED BY ADMINISTRATION

#Database location and a global cursor to use in the program
connection = sqlite3.connect("gym.db")
cursor = connection.cursor()

def execute_sql(cursor,sql):
    """Will execute the sql command given at the cursor given. It will return the cursor so we can do a quick fetch after the querry (i.e. execute_sql(cursor,sql).fetchall())"""

    return cursor.execute(sql)

def getcolumnNames(table)-> tuple:
    """Will return column names of table given"""
    columns=[]

    #"""PRAGMA table_info('given_table');""" #this will return information about each column of given_table using sqlite wizardry link:https://stackoverflow.com/questions/947215/how-to-get-a-list-of-column-names-on-sqlite3-database
    #selecting from pragmas link:https://stackoverflow.com/questions/6888581/is-there-an-equivalent-select-statement-for-pragma-table-infomytable-in-sqli/50951476

    cmd=f"""SELECT name FROM pragma_table_info("{table}");""" #will select the name of each column
    #print(cmd)
    for column in execute_sql(cursor,cmd).fetchall():
        columns.append(column[0])

    return tuple(columns)

def push_data(table,data):
    """will Insert data into table given (data must be a dictionary with key the field names)"""

    print(data)
    attr=[]
    values=[]
    for field in data:
        attr.append(field)
        if data[field].isnumeric(): #NEEDS FIX formating should be dependant on type , this is a quickfix
            values.append(int(data[field])) 
        elif data[field]=="":
             values.append("NULL") 
        else:
            values.append(data[field]) 
        print(attr,values)

    attr=tuple(attr)
    values=tuple(values)

    cmd=f"""INSERT INTO {table} {attr} VALUES {values};"""
    print(cmd)
    execute_sql(cursor,cmd)

def commit_changes():
    connection.commit()

def get_customer_info(customer_id):
    """Gets customer info that is necessary for everyday operations"""

    cmd = f"""SELECT * FROM client WHERE id={customer_id}"""
    basic_info=execute_sql(cursor,cmd).fetchone()

class GUI():

    def __init__(self) -> None:

        #tk.Tk.__init__(self) #Could use this to make the GUI a tkinter window
        self.mainWindow = tk.Tk()
        self.mainWindow.title("GYM-CHAIN ADMININISTRATOR")
        self.mainWindow.iconbitmap("icon.ico")

        self.mainWindow.minsize(600,400) #min window size
        self.mainWindow.maxsize(800,800) #max window size
        #self.mainWindow.geometry("400x400")#change window size

        self.mainWindow.protocol("WM_DELETE_WINDOW", self.close_app) #will run the close app when user clicks the exit button

        self.mainMenuBar = tk.Menu(master=self.mainWindow)
        #self.mainMenuBar.add_command(label="CLICK",command=self.foo)

        self.mainMenuBar.add_command(label="ReturnToMainWindow",command=lambda:self.changeFrame(MainWindow))

        self.mainMenuBar.add_command(label="AddNewCustomer",command=lambda:self.changeFrame(CustomerInput))

        self.mainMenuBar.add_command(label="SearchCustomers",command=lambda:self.changeFrame(CustomerSearch))

        self.mainMenuBar.add_command(label="SQLWindow",command=lambda:self.changeFrame(SQLWindow))

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


    def close_app(self):
        """This will run when user presses the close bytton"""

        if tk.messagebox.askyesno("Quit", "Do you want to quit?"):

            connection.close() #close connection to database 
            print("connection to db closed")
            self.mainWindow.destroy() #destroy app
            exit() #exit python (just in case anything remained open)

    def foo(self):
        print("foo")
    

class MainWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, master=parent) #now this class is itself the mainframe /Couldnt use super here because tkinter is very old
        self.controller = controller

        idFrame = tk.Frame(master=self)
        idFrame.pack(side=tk.TOP,fill=tk.BOTH)

        idlabel = tk.Label(master=idFrame, text="Customer ID:")
        idlabel.pack(side=tk.LEFT)

        customerId = tk.StringVar(master=idFrame,value="")
        showIdlabel = tk.Label(master=idFrame, textvar=customerId)
        showIdlabel.pack(side=tk.LEFT)


        ButtonFrame = tk.Frame(master=self)
        ButtonFrame.pack(side=tk.TOP, fill=tk.X)

        infobutton = tk.Button(master=ButtonFrame, text="Show customer info", command= lambda : self.showMoreInfo(self,customerId))
        infobutton.pack(side=tk.LEFT)
        clearbutton = tk.Button(master=ButtonFrame, text="click to clear info", command= lambda : customerId.set(""))
        clearbutton.pack(side=tk.LEFT)


        entryFrame = tk.Frame(master=ButtonFrame)
        entryFrame.pack(side = tk.RIGHT)

        entryboxvar =tk.StringVar(master=entryFrame)
        entrybox = tk.Entry(master=entryFrame, textvariable=entryboxvar)
        entrybox.bind('<Return>', lambda event : self.getentry(event,entrybox, customerId) )
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
    
    def __init__(self, parent, controller,input_table):
        """Makes a generic Input window with a Form for the table given"""
        tk.Frame.__init__(self, master=parent) #now this class is itself the mainframe /Couldnt use super here because tkinter is very old
        self.controller = controller

        #label = tk.Label(master=self, text="Welcome to input window")
        #label.pack()

        #fields = ("FirstName","LastName","AFM","Sex","Salary","Supervisor","Department") #for testing
        #newfields = {"FirstName":1,"LastName":2,"AFM":3,"Sex":4,"Salary":5,"Supervisor":6,"Department":7} #for testing

        #self.makeForm(fields,print,lambda: newfields) #can change print to any command we want to take the new data, can change the lambda to any command tha will return the new data
        self.table=input_table
        fields = getcolumnNames(self.table)
        print(fields)

        self.makeForm(fields,self.insert_data)

    def makeForm(self, fields, dataHandlerCommand, dataUpdaterCommand=None, initialValues=None):
        """Makes a frame with a form and some buttons to control it.    
        fields=fields for the forms, dataHandlerCommand=the command to be executed when user has inputed new data,
        dataUpdaterCommand=the command to be executed when user wants to update data (It will be used to take data to update the form),
        initialValues= The initial values to be displayed in the form """

        entryFrame=tk.Frame(master=self)

        label = tk.Label(master=entryFrame, text="Please fill out the fields bellow") #change later to display what is being filled out
        label.pack(pady=5,side=tk.TOP)

        #fields = ("FirstName","LastName","AFM","Sex","Salary","Supervisor","Department") #for testing
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

    def insert_data(self,data):
        print("inserting data")
        print(data)
        try:
            push_data(self.table,data) 
            commit_changes()
        except Exception as e:
            tkinter.messagebox.showwarning(message=f"ERROR:{e}")
            #raise e

class CustomerInput(InputWindow):
    def __init__(self, parent, controller):
        """Makes an input window for a customer"""
        super(CustomerInput,self).__init__(parent, controller,"client")


class DisplayWindow (tk.Frame):
    
    def __init__(self, parent, controller,columns,data=None):
        """Makes a generic Display window for columns and data given,
        Format should be columnNames=("col1","col2",...,"coln") data=(("col1-data","col2-data",...,"coln-data"),("col1-data","col2-data",...,"coln-data"),....) """
        tk.Frame.__init__(self, master=parent) #now this class is itself the mainframe /Couldnt use super here because tkinter is very old
        self.controller = controller

        #label = tk.Label(master=self, text="Welcome to Display window")
        #label.pack(side=tk.TOP)

        #columns = ("FirstName","LastName","PhoneNumber","Trainer") #for testing
        #data = (("Smith","Smithpoulos","6912345678",""),("John","Johnopoulos","6923456789","12345678"))

        self.displayFrame=tk.Frame(master=self,bg="red")
        self.displayFrame.pack(side=tk.TOP,fill=tk.BOTH,expand=True)

    

        self.makeColumnLabels(columns)
        self.displayData(data)

        #self.updateDisplay((("Smith","Smithpoulos","6912345678",""),),(("John","Johnopoulos","6923456789","123456789"),)) #prosoxi sto input giati prepei na einai panta tuple apo tuples

    def makeColumnLabels(self,columnNames):
        self.columnFrame = tk.Frame(master=self.displayFrame)
        self.columnFrame.pack(side=tk.TOP, fill=tk.X)
        for column in columnNames:
            print(column)
            columnLabel = tk.Label(master=self.columnFrame,width=14,padx=3, text=column) #padx maybe change?
            columnLabel.pack(side=tk.LEFT)

    def displayData(self,all_data:tuple):
        self.dataFrame = tk.Frame(master=self.displayFrame)
        self.dataFrame.pack(side=tk.TOP, fill=tk.BOTH)
        self.dataFrames={}
        if all_data:
            for data in all_data:
                dataFrame = tk.Frame(master=self.dataFrame)
                dataFrame.pack(side=tk.TOP, fill=tk.X)
                self.dataFrames[data]=dataFrame #store where in which frame data is stored
                for column in data:
                    dataLabel=tk.Label(master=dataFrame,width=14,padx=3,text=column)
                    dataLabel.pack(side=tk.LEFT)

    def updateDisplay(self,old_data,newdata):
        """Will update the display on the old_data given with the new data
        old_data must be tuple of tuples always
        newdata must be tuple of tuples always"""
        #old_data is the karnofell code (Inscryption)
        i=0
        for data in old_data:
            dataFrame=self.dataFrames[data]
            j=0
            for label in dataFrame.winfo_children():
                label.config(text=newdata[i][j])
                j+=1
            i+=1

    def addData(self,all_data):
        for data in all_data:
            dataFrame = tk.Frame(master=self.dataFrame)
            dataFrame.pack(side=tk.TOP, fill=tk.X)
            self.dataFrames[data]=dataFrame #store where in which frame data is stored
            for column in data:
                dataLabel=tk.Label(master=dataFrame,width=14,padx=3,text=column)
                dataLabel.pack(side=tk.LEFT)

    def clearData(self):
        for data in self.dataFrames:
            #print(f"data {data} has")
            frame=self.dataFrames[data]
            #print(frame)
            try:
                self.dataFrames[data].destroy()
            except:
                pass
        self.dataFrames={} #reset keys


class SearchWindow(tk.Frame):

    def __init__(self, parent, controller,table):
        """Makes a search window for table given"""
        tk.Frame.__init__(self, master=parent) #now this class is itself the mainframe /Couldnt use super here because tkinter is very old
        self.controller = controller

        label = tk.Label(master=self, text=f"Searching for {table}")

        label.pack(side=tk.TOP)


        self.make_search_window(table)


    def make_search_window(self,searchTable):

        self.searchFrame=tk.Frame(master=self) #,bg="blue"
        self.searchFrame.pack(side=tk.TOP,fill=tk.BOTH,expand=True)
        
        self.configConfirmFrame=tk.Frame(master=self.searchFrame)
        self.configConfirmFrame.pack(side=tk.TOP,fill=tk.X)

        self.configFrame =tk.Frame(master=self.configConfirmFrame)
        self.configFrame.pack(side=tk.LEFT,fill=tk.X)


        self.buttonoptions = {} #here we will store which buttons have been pressed
        self.entries={}
        i=0
        print(getcolumnNames(searchTable))
        for column in getcolumnNames(searchTable):
            print(column)
            optionbutton = tk.Button(master=self.configFrame,width=14, text=column) 
            optionbutton.config(command=lambda optionbutton=optionbutton,column=column:self.toggleColumn(optionbutton,column))#Attention in the lambda Use default parameter to avoid late-binding issue link:https://stackoverflow.com/questions/27198287/tkinter-create-multiple-buttons-with-different-command-function
            self.buttonoptions[column]=[i,False] #stores column position and state
            optionbutton.grid(column=i,row=0)
            i+=1

        searchButton = tk.Button(master=self.configConfirmFrame, text="confirm",bg="green")
        searchButton.config(command=lambda:self.do_search(searchTable))
        searchButton.pack(side=tk.LEFT,padx=10,fill=tk.BOTH)

        self.displayWindow=DisplayWindow(self.searchFrame,self,getcolumnNames(searchTable))
        self.displayWindow.pack(side=tk.TOP,fill=tk.BOTH,expand=True)


    def toggleColumn(self,button:tk.Button, column):
        #print(column)
        if self.buttonoptions[column][1]: #if button was already pressed
            self.buttonoptions[column][1]=False
            button.config(relief="raised")
            self.entries[column].destroy()
            self.entries.pop(column)
        else: #If button wasnted pressed
            self.buttonoptions[column][1]=True
            button.config(relief="sunken")
            entry = tk.Entry(master=self.configFrame, width=14)
            entry.grid(column=self.buttonoptions[column][0], row=1)
            self.entries[column] = entry
        #print(self.entries)

    def do_search(self,searchTable):
        print("searching")

        cmd= f"""SELECT * FROM {searchTable}"""

        cmdExt=""""""
        for column in self.entries:
            #print(column)
            searchitem=self.entries[column].get()
            if searchitem:
                if searchitem.isnumeric(): #NEEDS FIX formating should be dependant on type , this is a quickfix
                    cmdExt += f""" {column}={searchitem},""" 
                else:
                    cmdExt += f""" {column}="{searchitem}",""" 
            else:
                print("noinput")

        if cmdExt!="""""":cmd += """ WHERE"""+cmdExt[:-1] #if there is anything to search for (cmdExt[:-1] remove last comma)

        cmd+=""" ;"""

        print(cmd)
        self.do_sql(cmd)

    def do_sql(self,cmd):
        self.displayWindow.clearData()
        results=execute_sql(cursor,cmd).fetchall()
        self.displayWindow.addData(results)

class CustomerSearch(SearchWindow):
    def __init__(self,parent,controller):
        super(CustomerSearch,self).__init__(parent,controller,"client")




class SQLWindow(tk.Frame):
    """A passworded window where admins can execute sql"""

    def __init__(self, parent, controller):
            """Makes a generic Display window"""
            tk.Frame.__init__(self, master=parent) #now this class is itself the mainframe /Couldnt use super here because tkinter is very old
            self.controller = controller

            self.passwordFrame = tk.Frame(master=self)
            self.passwordFrame.pack(fill=tk.BOTH)

            label = tk.Label(master=self.passwordFrame, text="Welcome to SQL window")
            label.pack(side=tk.TOP)

            password_label = tk.Label(master=self.passwordFrame, text="Please type Admin Password")
            password_label.pack(side=tk.TOP)

            password_typed = tk.StringVar(master=self)
            password_entry = tk.Entry(master=self.passwordFrame, textvariable=password_typed)
            password_entry.bind('<Return>', lambda event : self.getpassword(event,password_entry) )
            password_entry.pack(side=tk.TOP)
            
    def getpassword(self,event,password_entry):
        givenpassword=password_entry.get()
        if givenpassword=="BaseisDedomenwn2022":
            self.show_sql()
        else:
            tkinter.messagebox.showwarning(message="PASSWORD IS WRONG")



    def show_sql(self):
        """If password was correct show sql"""
        self.passwordFrame.destroy()

        sqlFrame = tk.Frame(master=self)
        sqlFrame.pack(fill=tk.BOTH)

        sqlLabel = tk.Label(master=sqlFrame, text="Please type SQL Querry in the entry below")
        sqlLabel.pack(side=tk.TOP,fill=tk.X)

        sqlEntry = tk.Entry(master=sqlFrame)
        sqlEntry.bind('<Return>', lambda event : self.do_sql(event,sqlEntry.get()) )
        sqlEntry.pack(side=tk.TOP,fill=tk.X)

        self.sqlResults = tk.Text(master=sqlFrame, state="disabled")
        self.sqlResults.pack(side=tk.TOP,fill=tk.BOTH)


    def do_sql(self,event,sqlEntry):
        self.sqlResults.config(state="normal")
        self.sqlResults.delete("1.0","end")
        try:
            results=execute_sql(cursor,sqlEntry).fetchall()
            if results:
                i=1
                for result in results:
                    self.sqlResults.insert(tk.END,f"{result}\n")
                    i+=1
            else:
                self.sqlResults.insert("1.0","No results!")
        except Exception as e:
            #raise e
            self.sqlResults.insert("1.0",f"Something was wrong! Here is the error\n{e}")

        self.sqlResults.config(state="disabled")
        

def main():
    app = GUI() #runprogram

    #print(getUserInfo("1"))
    #connection.close()

if __name__ =="__main__":main()