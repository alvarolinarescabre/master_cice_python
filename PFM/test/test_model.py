import unittest
from app import create_app, db
from marvel.models import Battle


class UserModelTestCase(unittest.TestCase):
    path = "../battle.csv"

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        db.session.commit()
        Battle.insert_data_from_csv(UserModelTestCase.path)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_check_if_hero_exists(self):
        hero = Battle.query.filter_by(name="Hulk").first()
        self.assertTrue(hero.name == "Hulk")
        self.assertFalse(hero.name == "Batman")

    def test_delete_hero(self):
        hero = Battle.query.filter_by(name="Hulk").delete()
        self.assertTrue(hero)

    def test_update_hero(self):
        hero = Battle.query.filter_by(name="Hulk").first()
        hero.alignment = "Bad"
        self.assertTrue(hero.alignment == "Bad")
        self.assertFalse(hero.alignment == "Good")