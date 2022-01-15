BEGIN TRANSACTION;

DROP TABLE IF EXISTS "client";
CREATE TABLE IF NOT EXISTS "client" (
	"client_id"	int DEFAULT NULL,
	"f_name"	varchar(255) DEFAULT NULL,
	"l_name"	varchar(255) DEFAULT NULL,
	"pnumber"	int DEFAULT NULL,
    "personal_trainer" int DEFAULT NULL,
   	CONSTRAINT "personal_trainer_FK" FOREIGN KEY("personal_trainer") REFERENCES "personal_trainer"("afm"),

	PRIMARY KEY("client_id")
);


DROP TABLE IF EXISTS "buys";
CREATE TABLE IF NOT EXISTS"buys"(
    "date" date DEFAULT NULL,
    "name" varchar(255) DEFAULT NULL,
    "client_id" int DEFAULT NULL,
    CONSTRAINT "name_sub_FK" FOREIGN KEY("name") REFERENCES "subscription"("name"),
    CONSTRAINT "client_id_FK" FOREIGN KEY("client_id") REFERENCES "client"("client_id")
    );

DROP TABLE IF EXISTS "payment";
CREATE TABLE IF NOT EXISTS "payment" (
	"client_id"	int NOT NULL DEFAULT '0',
	"date"	date DEFAULT NULL,
	"price"	varchar(6) DEFAULT NULL,
	CONSTRAINT "client_id_FK" FOREIGN KEY("client_id") REFERENCES "client"("client_id"),
	PRIMARY KEY("client_id")
);

DROP TABLE IF EXISTS "subscription";
CREATE TABLE IF NOT EXISTS "subscription"(
    "name" varchar(255) DEFAULT NULL,
    "price" float(5) DEFAULT NULL,
    "start_date" date DEFAULT NULL,
    "end_date" date DEFAULT NULL,

    PRIMARY KEY("name")
);

DROP TABLE IF EXISTS "pays off";
CREATE TABLE IF NOT EXISTS "pays off"(
    "client_id" int DEFAULT NULL,
    "name" varchar(255) DEFAULT NULL,
    CONSTRAINT "client_id_fk" FOREIGN KEY("client_id") REFERENCES "client"("client_id"),
    CONSTRAINT "name_FK" FOREIGN KEY("name") REFERENCES "subscription"("name")
);

DROP TABLE IF EXISTS "training";
CREATE TABLE IF NOT EXISTS "training"(
    "time" datetime DEFAULT NULL,
    "duration" float(255) DEFAULT NULL,
    "date" date DEFAULT NULL,
    "name" varchar(255) DEFAULT NULL,
    "location" varchar(255) DEFAULT NULL,
    "trainer_afm" int DEFAULT NULL,
    CONSTRAINT "name_FK" FOREIGN KEY("name") REFERENCES "subscription"("name"),
    CONSTRAINT "location_FK" FOREIGN KEY("location") REFERENCES "room"("location"),
    CONSTRAINT "trainer_afm_FK" FOREIGN KEY("trainer_afm") REFERENCES "trainer"("afm"),
    PRIMARY KEY("time")
);

DROP TABLE IF EXISTS "room";
CREATE TABLE IF NOT EXISTS "room"(
    "location" varchar(255) DEFAULT NULL,
    "speciality" varchar(255) DEFAULT NULL,
    "last_cleaning" date  DEFAULT NULL,
    "size" float(255) DEFAULT NULL,
    PRIMARY KEY("location")
);

DROP TABLE IF EXISTS "use";
CREATE TABLE IF NOT EXISTS "use"(
    "time" datetime DEFAULT NULL,
    "serial_number" int DEFAULT NULL,
    CONSTRAINT "time_FK" FOREIGN KEY("time") REFERENCES "training"("time"),
    CONSTRAINT "serial_FK" FOREIGN KEY("serial_number") REFERENCES "equipment"("serial_number")
);

