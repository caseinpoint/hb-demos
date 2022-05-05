"""Load bear data into database."""

from model import Bear, connect_to_db, db
from server import app

#---------------------------------------------------------------------#

def get_bears():
    """Load bears from dataset into database."""

    with open("data/bear_data.csv") as bear_data:
        for i, row in enumerate(bear_data):
            if i >= 50:
                break

            db.session.add(Bear(*row.rstrip().split(",")))

            if i % 10 == 0:
                print(f"{i} bears have been added to the database")

    db.session.commit()

#---------------------------------------------------------------------#

if __name__ == '__main__':
    connect_to_db(app)
    db.create_all()

    get_bears()
