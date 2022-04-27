"""Sample file demonstrating SQLAlchemy joins & relationships."""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Model definitions


class Employee(db.Model):
    """Employee."""

    __tablename__ = "employees"

    employee_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    state = db.Column(db.String(2), nullable=False, default='CA')
    dept_code = db.Column(db.String(5), db.ForeignKey('departments.dept_code'))
    salary = db.Column(db.Integer, nullable=True)

    dept = db.relationship('Department', back_populates="employees")
    # dept = db.relationship('Department', backref="employees")

    def __repr__(self):
        return f"<Employee id={self.employee_id} name={self.name}>"


class Department(db.Model):
    """Department. A department has many employees."""

    __tablename__ = "departments"

    dept_code = db.Column(db.String(5), primary_key=True)
    dept_name = db.Column(db.String(20), nullable=False, unique=True)
    phone = db.Column(db.String(20))

    employees = db.relationship('Employee', back_populates="dept")
    # employees = db.relationship('Employee', backref="dept")

    def __repr__(self):
        return f"<Department code={self.dept_code} name={self.dept_name}>"


def example_data():
    """Create some sample data."""

    # In case this is run more than once, empty out existing data
    Employee.query.delete()
    Department.query.delete()

    # Add sample employees and departments
    df = Department(dept_code='fin', dept_name='Finance', phone='555-1000')
    dl = Department(dept_code='legal', dept_name='Legal', phone='555-2222')
    dm = Department(dept_code='mktg', dept_name='Marketing', phone='555-9999')
    de = Department(dept_code='eng', dept_name='Engineering', phone='555-7777')

    leonard = Employee(name='Leonard', dept=dl, salary=90000)
    liz = Employee(name='Liz', dept=dl, salary=90000, state='IL')
    maggie = Employee(name='Maggie', dept=dm, salary=70000)
    nadine = Employee(name='Nadine', state='OR')

    db.session.add_all([df, dl, dm, de, leonard, liz, maggie, nadine])
    db.session.commit()


def phone_dir_nav():
    """Show all employees."""

    # This is inefficient, as it makes a query for each department!

    emps = Employee.query.all()

    print("\n(getting departments)\n")

    for emp in emps:
        if emp.dept is not None:
            print(f"\n{emp.name:8} {emp.dept.dept_name:11} {emp.dept.phone}\n")
        else:
            print(f"\n{emp.name:8} {'-':11} {'-'}\n")


def phone_dir_nav_eager():
    """Show all employees.

    Unlike above version, this "eagerly" gets all departments at once.
    """

    emps = Employee.query.options(db.joinedload('dept')).all()

    print
    for emp in emps:
        if emp.dept is not None:
            print(f"{emp.name:8} {emp.dept.dept_name:11} {emp.dept.phone}")
        else:
            print(f"{emp.name:8} {'-':11} {'-'}")


def phone_dir_join():
    """Show employees with a join."""

    emps = db.session.query(Employee.name,
                            Department.dept_name,
                            Department.phone).join(Department).all()

    print()
    for name, dept, phone in emps:
        print(f"{name:8} {dept:11} {phone}")


def phone_dir_join_class():
    """Show employees with a join.

    This second version doesn't just get a list of data tuples,
    but a list of tuples of classes.
    """

    emps = db.session.query(Employee,
                            Department).join(Department).all()

    print
    for emp, dept in emps:
        print(f"{emp.name:8} {dept.dept_name:11} {dept.phone}")


def phone_dir_join_outerjoin():
    """Show all employees, even those without a dept."""

    emps = db.session.query(Employee,
                            Department).outerjoin(Department).all()

    print
    for emp, dept in emps:
        if dept:
            print(f"{emp.name:8} {dept.dept_name:11} {dept.phone}")
        else:
            print(f"{emp.name:8} {'-':11} {'-'}")

def phone_dir_join_full_join():
    """Show all employees and all departments."""

    emps = db.session.query(Employee,
                            Department).join(Department, full=True).all()

    print
    for emp, dept in emps:
        if emp and dept:
            print(f"{emp.name:8} {dept.dept_name:11} {dept.phone}")
        elif emp and not dept:
            print(f"{emp.name:8} {'-':11} {'-'}")
        else:
            print(f"{'-':8} {dept.dept_name:11} {dept.phone}")


##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our Postgres database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///employees'
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask

    from subprocess import run
    run(['dropdb', '--if-exists', 'employees'])
    run(['createdb', 'employees'])

    app = Flask(__name__)

    connect_to_db(app)
    print("Connected to DB.")

    db.create_all()
    example_data()