DROP TABLE IF EXISTS "equipment";
CREATE TABLE IF NOT EXISTS "equipment"(
    "serial_number" int DEFAULT NULL,
    "last_maintenance" date DEFAULT NULL,
    "speciality" varchar(255) DEFAULT NULL,

    PRIMARY KEY("serial_number")
);


DROP TABLE IF EXISTS "sport";
CREATE TABLE IF NOT EXISTS "sport"(
    "name" varchar(255) DEFAULT NULL,
    PRIMARY KEY("name")
);


DROP TABLE IF EXISTS "use";
CREATE TABLE IF NOT EXISTS "use"(
    "name" varchar(255) DEFAULT NULL,
    "time" varchar(255) DEFAULT NULL,
    CONSTRAINT "time_FK" FOREIGN KEY("time") REFERENCES "training"("time"),
    CONSTRAINT "name_fk" FOREIGN key("name") REFERENCES "sport"("name")
);


DROP TABLE IF EXISTS "employees";
CREATE TABLE IF NOT EXISTS "employees"(
    "afm" int DEFAULT NULL,
    "f_name" varchar(255) DEFAULT NULL,
    "l_name" varchar(255) DEFAULT NULL,
    "salary" float(255) DEFAULT NULL,
    PRIMARY KEY("afm")
);

DROP TABLE IF EXISTS "general_employyes";
CREATE TABLE IF NOT EXISTS "general_employees"(
    "afm" int DEFAULT NULL,
    PRIMARY KEY("afm")
    CONSTRAINT "afm_fk" FOREIGN key("afm") REFERENCES "employees"("afm")
);

DROP TABLE IF EXISTS "trainer";
CREATE TABLE IF NOT EXISTS "trainer"(
    "afm" int DEFAULT NULL,
    PRIMARY KEY("afm")
    CONSTRAINT "afm_fk" FOREIGN key("afm") REFERENCES "employees"("afm")
);

DROP TABLE IF EXISTS "personal_trainer";
CREATE TABLE IF NOT EXISTS"personal_trainer"(
    "afm" int DEFAULT NULL,
    PRIMARY KEY("afm")
    CONSTRAINT "afm_fk" FOREIGN key("afm") REFERENCES "employees"("afm")
);





insert into employees (afm, f_name, l_name, salary) values ('0486669', 'Vida', 'Edgcumbe', '30000');
insert into employees (afm, f_name, l_name, salary) values ('8847803', 'Farr', 'Besque', '30000');
insert into employees (afm, f_name, l_name, salary) values ('7209911', 'Cyril', 'Okroy', '30000');
insert into employees (afm, f_name, l_name, salary) values ('6101714', 'Alexei', 'Kondratovich', '30000');
insert into employees (afm, f_name, l_name, salary) values ('1881878', 'Elden', 'Liggens', '30000');
insert into employees (afm, f_name, l_name, salary) values ('1794227', 'Theodoric', 'Enriques', '30000');
insert into employees (afm, f_name, l_name, salary) values ('1905332', 'Tamas', 'Fabry', '35000');
insert into employees (afm, f_name, l_name, salary) values ('5040737', 'Lincoln', 'Roffey', '35000');
insert into employees (afm, f_name, l_name, salary) values ('3438893', 'Jerrilee', 'Foister', '35000');
insert into employees (afm, f_name, l_name, salary) values ('2321017', 'Geralda', 'Gert', '40000');
insert into employees (afm, f_name, l_name, salary) values ('3992426', 'Maurizia', 'Kenlin', '40000');
insert into employees (afm, f_name, l_name, salary) values ('5840360', 'Mirabelle', 'Dowe', '40000');
insert into employees (afm, f_name, l_name, salary) values ('8446776', 'Helsa', 'Llewhellin', '40000');
insert into employees (afm, f_name, l_name, salary) values ('4192403', 'Maryann', 'Olyff', '40000');
insert into employees (afm, f_name, l_name, salary) values ('4737764', 'Ozzy', 'Gault', '45000');
insert into employees (afm, f_name, l_name, salary) values ('8615082', 'Lind', 'Lording', '45000');
insert into employees (afm, f_name, l_name, salary) values ('6386190', 'Lanita', 'Votier', '45000');
insert into employees (afm, f_name, l_name, salary) values ('9065660', 'Davida', 'Govini', '45000');
insert into employees (afm, f_name, l_name, salary) values ('1160330', 'Megan', 'Hartus', '45000');
insert into employees (afm, f_name, l_name, salary) values ('9938892', 'Cherilyn', 'Bareford', '45000');



