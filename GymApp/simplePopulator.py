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
    d = random.randint(p_d if m == p_m else 1, (28 if m == 2 else 30) if m==p_m else l_d)

    return "%s-%s-%s" % (y, str(m).zfill(2), str(d).zfill(2))

def create_time(previous_time = "00:00" , timelimit="23:59",simple_time=True):
    """ Create a random time that happens AFTER previous_time. (minute output is can be 00 or 30 if simple_time=True)"""
    
    p_h, p_m = (int(i) for i in previous_time.split(':'))
    l_h, l_m = (int(i) for i in timelimit.split(':'))

    h = random.randint(p_h, l_h)
    if simple_time:
        if random.getrandbits(1):
            m = "00"
        else:
            m = "30"
    else:
        m = random.randint(p_m if h == p_h else 0, 59 if h==p_h else l_m)

    return "%s:%s" % (str(h).zfill(2), str(m).zfill(2))


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
        except Exception as e:
            #raise e
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


def populate_subscriptions(amount):

    def create_subscription():

        start_date=create_date("2021-12-1","2022-01-15")

        p_y, p_m, p_d = (int(i) for i in start_date.split('-'))

        y = random.randint(p_y, 2023)
        m = random.randint(p_m if y == p_y else 1, 12 )
        d = 28 if m == 2 else 30

        end_date="%s-%s-%s" % (y, str(m).zfill(2), str(d).zfill(2))

        name=random.choice(sports)+f"-{str(m).zfill(2)}-{str(y).zfill(4)}"
        price= (m-p_m+100 if p_y==y else abs(m-p_m) + 12* abs(y-p_y)) * 100
        description=random.choice(equipment)

        return name,price,start_date,end_date,description

    for id in range(amount):
        cmd = f"""INSERT INTO subscription (name,price,start_date,end_date,description) VALUES {create_subscription()};""" #Dont use ({create_client()}) because we would end up with double ()

        #print(cmd)
        try:
            execute_sql(cursor,cmd)
        except:
            pass #except failed constraint

def make_subscriptions():

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
    populate_subscriptions(10)
    pk["subscription"]="name"


def populate_sports(amount):

    def create_sport():

        name=random.choice(sports)

        return name

    for id in range(amount):
        cmd = f"""INSERT INTO sport (name) VALUES ("{create_sport()}");""" 

        #print(cmd)
        try:
            execute_sql(cursor,cmd)
        except Exception as e:
            #raise e
            pass

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


def populate_trainings(amount,month_trainings=True):
    """if month_training=True it will make trainings for whole months for a random sport,subscription,room,trainer"""
    
    def create_training():

        date=create_date("2021-12-1","2022-12-15")
        start_time = create_time("")
        duration = random.randint(1,3)
        subscription = execute_sql(cursor,f"""SELECT name FROM subscription ORDER BY RANDOM() LIMIT 1""").fetchone()[0]
        sport = execute_sql(cursor,f"""SELECT name FROM sport ORDER BY RANDOM() LIMIT 1""").fetchone()[0]
        room = execute_sql(cursor,f"""SELECT id FROM room ORDER BY RANDOM() LIMIT 1""").fetchone()[0]
        trainer = execute_sql(cursor,f"""SELECT afm FROM trainer ORDER BY RANDOM() LIMIT 1""").fetchone()[0]

        return date,start_time,duration,subscription,sport,room,trainer

    def create_month_trainings(givendate):

        givenyear,givenmonth = givendate.split("-")[0:2]

        subscription = execute_sql(cursor,f"""SELECT name FROM subscription ORDER BY RANDOM() LIMIT 1""").fetchone()[0]
        sport = execute_sql(cursor,f"""SELECT name FROM sport ORDER BY RANDOM() LIMIT 1""").fetchone()[0]
        room = execute_sql(cursor,f"""SELECT id FROM room ORDER BY RANDOM() LIMIT 1""").fetchone()[0]
        trainer = execute_sql(cursor,f"""SELECT afm FROM trainer ORDER BY RANDOM() LIMIT 1""").fetchone()[0]

        for i in range(29 if givenmonth==2 else 32):
            date=f"{givenyear}-{givenmonth}-{str(i).zfill(2)}"
            start_time = create_time()
            duration = random.randint(1,3)
        
            values=date,start_time,duration,subscription,sport,room,trainer
            cmd = f"""INSERT INTO training (date,start_time,duration,subscription,sport,room,trainer) VALUES {values};""" #Dont use ({create_client()}) because we would end up with double ()
            #print(cmd)
            try:
                execute_sql(cursor,cmd)
            except:
                pass


    if month_trainings:
        for id in range(amount):
            create_month_trainings(create_date("2021-12-1","2022-12-1"))

    else:

        for id in range(amount):
            cmd = f"""INSERT INTO training () VALUES {create_training()};""" #Dont use ({create_client()}) because we would end up with double ()

            #print(cmd)
            try:
                execute_sql(cursor,cmd)
            except:
                pass #except failed constraint

