import sqlite3
import random 
#https://docs.python.org/3/library/random.html#random.getrandbits
#will use the getrandbits to generate an 8length integer
#this simple program populates some atributes
connection = sqlite3.connect("gym.db")
cursor = connection.cursor()
pk={} #this dictionary will be appended to store tables name:nameOfTablesPrimaryKey ie(employee:afm) | a better practice would be to name every pk as id
#edit: found workaround in new getPrimaryKey() function but it uses experimental stuff

with open("namesAndSurnames.txt","r") as names:

    firstnames,lastnames = names.read().strip().split("\n\n") #in this files first are the names and then the surnames

    firstnames=firstnames.split("\n")
    lastnames=lastnames.split("\n")

with open("sportsAndEquipment.txt", "r") as sportequiment:
    sports,equipment = sportequiment.read().strip().split("\n\n") #in this files first are the sports and then the equipment

    sports = sports.split("\n")
    equipment = equipment.split("\n")

with open("locations.txt", "r") as location:
    locations,addresses = location.read().strip().split("\n\n")

    locations = locations.split("\n")
    addresses = addresses.split("\n")

with open("afms.txt","r") as empafm:
    afms=empafm.read().strip().split("\n")
    #for i in range(len(afms)):
        #afms[i]=int(afms[i])

def execute_sql(cursor,sql):
    """Will execute the sql command given at the cursor given. It will return the cursor so we can do a quick fetch after the querry (i.e. execute_sql(cursor,sql).fetchall())"""

    return cursor.execute(sql)

def create_name():

    f_name=random.choice(firstnames)
    l_name=random.choice(lastnames)

    return f_name,l_name

def create_date(previous_date = "2010-1-1",yearlimit="2022-2-2"):
    """ Create a random date that happens AFTER previous_date."""
    
    p_y, p_m, p_d = (int(i) for i in previous_date.split('-'))
    l_y, l_m, l_d = (int(i) for i in yearlimit.split('-'))

    y = random.randint(p_y, l_y)
    m = random.randint(p_m if y == p_y else 1, 12 if y==p_y else l_m)
    d = random.randint(p_d if m == p_m else 1, (28 if m == 2 else 30) if m==p_y else l_d)

    return "%s-%s-%s" % (y, str(m).zfill(2), str(d).zfill(2))


def populate_gyms(amount):

    def create_gym():

        location=random.choice(locations)
        address=random.choice(addresses)

        return location,address

    for id in range(amount):

        cmd = f"""INSERT INTO gym (location,address) VALUES {create_gym()};""" 

        #print(cmd)
        try:
            execute_sql(cursor,cmd)
        except:
            pass #except failed constraint

def make_gyms():

    #delete table if it existed
    cmd="""DROP TABLE IF EXISTS gym;"""
    execute_sql(cursor,cmd)

    #create table
    cmd="""CREATE TABLE IF NOT EXISTS gym(
        "location" varchar(30) NOT NULL PRIMARY KEY,
        "address" varchar(30) NOT NULL
    );"""
    execute_sql(cursor,cmd)
    populate_gyms(10)

    pk["gym"]="location"


def populate_clients(amount):

    def create_client():

        pnumber="69"+str(random.getrandbits(26))
        cmd="""SELECT afm FROM trainer ORDER BY RANDOM() LIMIT 1"""
        personal_trainer=random.choice(execute_sql(cursor,cmd).fetchone())
        #print(personal_trainer)

        return *create_name(),pnumber,personal_trainer

    for id in range(amount):

        cmd = f"""INSERT INTO client (f_name,l_name,p_number,personal_trainer) VALUES {create_client()};""" #Dont use ({create_client()}) because we would end up with double ()

        #print(cmd)
        execute_sql(cursor,cmd)

