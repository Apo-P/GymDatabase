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
CREATE TABLE IF NOT EXISTS "payment"(
    "client_id" int DEFAULT NULL,
    "price" float(5) DEFAULT NULL,
    "date" date DEFAULT NULL,
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
    CONSTRAINT "afm_fk" FOREIGN key("afm") REFERENCES "employees"("afm")
);

DROP TABLE IF EXISTS "trainer";
CREATE TABLE IF NOT EXISTS "trainer"(
    "afm" int DEFAULT NULL,
    CONSTRAINT "afm_fk" FOREIGN key("afm") REFERENCES "employees"("afm")
);

DROP TABLE IF EXISTS "personal_trainer";
CREATE TABLE IF NOT EXISTS"personal_trainer"(
    "afm" int DEFAULT NULL,
    CONSTRAINT "afm_fk" FOREIGN key("afm") REFERENCES "employees"("afm")
);



