def make_trainings():

    #delete table if it existed
    cmd="""DROP TABLE IF EXISTS training;"""
    execute_sql(cursor,cmd)

    #create table
    cmd=f"""CREATE TABLE IF NOT EXISTS training(
        "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        "date" DATE NOT NULL,
        "start_time" TIME,
        "duration" integer NOT NULL,
        "subscription" varchar(30) NOT NULL,
        "sport" varchar(30) DEFAULT NULL,
        "room" integer NOT NULL,
        "trainer" DEFAULT NULL,
        
        CONSTRAINT "subscription_fk" FOREIGN KEY("subscription") REFERENCES "subscription"("name") ON DELETE CASCADE ON UPDATE CASCADE,
        CONSTRAINT "sport_fk" FOREIGN KEY("sport") REFERENCES "sport"("name") ON DELETE CASCADE ON UPDATE CASCADE,
        CONSTRAINT "room_fk" FOREIGN KEY("room") REFERENCES "room"("id") ON DELETE CASCADE ON UPDATE CASCADE,
        CONSTRAINT "trainer_fk" FOREIGN KEY("trainer") REFERENCES "trainer"("afm") ON DELETE SET DEFAULT ON UPDATE CASCADE
    );"""

    execute_sql(cursor,cmd)
    pk["training"]="id"
    populate_trainings(100)


def populate_buys(amount):
    def create_buy():

        cmd="""SELECT id FROM client ORDER BY RANDOM();"""
        client_id = execute_sql(cursor,cmd).fetchone()[0]
        cmd="""SELECT name FROM subscription ORDER BY RANDOM();"""
        subscription = execute_sql(cursor,cmd).fetchone()[0]
        date=create_date("2021-11-1","2022-1-16")
        discount=0

        return subscription,client_id,date,discount

    for id in range(amount):
        cmd = f"""INSERT INTO buys (subscription,client_id,date,discount) VALUES {create_buy()};""" 

        #print(cmd)
        try:
            execute_sql(cursor,cmd)
        except Exception as e:
            #raise e #ERROR if it tries to make the same person buy the same subscription twice
            pass

def make_buys():
        #delete table if it existed
        cmd="""DROP TABLE IF EXISTS buys;"""
        execute_sql(cursor,cmd)

        #create table #ADD UNIQUE TOGETHER
        cmd=f"""CREATE TABLE IF NOT EXISTS buys(
            "subscription" varchar(50) NOT NULL,
            "client_id" integer NOT NULL,
            "date" DATE NOT NULL,
            "discount" float NOT NULL,
            
            CONSTRAINT "subscription_fk" FOREIGN KEY("subscription") REFERENCES "subscription"("name") ON DELETE CASCADE ON UPDATE CASCADE,
            CONSTRAINT "client_fk" FOREIGN KEY("client_id") REFERENCES "client"("id") ON DELETE CASCADE ON UPDATE CASCADE,
            UNIQUE("subscription","client_id")
            );"""

        execute_sql(cursor,cmd)
        populate_buys(10)