def make_clients():

    #delete table if it existed
    cmd="""DROP TABLE IF EXISTS client;"""
    execute_sql(cursor,cmd)

    #create table
    cmd="""CREATE TABLE IF NOT EXISTS client(
        "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        "f_name" varchar(30) NOT NULL,
        "l_name" varchar(30) NOT NULL,
        "p_number" varchar(13) NULL,
        "personal_trainer" integer DEFAULT NULL,

        CONSTRAINT "personal_trainer_fk" FOREIGN KEY("personal_trainer") REFERENCES "personal_trainer"("id") ON DELETE SET NULL
    );"""
    execute_sql(cursor,cmd)
    populate_clients(10)

    pk["client"]="id"


def populate_employees(amount):

    def create_employee():

        afm = random.choice(afms)
        salary=str(random.randint(0,1))+str(random.getrandbits(10))
        #print(salary)

        return afm,*create_name(),salary

    for id in range(amount):
    
        cmd = f"""INSERT INTO employee (afm,f_name,l_name,salary) VALUES {create_employee()};"""  #Dont use ({create_client()}) because we would end up with double ()

        #print(cmd)
        try:
            execute_sql(cursor,cmd)
        except:
            #print("same afm")
            pass

def make_employees():

    #delete table if it existed
    cmd="""DROP TABLE IF EXISTS employee;"""
    execute_sql(cursor,cmd)

    #create table
    cmd="""CREATE TABLE IF NOT EXISTS employee(
        "afm" integer NOT NULL PRIMARY KEY,
        "f_name" varchar(30) NOT NULL,
        "l_name" varchar(30) NOT NULL,
        "salary" integer NOT NULL
    );"""
    execute_sql(cursor,cmd)
    populate_employees(10)
    pk["employee"]="afm"


def populate_rooms(amount):

    def create_room():

        location=random.choice(locations)
        specialty=random.choice(sports)
        last_cleaned=create_date("2021-12-1","2022-01-15") #For random date in sql
        size=random.randint(100,300)

        return location,specialty,last_cleaned,size

    for id in range(amount):
        cmd = f"""INSERT INTO room (location,specialty,last_cleaned,size) VALUES {create_room()};""" #Dont use ({create_client()}) because we would end up with double ()

        #print(cmd)
        execute_sql(cursor,cmd)

def make_rooms():

    #delete table if it existed
    cmd="""DROP TABLE IF EXISTS room;"""
    execute_sql(cursor,cmd)

    #create table
    #datelimit = "2022-01-15" #change later to change when program is run CONSTRAINT 'date_cleaned' CHECK(last_cleaned <= {datelimit}
    cmd=f"""CREATE TABLE IF NOT EXISTS room(
        "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        "location" varchar(30) NOT NULL ,
        "specialty" varchar(30) DEFAULT NULL,
        "last_cleaned" DATE NOT NULL,
        "size" integer NOT NULL,

        CONSTRAINT "location_fk" FOREIGN KEY("location") REFERENCES "gym"("name") ON DELETE CASCADE ON UPDATE CASCADE
    );"""

    execute_sql(cursor,cmd)
    populate_rooms(10)
    pk["room"]="id"


def populate_equipment(amount):

    def create_equipment():

        serial_number=random.choice(afms)
        location=random.choice(locations)
        specialty=random.choice(equipment)
        last_cleaned=create_date("2021-12-1","2022-01-15") #For random date in sql

        return serial_number,location,specialty,last_cleaned

    for id in range(amount):
        cmd = f"""INSERT INTO equipment (serial_number,location,specialty,last_cleaned) VALUES {create_equipment()};""" #Dont use ({create_client()}) because we would end up with double ()

        #print(cmd)
        try:
            execute_sql(cursor,cmd)
        except:
            #print("same serial_number")
            pass #except failed constraint

