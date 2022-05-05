"""Data model for bears."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#---------------------------------------------------------------------#

class Bear(db.Model):
    """Map points for bears."""

    __tablename__ = "bears"

    marker_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    bear_id = db.Column(db.String(64), nullable=True)
    gender = db.Column(db.String(64), nullable=True)
    birth_year = db.Column(db.String(64), nullable=True)
    cap_year = db.Column(db.String(64), nullable=True)
    cap_lat = db.Column(db.Float, nullable=True)
    cap_long = db.Column(db.Float, nullable=True)
    collared = db.Column(db.String(15), nullable=True)

    def __init__(self,
                 bear_id,
                 gender,
                 birth_year,
                 cap_year,
                 cap_lat,
                 cap_long,
                 collared):
        """Create a bear."""

        self.bear_id = bear_id
        self.gender = gender
        self.birth_year = birth_year
        self.cap_year = cap_year
        self.cap_lat = cap_lat
        self.cap_long = cap_long
        self.collared = collared


    def __repr__(self):
        """Clear representation of bear."""

        repr_str = "<Bear marker_id={marker_id}>"

        return repr_str.format(marker_id=self.marker_id)


#---------------------------------------------------------------------#

def connect_to_db(app):
    """Connect the database to Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///bears'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    print("Connected to DB.")