def populate_payments_pays_offs(client_amount):
    def create_payments():

        def create_payment(client_id,amount,init_day):
            #print(init_day)
            date=create_date(init_day,"2022-12-12") #create a random date after the date the sub was bought
            values=client_id,amount,date
            cmd = f"""INSERT INTO payment (client_id,amount,payment_date) VALUES {values};""" 
            #print(cmd)
            try:
                execute_sql(cursor,cmd)
            except Exception as e:
                #raise e
                pass

        def create_pays_off(subscription,client_id):
            values=subscription,client_id
            cmd = f"""INSERT INTO pays_off (subscription,client_id) VALUES {values};""" 
            try:
                execute_sql(cursor,cmd)
            except Exception as e:
                #raise e
                pass
            

        
        cmd = f"""SELECT c.id FROM client as c WHERE c.id NOT IN(SELECT DISTINCT client_id FROM payment) AND c.id IN(SELECT DISTINCT client_id FROM buys)  ORDER BY RANDOM();""" #select random client who has no payment but has buys
        #print(cmd)
        client_id=execute_sql(cursor,cmd).fetchone()
        #print(client_id)
        if client_id==None:
            print("everyone has payed")
            return
        client_id=client_id[0]
        #print(f"client = {client_id}")

        cmd=f"""SELECT s.name,s.price FROM subscription as s, buys as b WHERE b.subscription=s.name AND b.client_id={client_id} AND s.name NOT IN (SELECT subscription FROM pays_off WHERE client_id={client_id}) ORDER BY RANDOM();""" #select random amount from bought subscriptions to make payments for 
        #print(cmd)
        #results2=execute_sql(cursor,cmd).fetchall()
        results=execute_sql(cursor,cmd).fetchone()

        #print(f"client{client_id} has  subs:{results2} chosen sub:{results}")
        if results==None: #if this client hasnt bought anyhthing yet
            #print(f"client hasnt bought anything yet")
            return
        subscription,total_amount=results

        cmd=f"""SELECT date FROM buys WHERE subscription="{subscription}" ;"""  #select the date from the buy of the subscription
        #print(cmd)
        date=execute_sql(cursor,cmd).fetchone()[0]
        #print(date)


        div=random.randint(1,4) #select random dividant
        for i in range(div): #make payment and assign what it pays off
            #print(i)
            create_payment(client_id,total_amount/div,date)
            create_pays_off(subscription,client_id)

    for client in range(client_amount):
        create_payments()

def make_payments_pays_offs():
    def make_pays_off():
        #delete table if it existed
        cmd="""DROP TABLE IF EXISTS pays_off;"""
        execute_sql(cursor,cmd)

        #create table
        cmd=f"""CREATE TABLE IF NOT EXISTS pays_off(
            "subscription" varchar(50) NOT NULL,
            "client_id" integer NOT NULL,
            
            CONSTRAINT "subscription_fk" FOREIGN KEY("subscription") REFERENCES "subscription"("name") ON DELETE CASCADE ON UPDATE CASCADE,
            CONSTRAINT "client_fk" FOREIGN KEY("client_id") REFERENCES "payment"("id") ON DELETE CASCADE ON UPDATE CASCADE
            );"""
            #Unique is to make sure no 

        execute_sql(cursor,cmd)

    def make_payments():
        #delete table if it existed
        cmd="""DROP TABLE IF EXISTS payment;"""
        execute_sql(cursor,cmd)

        #create table
        cmd=f"""CREATE TABLE IF NOT EXISTS payment(
            "client_id" integer NOT NULL,
            "amount" integer NOT NULL,
            "payment_date" DATE NOT NULL,
            
            CONSTRAINT "client_fk" FOREIGN KEY("client_id") REFERENCES "client"("id") ON DELETE CASCADE ON UPDATE CASCADE
            );"""

        execute_sql(cursor,cmd)

    make_payments()
    make_pays_off()
    populate_payments_pays_offs(5)

