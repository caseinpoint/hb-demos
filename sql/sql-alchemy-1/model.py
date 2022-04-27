"""sql-alchemy-1-demo/model.py

Demo file for the SQLAlchemy 1 lecture.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Cat(db.Model):
    """Felis catus."""

    __tablename__ = "cats"

    cat_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    color = db.Column(db.String(50), nullable=True)
    hunger = db.Column(db.Integer, nullable=False, default=20)

    def __repr__(self):
        """Show info about cat."""

        return f"<Cat id={self.cat_id} name={self.name}>"

    def greet(self):
        """Greet using name."""

        return f"Meow! I'm {self.name}"

    def feed(self, units=10):
        """Nom nom nom."""

        self.hunger -= units
        self.hunger = max(self.hunger, 0)


# class CatOwner(db.Model):
#     __tablename__ = "owners"

#     owner_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(50), nullable=False)

def connect_to_db(app, db_name):
    """Connect to database."""

    print('Connecting to db...', end=' ')

    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{db_name}"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)

    print('Connected!')


if __name__ == "__main__":
    from server import app

    connect_to_db(app, "cats")
