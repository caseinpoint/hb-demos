BEGIN TRANSACTION;
CREATE TABLE departments (
	dept_code VARCHAR(5) NOT NULL, 
	dept VARCHAR(20) NOT NULL, 
	phone VARCHAR(20), 
	PRIMARY KEY (dept_code), 
	UNIQUE (dept)
);
INSERT INTO "departments" VALUES('fin','Finance','555-1000');
INSERT INTO "departments" VALUES('legal','Legal','555-2222');
INSERT INTO "departments" VALUES('mktg','Marketing','555-9999');
CREATE TABLE employees (
	id SERIAL NOT NULL,
	name VARCHAR(20) NOT NULL, 
	state VARCHAR(2) NOT NULL, 
	dept_code VARCHAR(5), 
	PRIMARY KEY (id), 
	UNIQUE (name), 
	FOREIGN KEY(dept_code) REFERENCES departments (dept_code)
);
INSERT INTO "employees" VALUES(1,'Leonard','CA','legal');
INSERT INTO "employees" VALUES(2,'Liz','CA','legal');
INSERT INTO "employees" VALUES(3,'Maggie','CA','mktg');
INSERT INTO "employees" VALUES(4,'Nadine','CA',NULL);
CREATE TABLE users (
    id SERIAL NOT NULL,
    username VARCHAR(20) NOT NULL,
    password VARCHAR(20) NOT NULL,
	PRIMARY KEY (id),
	UNIQUE (username)
);
INSERT INTO users(username, password) VALUES('rachel', '123');
INSERT INTO users(username, password) VALUES('balloonicorn', 'hackbright');
COMMIT;
