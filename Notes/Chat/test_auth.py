import os
import time
import sqlite3
import unittest
from auth import Auth


class TestAuth(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.con = sqlite3.connect("test_chat.db")
        cursor = cls.con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users"
                       "(id text PRIMARY KEY, name text NOT NULL, pwd text NOT NULL, token text);")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.con.close()
        time.sleep(2)
        os.remove("test_chat.db")

    def setUp(self) -> None:
        self.test = Auth(TestAuth.con, "")

    def tearDown(self) -> None:
        return None

    def test_encrypt(self):
        self.assertEqual(self.test.encrypt("1234"), "7110eda4d09e062aa5e4a390b0a572ac0d2c0220")
        self.assertEqual(type(self.test.encrypt("1234")), str)

    def test_create_user(self):
        self.assertEqual(self.test.create_user("test", "Abc123"), True)
        self.assertEqual(self.test.create_user("test", "Abc123"), False)


if __name__ == "__main__":
    unittest.main()
