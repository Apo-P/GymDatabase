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
    "discount" float(5) DEFAULT NULL,
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


insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('8021933', 'Shanta', 'Ansett', '6985211941', '4737764');
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('5749480', 'Read', 'Sambell', '6965794824', '4737764');
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('0669117', 'Heida', 'Grassin', '6972275859', '4737764');
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('2896645', 'Brocky', 'Mazella', '6949343447', '8615082');
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('5500501', 'Jenilee', 'Petrozzi', '6989462762', '8615082');
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('9263100', 'Nissa', 'Kerwin', '6964999482', '8615082');
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('9561708', 'Germain', 'Aizikovitch', '6913507689', '1160330');
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('5011813', 'Iris', 'Blight', '6984775319', '1160330');
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('8590956', 'Sarina', 'Romke', '6949452292', '1160330');
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('8988322', 'Quentin', 'Tuson', '6990608135', '9938892');
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('5357805', 'Catriona', 'Palmer', '6974305148', '9938892');
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('6979371', 'Fritz', 'Ebbs', '6930014321', '9938892');
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('9669697', 'Marybelle', 'Boath', '6979932959', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('3182104', 'Carlynne', 'Crolla', '6901958605', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('5504997', 'Morganica', 'Tinghill', '6982993512', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('4554247', 'Angelo', 'Cotterel', '6944318568', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('3372484', 'Selie', 'Kingham', '6953474344', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('2864470', 'Neda', 'Adolfsen', '6967312460', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('7451715', 'Purcell', 'Bickmore', '6952572949', null);
insert into client (client_id, f_name, l_name, pnumber, personal_trainer) values ('5769311', 'Pieter', 'Flinn', '6911235558', null);
/*
insert into payment (price, date) values ('8698636', '01/09/2021');
insert into payment (price, date) values ('2447139', '03/08/2021');
insert into payment (price, date) values ('2407676', '17/07/2021');
insert into payment (price, date) values ('3882732', '02/10/2021');
insert into payment (price, date) values ('8420208', '24/05/2021');
insert into payment (price, date) values ('9433925', '31/07/2021');
insert into payment (price, date) values ('1265108', '22/03/2021');
insert into payment (price, date) values ('8941149', '30/09/2021');
insert into payment (price, date) values ('0824152', '14/02/2021');
insert into payment (price, date) values ('1752610', '03/08/2021');
insert into payment (price, date) values ('7605810', '01/06/2021');
insert into payment (price, date) values ('2158409', '01/07/2021');
insert into payment (price, date) values ('6046912', '14/01/2021');
insert into payment (price, date) values ('0072470', '07/04/2021');
insert into payment (price, date) values ('5013284', '27/10/2021');
insert into payment (price, date) values ('6545700', '08/09/2021');
insert into payment (price, date) values ('5884472', '19/02/2021');
insert into payment (price, date) values ('3510823', '29/10/2021');
insert into payment (price, date) values ('0646848', '08/12/2020');
insert into payment (price, date) values ('3219785', '08/05/2021');