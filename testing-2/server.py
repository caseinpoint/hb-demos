from flask import Flask, render_template, request, flash, redirect, session
from model import connect_to_db, Department, User

app = Flask(__name__)
app.secret_key = "secret"


@app.route("/")
def index():
    return render_template("index.html")


###### Routes for Department info
@app.route("/departments")
def department_list():
    """Show a list of all departments."""
    depts = Department.query.all()
    return render_template("depts.html", depts=depts)


@app.route("/department/<dept_code>")
def department_details(dept_code):
    """Show details of a department."""
    dept = Department.query.get(dept_code)
    return render_template("dept_details.html", dept=dept)


####### Routes for Login/Logout

@app.route('/login', methods=['GET'])
def login_form():
    """Show login form."""
    return render_template("login.html")


@app.route('/login', methods=['POST'])
def login_process():
    """Process login."""
    username = request.form["username"]
    password = request.form["password"]

    user = User.query.filter_by(username=username).first()

    if user and user.password == password:
        session["user_id"] = user.id
        return redirect("/important")
    else:
        flash("Invalid username or password")
        return redirect("/login")    


@app.route("/important")
def important():
    """Important info for logged in users."""
    if "user_id" in session:
        return render_template("important.html")

    else:
        flash("You must be logged in to view the important page")
        return redirect("/login")


@app.route("/logout")
def logout():
    """User must be logged in."""
    del session["user_id"]
    flash("Logged Out.")

    return redirect("/login")



if __name__ == "__main__":
    app.debug = True
    connect_to_db(app)
    app.run(host='0.0.0.0')
