import os
from flask_migrate import Migrate
from marvel import create_app, db
from marvel.models import Battle, Users

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
Migrate(app, db)

path = "battle.csv"
database = app.config["SQLALCHEMY_DATABASE_URI"]

with app.app_context():
    if Battle.check_database_exists(database):
        Battle.insert_data_from_csv(path)

    Users.create_database(database)

if __name__ == "__main__":
    app.run()