def make_equipment():

    #delete table if it existed
    cmd="""DROP TABLE IF EXISTS equipment;"""
    execute_sql(cursor,cmd)

    #create table
    #datelimit = "2022-01-15" #change later to change when program is run CONSTRAINT 'date_cleaned' CHECK(last_cleaned <= {datelimit}
    cmd=f"""CREATE TABLE IF NOT EXISTS equipment(
        "serial_number" integer NOT NULL PRIMARY KEY,
        "location" varchar(30) DEFAULT "WAREHOUSE",
        "specialty" varchar(30) DEFAULT NULL,
        "last_cleaned" DATE NOT NULL,

        CONSTRAINT "location_fk" FOREIGN KEY("location") REFERENCES "room"("location") ON DELETE SET DEFAULT ON UPDATE CASCADE
    );"""

    execute_sql(cursor,cmd)
    populate_equipment(10)
    pk["equipment"]="serial_number"

def populate_subscription(amount):

    def create_sport():

        name=random.choice(sports)

        return name

    for id in range(amount):
        cmd = f"""INSERT INTO sport (name) VALUES {create_sport()};""" #Dont use ({create_client()}) because we would end up with double ()

        #print(cmd)
        try:
            execute_sql(cursor,cmd)
        except:
            pass #except failed constraint

def make_subscription():

    #delete table if it existed
    cmd="""DROP TABLE IF EXISTS subscription;"""
    execute_sql(cursor,cmd)

    #create table
    #datelimit = "2022-01-15" #change later to change when program is run CONSTRAINT 'date_cleaned' CHECK(last_cleaned <= {datelimit}
    cmd=f"""CREATE TABLE IF NOT EXISTS subscription(
        "name" varchar(30) NOT NULL PRIMARY KEY,
        "price" integer NOT NULL,
        "start_date" DATE NOT NULL,
        "end_date" DATE NOT NULL,
        "description" varchar(30) DEFAULT NULL
    );"""

    execute_sql(cursor,cmd)
    populate_subscription(10)
    pk["subscription"]="name"


def populate_sports(amount):

    def create_subscription():

        start_date=create_date("2021-12-1","2022-01-15")

        p_y, p_m, p_d = (int(i) for i in start_date.split('-'))

        y = random.randint(p_y, 2023)
        m = random.randint(p_m if y == p_y else 1, 12 )
        d = 28 if m == 2 else 30

        end_date="%s-%s-%s" % (y, str(m).zfill(2), str(d).zfill(2))

        name=random.choice(sports)+str(m)+str(y)
        price= (m-p_m if p_y==y else abs(m-p_m) + 12* abs(y-p_y)) * 100
        description=random.choice(equipment)

        return name,price,start_date,end_date,description

    for id in range(amount):
        cmd = f"""INSERT INTO subscription (name,price,start_date,end_date,description) VALUES {create_subscription()};""" #Dont use ({create_client()}) because we would end up with double ()

        #print(cmd)
        try:
            execute_sql(cursor,cmd)
        except:
            pass #except failed constraint

def make_sports():

    #delete table if it existed
    cmd="""DROP TABLE IF EXISTS sport;"""
    execute_sql(cursor,cmd)

    #create table
    #datelimit = "2022-01-15" #change later to change when program is run CONSTRAINT 'date_cleaned' CHECK(last_cleaned <= {datelimit}
    cmd=f"""CREATE TABLE IF NOT EXISTS sport(
        "name" varchar(30) NOT NULL PRIMARY KEY
    );"""

    execute_sql(cursor,cmd)
    populate_sports(10)
    pk["sport"]="name"


def populate_specialists():
    cmd="""SELECT afm FROM employee;"""
    results=execute_sql(cursor,cmd).fetchall()

    
    for afm in results:
        if random.getrandbits(1):
            cmd = f"""INSERT INTO generalstaff (afm) VALUES ({afm[0]});""" #need to use [0] because afm is a tuple of len 1
        else:
            cmd = f"""INSERT INTO trainer (afm) VALUES ({afm[0]});"""
        #print(cmd)
        execute_sql(cursor,cmd)