def populate_relations():
    def create_equipment_use():
        def create_equipment(training_id,equipment_id):
            values=training_id,equipment_id
            #print(values)
            cmd = f"""INSERT INTO equipment_use (training_id,equipment_id) VALUES {values};""" 
            #print(cmd)
            try:
                execute_sql(cursor,cmd)
            except Exception as e:
                #raise e
                pass
            
        cmd="""SELECT id FROM training;"""
        results=execute_sql(cursor,cmd).fetchall()
        #print(results)
        for training_id in results:
            cmd="""SELECT serial_number FROM equipment ORDER BY RANDOM();"""
            equipment_id=execute_sql(cursor,cmd).fetchone()[0]
        
            create_equipment(training_id[0],equipment_id)

    def create_works():

        def create_work(gym,employee):
            values=gym,employee
            #print(values)
            cmd = f"""INSERT INTO works (gym_location,employee_afm) VALUES {values};""" 
            #print(cmd)
            try:
                execute_sql(cursor,cmd)
            except Exception as e:
                #raise e
                pass
            
        cmd="""SELECT afm FROM employee;"""
        results=execute_sql(cursor,cmd).fetchall()

        for employee in results:
            gym=random.choice(locations)
            create_work(gym,employee[0]) #employe[0] giati einai tuple 
        
    create_equipment_use()
    create_works()

def make_relations():
    def make_equipment_use():
        #delete table if it existed
        cmd="""DROP TABLE IF EXISTS equipment_use;"""
        execute_sql(cursor,cmd)

        #create table
        cmd=f"""CREATE TABLE IF NOT EXISTS equipment_use(
            "training_id" integer NOT NULL,
            "equipment_id" integer NOT NULL,
            
            CONSTRAINT "training_fk" FOREIGN KEY("training_id") REFERENCES "training"("id") ON DELETE CASCADE ON UPDATE CASCADE,
            CONSTRAINT "equipment_fk" FOREIGN KEY("equipment_id") REFERENCES "equipment"("serial_number") ON DELETE CASCADE ON UPDATE CASCADE
            );"""

        execute_sql(cursor,cmd)

    def make_works():
        #delete table if it existed
        cmd="""DROP TABLE IF EXISTS works;"""
        execute_sql(cursor,cmd)

        #create table
        cmd=f"""CREATE TABLE IF NOT EXISTS works(
            "gym_location" integer NOT NULL,
            "employee_afm" integer NOT NULL,
            
            CONSTRAINT "gym_fk" FOREIGN KEY("gym_location") REFERENCES "gym"("location") ON DELETE CASCADE ON UPDATE CASCADE,
            CONSTRAINT "employee_fk" FOREIGN KEY("employee_afm") REFERENCES "employee"("afm") ON DELETE CASCADE ON UPDATE CASCADE
            );"""

        execute_sql(cursor,cmd)
    
    make_equipment_use()
    make_works()
    populate_relations() 


def getInfo(table,key=None):
    """Get all info of a object in a table with the key given (if no key is given will return all info)"""
    if key:
        cmd=f"""SELECT * FROM {table} WHERE {pk[table]}={key};"""

        #print(cmd)
        try:
            return execute_sql(cursor,cmd).fetchone()
        except Exception as e: #for any expection will enter and name it e (since Exception class is God class for all exceptions)
            print(e)
            #raise e #can uncomment in order to stop program
    else:
        cmd=f"""SELECT * FROM {table};"""

        #print(cmd)
        try:
            return execute_sql(cursor,cmd).fetchall()
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
        if pk:
            print(f"table {name} has columns {col_names} with column: {pk[0]} being its primary key")
        else:
            print(f"table {name} has columns {col_names} with no primary key")

def printAllValues(table):
    results=getInfo(table)
    #print(results)
    for result in results:
        print(result)

def printEverything():
    for name in getTableNames():
        if name!="training" and name!="equipment_use":
            print(f"table {name} has:")
            printAllValues(name)
        elif name!="equipment_use":
            print("equipment_use has to much to show")
        else:
            print("trainings has to much to show")

make_gyms()
make_employees()
make_specialists()
make_rooms()
make_equipment()
make_sports()
make_subscriptions()
make_clients()
make_trainings()
make_buys()
make_relations()
make_payments_pays_offs()


#printEverything()

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

getAllTablesInfo()


connection.commit()
connection.close()