INSERT INTO general_employees(afm) SELECT afm FROM employees WHERE salary=='30000';
INSERT INTO trainer(afm) SELECT afm FROM employees WHERE salary>'30000';
INSERT INTO personal_trainer(afm) SELECT afm FROM employees WHERE salary>'44999';


insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('1067619', 'Teddie', 'Sked', '6914407449', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('1132146', 'Roslyn', 'Ebbings', '6930073283', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('1157761', 'Orelle', 'Rableau', '6980985551', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('1223302', 'Willy', 'Cuddy', '6946413442', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('1429335', 'Fayre', 'Strank', '6922993343', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('1538213', 'Nahum', 'Klimecki', '6917150061', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('1634171', 'Dominick', 'Featherstonhalgh', '6909371851', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('1708652', 'Calypso', 'Hutfield', '6949230728', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('1746020', 'Stace', 'Shardlow', '6982540422', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('2123906', 'Fair', 'Underwood', '6978098841', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('2165007', 'Kellie', 'Braunton', '6998595889', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('2404847', 'Emile', 'Litzmann', '6950803906', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('2434116', 'Terrance', 'Whiscard', '6931793564', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('2506226', 'Chelsie', 'Rhucroft', '6978355824', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('2537393', 'Elianora', 'Kwiek', '6927589037', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('2591713', 'Hailey', 'Ivanchov', '6986670075', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('2591968', 'Dun', 'Albiston', '6995422562', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('2705343', 'Hamilton', 'Rentenbeck', '6918030161', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('2854528', 'Marrissa', 'Ellen', '6915483525', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('2927736', 'Irita', 'Kibard', '6978825510', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('3004121', 'Eolande', 'Bravington', '6960727335', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('3069570', 'Donielle', 'Burnell', '6987913353', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('3163192', 'Avigdor', 'Vesque', '6960566178', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('3258593', 'Gwennie', 'Patten', '6987372426', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('3365089', 'Agnella', 'Grivori', '6966363461', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('3409800', 'Curt', 'Jachimiak', '6996876807', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('3606774', 'Rafaela', 'Autie', '6946853967', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('3706739', 'Erhard', 'Decaze', '6983770625', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('3762229', 'Carlina', 'Frugier', '6981063547', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('3766031', 'Carleton', 'Fawcus', '6952412813', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('3798595', 'Tuck', 'Rockhill', '6969852554', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('3808516', 'Waldemar', 'Keenleyside', '6909717448', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('3817803', 'Flori', 'Raffles', '6909444955', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('3899381', 'Rikki', 'Cardenosa', '6929512394', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('3917793', 'Willi', 'Domnick', '6900238471', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('4129386', 'Maribel', 'Le Surf', '6963985017', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('4134767', 'Clarette', 'Brocking', '6908928611', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('4174002', 'Staci', 'Stonard', '6989326390', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('4234821', 'Agretha', 'Kinton', '6936841205', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('4272801', 'Franky', 'Zanicchi', '6947141590', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('4359608', 'Em', 'Mixer', '6904632437', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('4417795', 'Clarance', 'Collison', '6937089182', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('4495013', 'Lexy', 'Schulkins', '6962972299', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('4551669', 'Yorker', 'Fishly', '6926994371', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('4627318', 'Elli', 'Gabbitis', '6926455329', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('4717453', 'Brewer', 'Juza', '6920593730', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('4922502', 'Ann', 'Dewes', '6971492124', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('5018700', 'Janessa', 'Hinken', '6957277835', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('5080890', 'Jervis', 'Arnao', '6967855525', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('5184778', 'Rodger', 'Moyler', '6909460360', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('5196473', 'Ranee', 'Ranscombe', '6941443444', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('5220365', 'Neala', 'Veschi', '6920119586', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('5229274', 'Romona', 'Boswood', '6965354470', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('5316511', 'Micky', 'Doeg', '6929652195', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('5324377', 'Chantal', 'Howell', '6945798121', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('5454590', 'Aristotle', 'Finnes', '6935254641', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('5508029', 'Mae', 'Urry', '6990624154', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('5614056', 'Donnie', 'Demeter', '6922007182', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('5705075', 'Steven', 'Longshaw', '6915198551', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('5866800', 'Willem', 'Jorczyk', '6916543455', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('6048542', 'Ryley', 'Smalcombe', '6954209635', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('6115375', 'Bren', 'Armatidge', '6984489339', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('6199076', 'Elset', 'Morter', '6999241174', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('6252502', 'Royal', 'Haville', '6980283185', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('6258884', 'Davy', 'Gammett', '6953986019', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('6326480', 'Evelina', 'Rekes', '6992303049', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('6441778', 'Keri', 'Cattellion', '6940060074', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('6525266', 'Dev', 'Welchman', '6919496440', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('6767597', 'Rory', 'MacTimpany', '6930045815', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('6959779', 'Idette', 'Clarke-Williams', '6953934601', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('7061088', 'Kane', 'Cattermoul', '6986816798', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('7213241', 'Kattie', 'Dutteridge', '6910553932', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('7283839', 'Katha', 'Punshon', '6970915124', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('7406945', 'Egan', 'Bogue', '6913935535', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('7599620', 'Eleanore', 'Hebbes', '6911798693', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('7676625', 'Ursuline', 'Timby', '6945512422', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('7687196', 'Karla', 'Wareing', '6997286383', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('8021968', 'Lurette', 'Baynton', '6942787767', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('8058209', 'Stacey', 'Scheu', '6955805993', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('8092798', 'Aloysia', 'Walasik', '6938151030', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('8133863', 'Clem', 'Sex', '6957540390', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('8198261', 'Nathanael', 'Bostock', '6901318195', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('8295954', 'Maribel', 'Robker', '6985329492', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('8324965', 'Lawry', 'Robertis', '6936884419', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('8359682', 'Avril', 'Brucker', '6932856465', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('8386125', 'Kirstin', 'Lantuffe', '6916161917', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('8438395', 'Waylon', 'Scourgie', '6935807344', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('8637088', 'Maurita', 'Elder', '6972132025', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('8711621', 'Callie', 'Hailey', '6958942939', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('8750952', 'Dawna', 'Blumer', '6966550770', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('8807756', 'Buiron', 'Pencot', '6972435013', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('8850889', 'Fred', 'McRavey', '6916118649', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('8919556', 'Winnie', 'Sollas', '6947102389', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('9077137', 'Brendon', 'Aries', '6967491199', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('9148235', 'Zsazsa', 'Ayer', '6915468117', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('9243533', 'Cherin', 'Baltzar', '6998891127', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('9443343', 'Abe', 'Lonsbrough', '6962396573', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('9785701', 'Kinny', 'Butchard', '6904456585', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('9849155', 'Moria', 'Giacopello', '6928392041', null);


insert into payment (client_id,date,price) values ('1067619', '12/01/2021', '90');
insert into payment (client_id,date,price) values ('1132146', '08/10/2021', '120');
insert into payment (client_id,date,price) values ('1157761', '09/01/2021', '30');
insert into payment (client_id,date,price) values ('1223302', '12/04/2021', '90');
insert into payment (client_id,date,price) values ('1429335', '22/12/2020', '90');
insert into payment (client_id,date,price) values ('1538213', '19/10/2021', '120');
insert into payment (client_id,date,price) values ('1634171', '04/03/2021', '120');
insert into payment (client_id,date,price) values ('1708652', '07/10/2021', '120');
insert into payment (client_id,date,price) values ('1746020', '26/09/2021', '30');
insert into payment (client_id,date,price) values ('2123906', '04/05/2021', '90');
insert into payment (client_id,date,price) values ('2165007', '24/12/2020', '30');
insert into payment (client_id,date,price) values ('2404847', '20/02/2021', '90');
insert into payment (client_id,date,price) values ('2434116', '19/12/2020', '90');
insert into payment (client_id,date,price) values ('2506226', '18/03/2021', '30');
insert into payment (client_id,date,price) values ('2537393', '18/05/2021', '30');
insert into payment (client_id,date,price) values ('2591713', '28/11/2021', '120');
insert into payment (client_id,date,price) values ('2591968', '26/10/2021', '30');
insert into payment (client_id,date,price) values ('2705343', '07/04/2021', '30');
insert into payment (client_id,date,price) values ('2854528', '10/12/2021', '30');
insert into payment (client_id,date,price) values ('2927736', '25/07/2021', '120');
insert into payment (client_id,date,price) values ('3004121', '08/04/2021', '30');
insert into payment (client_id,date,price) values ('3069570', '08/12/2021', '90');
insert into payment (client_id,date,price) values ('3163192', '09/07/2021', '90');
insert into payment (client_id,date,price) values ('3258593', '01/03/2021', '90');
insert into payment (client_id,date,price) values ('3365089', '18/09/2021', '30');
insert into payment (client_id,date,price) values ('3409800', '27/06/2021', '30');
insert into payment (client_id,date,price) values ('3606774', '08/01/2021', '30');
insert into payment (client_id,date,price) values ('3706739', '27/02/2021', '30');
insert into payment (client_id,date,price) values ('3762229', '05/09/2021', '90');
insert into payment (client_id,date,price) values ('3766031', '07/04/2021', '30');
insert into payment (client_id,date,price) values ('3798595', '30/12/2020', '30');
insert into payment (client_id,date,price) values ('3808516', '24/07/2021', '30');
insert into payment (client_id,date,price) values ('3817803', '13/08/2021', '30');
insert into payment (client_id,date,price) values ('3899381', '07/07/2021', '30');
insert into payment (client_id,date,price) values ('3917793', '15/04/2021', '30');
insert into payment (client_id,date,price) values ('4129386', '03/06/2021', '30');
insert into payment (client_id,date,price) values ('4134767', '04/07/2021', '120');
insert into payment (client_id,date,price) values ('4174002', '28/12/2020', '120');
insert into payment (client_id,date,price) values ('4234821', '15/08/2021', '120');
insert into payment (client_id,date,price) values ('4272801', '02/02/2021', '30');
insert into payment (client_id,date,price) values ('4359608', '28/06/2021', '120');
insert into payment (client_id,date,price) values ('4417795', '08/02/2021', '120');
insert into payment (client_id,date,price) values ('4495013', '12/06/2021', '90');
insert into payment (client_id,date,price) values ('4551669', '20/01/2021', '120');
insert into payment (client_id,date,price) values ('4627318', '22/01/2021', '120');
insert into payment (client_id,date,price) values ('4717453', '20/04/2021', '30');
insert into payment (client_id,date,price) values ('4922502', '20/07/2021', '90');
insert into payment (client_id,date,price) values ('5018700', '25/01/2021', '30');
insert into payment (client_id,date,price) values ('5080890', '16/03/2021', '120');
insert into payment (client_id,date,price) values ('5184778', '01/01/2021', '30');
insert into payment (client_id,date,price) values ('5196473', '15/09/2021', '120');
insert into payment (client_id,date,price) values ('5220365', '11/08/2021', '90');
insert into payment (client_id,date,price) values ('5229274', '31/12/2020', '120');
insert into payment (client_id,date,price) values ('5316511', '22/09/2021', '120');
insert into payment (client_id,date,price) values ('5324377', '19/01/2021', '30');
insert into payment (client_id,date,price) values ('5454590', '19/12/2020', '90');
insert into payment (client_id,date,price) values ('5508029', '26/01/2021', '90');
insert into payment (client_id,date,price) values ('5614056', '04/11/2021', '120');
insert into payment (client_id,date,price) values ('5705075', '18/04/2021', '30');
insert into payment (client_id,date,price) values ('5866800', '11/01/2021', '120');
insert into payment (client_id,date,price) values ('6048542', '27/02/2021', '120');
insert into payment (client_id,date,price) values ('6115375', '15/11/2021', '90');
insert into payment (client_id,date,price) values ('6199076', '13/03/2021', '90');
insert into payment (client_id,date,price) values ('6252502', '03/01/2021', '90');
insert into payment (client_id,date,price) values ('6258884', '02/12/2021', '90');
insert into payment (client_id,date,price) values ('6326480', '11/09/2021', '90');
insert into payment (client_id,date,price) values ('6441778', '25/09/2021', '30');
insert into payment (client_id,date,price) values ('6525266', '23/06/2021', '120');
insert into payment (client_id,date,price) values ('6767597', '09/06/2021', '120');
insert into payment (client_id,date,price) values ('6959779', '01/02/2021', '90');
insert into payment (client_id,date,price) values ('7061088', '31/08/2021', '90');
insert into payment (client_id,date,price) values ('7213241', '12/12/2021', '30');
insert into payment (client_id,date,price) values ('7283839', '24/05/2021', '30');
insert into payment (client_id,date,price) values ('7406945', '06/07/2021', '30');
insert into payment (client_id,date,price) values ('7599620', '22/12/2020', '30');
insert into payment (client_id,date,price) values ('7676625', '22/09/2021', '90');
insert into payment (client_id,date,price) values ('7687196', '28/02/2021', '120');
insert into payment (client_id,date,price) values ('8021968', '04/02/2021', '90');
insert into payment (client_id,date,price) values ('8058209', '13/06/2021', '120');
insert into payment (client_id,date,price) values ('8092798', '13/06/2021', '30');
insert into payment (client_id,date,price) values ('8133863', '26/11/2021', '30');
insert into payment (client_id,date,price) values ('8198261', '29/10/2021', '90');
insert into payment (client_id,date,price) values ('8295954', '03/06/2021', '90');
insert into payment (client_id,date,price) values ('8324965', '23/06/2021', '120');
insert into payment (client_id,date,price) values ('8359682', '16/11/2021', '30');
insert into payment (client_id,date,price) values ('8386125', '20/08/2021', '120');
insert into payment (client_id,date,price) values ('8438395', '10/12/2020', '30');
insert into payment (client_id,date,price) values ('8637088', '05/05/2021', '90');
insert into payment (client_id,date,price) values ('8711621', '03/08/2021', '30');
insert into payment (client_id,date,price) values ('8750952', '20/06/2021', '90');
insert into payment (client_id,date,price) values ('8807756', '13/12/2020', '120');
insert into payment (client_id,date,price) values ('8850889', '25/08/2021', '120');
insert into payment (client_id,date,price) values ('8919556', '30/07/2021', '120');
insert into payment (client_id,date,price) values ('9077137', '27/04/2021', '120');
insert into payment (client_id,date,price) values ('9148235', '14/10/2021', '120');
insert into payment (client_id,date,price) values ('9243533', '18/10/2021', '120');
insert into payment (client_id,date,price) values ('9443343', '07/04/2021', '90');
insert into payment (client_id,date,price) values ('9785701', '06/05/2021', '30');
insert into payment (client_id,date,price) values ('9849155', '03/03/2021', '90');