import csv
from sqlalchemy_utils import database_exists
from marvel import db


class Battle(db.Model):
    __tablename__ = "battle"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=250), unique=True)
    popularity = db.Column(db.Integer)
    alignment = db.Column(db.String(length=250))
    gender = db.Column(db.String(length=250))
    height_m = db.Column(db.Integer)
    weight_kg = db.Column(db.Integer)
    hometown = db.Column(db.String(length=250))
    intelligence = db.Column(db.Integer)
    strength = db.Column(db.Integer)
    speed = db.Column(db.Integer)
    durability = db.Column(db.Integer)
    energy_Projection = db.Column(db.Integer)
    fighting_Skills = db.Column(db.Integer)

    def __repr__(self):
        return f"<Heroe: {self.name}>"

    @staticmethod
    def check_database_exists(database):
        engine = db.create_engine(database, {})

        if not database_exists(engine.url):
            db.create_all()
            db.session.commit()

        return True

    @staticmethod
    def insert_data_from_csv(path):
        with open(path, "r", encoding="utf-8") as file:
            csv_reader = csv.reader(file, delimiter=',')
            header = next(csv_reader, None)

            for field in csv_reader:
                kwargs = {column: value for column, value in zip(header, field)}
                entry = Battle(**kwargs)
                db.session.add(entry)
                db.session.commit()


class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(length=50), unique=True)
    password = db.Column(db.String(length=250))

    def __repr__(self):
        return f"<Username: {self.email}>"

    @staticmethod
    def create_database(database):
        db.create_all()
        db.session.commit()
