import sqlite3
import random 
#https://docs.python.org/3/library/random.html#random.getrandbits
#will use the getrandbits to generate an 8length integer
#this simple program populates some atributes
connection = sqlite3.connect("gym.db")
cursor = connection.cursor()


with open("namesAndSurnames.txt","r") as names:

    firstnames,lastnames = names.read().strip().split("\n\n") #in this files first are the names and then the surnames

    firstnames=firstnames.split("\n")
    lastnames=lastnames.split("\n")

with open("sportsAndEquipment.txt", "r") as sportequiment:
    sports,equipment = sportequiment.read().strip().split("\n\n") #in this files first are the sports and then the equipment

    sports = sports.split("\n")
    equipment = equipment.split("\n")

with open("locations.txt", "r") as location:
    locations = location.read().strip().split("\n")

with open("afms.txt","r") as empafm:
    afms=empafm.read().strip().split("\n")

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


def populate_clients(amount):

    def create_client():

        pnumber="69"+str(random.getrandbits(26))
        cmd="""SELECT afm FROM personal_trainer ORDER BY RANDOM() LIMIT 1"""
        personal_trainer=random.choice(execute_sql(cursor,cmd).fetchone())

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
        "personal_trainer" integer DEFAULT NULL

        CONSTRAINT "personal_trainer_fk" FOREIGN KEY("personal_trainer") REFERENCES "personal_trainer"("id") ON DELETE SET NULL
    );"""
    execute_sql(cursor,cmd)
    populate_clients(10)


def populate_employees(amount):

    def create_employee():

        afm = random.choice(afms)

        salary=str(random.randint(0,1))+str(random.getrandbits(9))

        return afm,*create_name(),salary

    for id in range(amount):
        cmd = f"""INSERT INTO employee (afm,f_name,l_name,salary) VALUES {create_employee()};""" #Dont use ({create_client()}) because we would end up with double ()

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
        "size" integer NOT NULL

 
    );"""

    execute_sql(cursor,cmd)
    populate_rooms(10)


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
            pass

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
        "last_cleaned" DATE NOT NULL

        CONSTRAINT "location_fk" FOREIGN KEY("location") REFERENCES "room"("location") ON DELETE SET DEFAULT ON UPDATE CASCADE
    );"""

    execute_sql(cursor,cmd)
    populate_equipment(10)


def populate_subscription(amount):

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
            #print("same serial_number")
            pass

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
    populate_equipment(10)

def make_specialists(amount):

    #delete table if it existed
    cmd="""DROP TABLE IF EXISTS generalstaff;"""
    execute_sql(cursor,cmd)

    #create table
    cmd=f"""CREATE TABLE IF NOT EXISTS trainer(
        "afm" varchar(30) NOT NULL PRIMARY KEY

        CONSTRAINT FOREIGN KEY("afm") REFERENCES "employees"("afm") ON DELETE CASCADE ON UPDATE CASCADE
    );"""

    #delete table if it existed
    cmd="""DROP TABLE IF EXISTS trainer;"""
    execute_sql(cursor,cmd)

    #create table
    cmd=f"""CREATE TABLE IF NOT EXISTS trainer(
        "afm" varchar(30) NOT NULL PRIMARY KEY

        CONSTRAINT FOREIGN KEY("afm") REFERENCES "employees"("afm") ON DELETE CASCADE ON UPDATE CASCADE
    );"""


    execute_sql(cursor,cmd)
    populate_equipment(10)


def getUserInfo(userId):
    """Returns all info on user requested by id"""

    cmd=f"""SELECT * FROM client WHERE id={userId};"""

    return execute_sql(cursor,cmd).fetchone()

def getEmployeeInfo(afm):
    """Returns all info on Employee requested by afm"""

    cmd=f"""SELECT * FROM employee WHERE afm={afm};"""

    return execute_sql(cursor,cmd).fetchone()

def getRoomInfo(location):
    """Returns all info on room requested by location"""

    cmd=f"""SELECT * FROM room WHERE location="{location}";""" #we use "{location}" because it wouldnt have "" otherwise and querry qould fail
    return execute_sql(cursor,cmd).fetchone()

def getEquipmentInfo(serial_number):
    """Returns all info on Equipment requested by serial_number"""

    cmd=f"""SELECT * FROM equipment WHERE serial_number={serial_number};"""
    #print(cmd)
    return execute_sql(cursor,cmd).fetchone()

make_clients()
make_employees()
make_rooms()
make_equipment()
make_subscription()


print(getUserInfo("1"))
print(getEmployeeInfo("123456789"))
print(getRoomInfo("Patra1"))
print(getEquipmentInfo("123456789"))


connection.commit()
connection.close()