CREATE TABLE departments (
    dept_code VARCHAR(10) PRIMARY KEY,
    dept VARCHAR(20) NOT NULL,
    phone VARCHAR(20));

INSERT INTO Departments VALUES('mktg','Marketing','555-1212');
INSERT INTO Departments VALUES('legal','Legal','555-1000');
INSERT INTO Departments VALUES('fin','Finance','555-9876');

CREATE TABLE Employees(
    id SERIAL PRIMARY KEY,
    fname VARCHAR(20) NOT NULL,
    lname VARCHAR(20) NOT NULL,
    salary INTEGER,
    full_time BOOLEAN NOT NULL DEFAULT True,
    start_date DATE,
    dept_code VARCHAR(10)
      REFERENCES Departments
    );

INSERT INTO Employees (fname, lname, salary, full_time, start_date, dept_code)
  VALUES('Liz','Lemon',90000,True,NULL,'legal'),
        ('Maggie','McEnroe',70000,True,NULL,'mktg'),
        ('Leonard','Lancelot',90000,True,NULL,'legal'),
        ('Nadine','Nelson',NULL,True,NULL,NULL)
        ;
