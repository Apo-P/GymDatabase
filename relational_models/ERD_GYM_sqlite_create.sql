CREATE TABLE room (
	location varchar,
	speciality varchar,
	last_cleaning date,
	capacity integer
);

CREATE TABLE equipment (
	serial number integer,
	last_maintenance date,
	speciality varchar
);

CREATE TABLE sport (
	name varchar
);

CREATE TABLE training (
	date date,
	duration time,
	name varchar,
	VAT_number integer,
	location integer
);

CREATE TABLE staff (
	VAT_number integer,
	last_name varchar,
	first_name varchar,
	salary float,
	speciality boolean
);

CREATE TABLE client (
	ID integer,
	Pnumber integer,
	first_name varchar,
	last_name varchar,
	VAT_number binary
);

insert into client (id, first_name, last_name, Pnumber, VAT_number) values ('0931675', 'Meaghan', 'Revening', '8053275392', '63714534');
insert into client (id, first_name, last_name, Pnumber, VAT_number) values ('3990967', 'Rickard', 'Biddulph', '1121654719', '38630630');
insert into client (id, first_name, last_name, Pnumber, VAT_number) values ('6533703', 'Jerrilyn', 'Plum', '3829816340', '66696230');
insert into client (id, first_name, last_name, Pnumber, VAT_number) values ('4743060', 'Talya', 'Antoniutti', '5133794698', '35625913');
insert into client (id, first_name, last_name, Pnumber, VAT_number) values ('2170691', 'Land', 'Dearness', '5551035527', '21438644');
insert into client (id, first_name, last_name, Pnumber, VAT_number) values ('4496058', 'Cal', 'Pepin', '8308895997', '17109755');
insert into client (id, first_name, last_name, Pnumber, VAT_number) values ('3468958', 'Orsola', 'Magee', '7528035769', '87003960');
insert into client (id, first_name, last_name, Pnumber, VAT_number) values ('5957961', 'Thedric', 'Hapgood', '4296571087', '92132765');
insert into client (id, first_name, last_name, Pnumber, VAT_number) values ('5351909', 'Marvin', 'Groger', '6779243068', '44447316');
insert into client (id, first_name, last_name, Pnumber, VAT_number) values ('2394775', 'Ashton', 'Toth', '2268142008', '38938141');
insert into client (id, first_name, last_name, Pnumber, VAT_number) values ('1571835', 'Ryun', 'Dunbobin', '6925063746', '44550132');
insert into client (id, first_name, last_name, Pnumber, VAT_number) values ('3343645', 'Dannie', 'Briztman', '8016831095', '68920760');
insert into client (id, first_name, last_name, Pnumber, VAT_number) values ('4870091', 'Des', 'Broadhead', '7403481512', '13552138');
insert into client (id, first_name, last_name, Pnumber, VAT_number) values ('5892293', 'Paulo', 'Walburn', '5164989033', '71630484');
insert into client (id, first_name, last_name, Pnumber, VAT_number) values ('1838915', 'Shell', 'Phipps', '8171836749', '57935229');
insert into client (id, first_name, last_name, Pnumber, VAT_number) values ('5043257', 'Nicolas', 'Mander', '2989334433', '20644957');
insert into client (id, first_name, last_name, Pnumber, VAT_number) values ('9729235', 'Ronnie', 'Burger', '7684986034', '92433910');
insert into client (id, first_name, last_name, Pnumber, VAT_number) values ('0315701', 'Marlon', 'Shay', '1021061100', '38073570');
insert into client (id, first_name, last_name, Pnumber, VAT_number) values ('2770740', 'Tremaine', 'Abbatini', '1811869518', '31995205');
insert into client (id, first_name, last_name, Pnumber, VAT_number) values ('8129053', 'Stacia', 'Greves', '5543983280', '35371555');
insert into client (id, first_name, last_name, Pnumber, VAT_number) values ('5192613', 'Gabbie', 'Bragginton', '5206603207', '44209904');
insert into client (id, first_name, last_name, Pnumber, VAT_number) values ('7385456', 'Vanda', 'Corrington', '2312255658', '22592960');
insert into client (id, first_name, last_name, Pnumber, VAT_number) values ('8736016', 'Thaine', 'Baggaley', '7845130819', '89881616');
insert into client (id, first_name, last_name, Pnumber, VAT_number) values ('4171401', 'Traci', 'Eustes', '1433429676', '69342140');
insert into client (id, first_name, last_name, Pnumber, VAT_number) values ('1024845', 'Fremont', 'Leythley', '2899389037', '63014772');
insert into client (id, first_name, last_name, Pnumber, VAT_number) values ('7404458', 'Lorenzo', 'Cordner', '3109806731', '97210299');
insert into client (id, first_name, last_name, Pnumber, VAT_number) values ('9253895', 'Rocky', 'France', '8946876075', '14930696');
insert into client (id, first_name, last_name, Pnumber, VAT_number) values ('3983796', 'Vinson', 'Jodlkowski', '6367138088', '54772556');
insert into client (id, first_name, last_name, Pnumber, VAT_number) values ('9548301', 'Gertie', 'Botwright', '1826586361', '91645341');
insert into client (id, first_name, last_name, Pnumber, VAT_number) values ('4498275', 'Marcelle', 'Wilman', '8738312865', '84770043');
insert into client (id, first_name, last_name, Pnumber, VAT_number) values ('3010814', 'Fayth', 'Acaster', '7298652893', '46814656');
insert into client (id, first_name, last_name, Pnumber, VAT_number) values ('0299159', 'Lily', 'Sennett', '4397734589', '48096984');

CREATE TABLE subscription (
	name varchar,
	cost float,
	duration integer
);

CREATE TABLE payment (
	amount float,
	payment_date date,
	ID integer
);

CREATE TABLE buys (
	date date,
	discount float,
	ID integer,
	name integer
);

CREATE TABLE teeeeest(
	name varchar,
	date date
);

CREATE TABLE using (
	serial_number integer,
	date date
);










