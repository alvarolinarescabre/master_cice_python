import os
import time
import unittest
from Notes.Chat.handlers.db import DB
from Notes.Chat.handlers.auth import Auth


class TestAuth(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.db = DB()
        sql = f"""CREATE TABLE IF NOT EXISTS users (id text PRIMARY KEY, name text NOT NULL, pwd text NOT NULL, token text);"""
        cls.db.query(sql)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.db.con.close()
        time.sleep(2)
        os.remove(DB.path)

    def setUp(self) -> None:
        self.auth = Auth("")

    def tearDown(self) -> None:
        return None

    def test_encrypt(self):
        self.assertEqual(self.auth.encrypt("1234"), "7110eda4d09e062aa5e4a390b0a572ac0d2c0220")
        self.assertEqual(type(self.auth.encrypt("1234")), str)

    def test_create_user(self):
        self.assertEqual(self.auth.create_user("test", "Abc123"), True)
        self.assertEqual(self.auth.create_user("test", "Abc123"), False)


if __name__ == "__main__":
    unittest.main()