def make_specialists():

    #delete table if it existed
    cmd="""DROP TABLE IF EXISTS generalstaff;"""
    execute_sql(cursor,cmd)

    #create table
    cmd=f"""CREATE TABLE IF NOT EXISTS generalstaff(
        "afm" varchar(30) NOT NULL PRIMARY KEY,
        
        CONSTRAINT "afm_fk" FOREIGN KEY("afm") REFERENCES "employee"("afm") ON DELETE CASCADE ON UPDATE CASCADE
    );"""
    
    execute_sql(cursor,cmd)
    pk["generalstaff"]="afm"

    #delete table if it existed
    cmd="""DROP TABLE IF EXISTS trainer;"""
    execute_sql(cursor,cmd)

    #create table
    cmd=f"""CREATE TABLE IF NOT EXISTS trainer(
        "afm" varchar(30) NOT NULL PRIMARY KEY,

        CONSTRAINT "afm_fk" FOREIGN KEY("afm") REFERENCES "employee"("afm") ON DELETE CASCADE ON UPDATE CASCADE
    );"""


    execute_sql(cursor,cmd)
    pk["trainer"]="afm"
    populate_specialists()



def getInfo(table,key):
    """Get all info of a object in a table with the key given"""

    cmd=f"""SELECT * FROM {table} WHERE {pk[table]}={key};"""

    #print(cmd)
    try:
        return execute_sql(cursor,cmd).fetchone()
    except Exception as e: #for any expection will enter and name it e (since Exception class is God class for all exceptions)
        print(e)
        #raise e #can uncomment in order to stop program

def getTableNames():
    """returns tuple with all the table names in db"""

    tables=[]
    for table in execute_sql(cursor,"""SELECT name sql FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%';""").fetchall(): #this will return all the tables in the db using sqlite wizardry link:https://www.sqlitetutorial.net/sqlite-tutorial/sqlite-show-tables/
        tables.append(table[0]) #have to use table[0] because table name is a 1 value tuple

    return tuple(tables)

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

def getPrimaryKey(table) -> tuple:
    """Will return the name(s) of the primary key(s) column in the given table (it will return a tuple)"""
    columns=[]
    #selecting from pragmas link:https://stackoverflow.com/questions/6888581/is-there-an-equivalent-select-statement-for-pragma-table-infomytable-in-sqli/50951476
    cmd=f"""SELECT name FROM pragma_table_info("{table}") WHERE pk=1;""" #will select the name of each column that is a pk
    #print(cmd)
    for column in execute_sql(cursor,cmd).fetchall():
        columns.append(column[0])

    return tuple(columns)

def getTableInfo(table) -> tuple:
    """Will return tuple with column names and pk_column of given table"""
    col_names=getcolumnNames(table)
    pk=getPrimaryKey(table)
    return col_names,pk

def getAllTablesInfo():
    """Will print info for all tables"""
    names=getTableNames()
    for name in names:
        col_names,pk = getTableInfo(name)
        print(f"table {name} has columns {col_names} with column: {pk[0]} being its primary key")

make_gyms()
make_employees()
make_specialists()
make_rooms()
make_equipment()
make_sports()
make_subscription()
make_clients()


'''print(getInfo("client","1"))
print(getInfo("employee","123456789"))
print(getInfo("room","1"))
print(getInfo("equipment","123456789"))
print(getInfo("subscription","1"))'''

#print(pk) #print primary key names

#print(execute_sql(cursor,"""SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%';""").fetchall()) #this will return all the tables in the db using sqlite wizardry link:https://www.sqlitetutorial.net/sqlite-tutorial/sqlite-show-tables/
#print(execute_sql(cursor,"""PRAGMA table_info('client');""").fetchall()) #this will return information about each column of given_table using sqlite wizardry link:https://stackoverflow.com/questions/947215/how-to-get-a-list-of-column-names-on-sqlite3-database


'''for table in execute_sql(cursor,"""SELECT name sql FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%';""").fetchall():
    print("\ntable=",table[0])

    for column in execute_sql(cursor,f"""PRAGMA table_info("{table[0]}");""").fetchall(): #have to use table[0] because table name is a 1 value tuple
        print("column name=",column[1],"     IsPrimarykey=",column[5])
'''

#getAllTablesInfo()

connection.commit()
connection.close()