import json
import sqlite3
import secrets
from os import getcwd
from uuid import uuid4
from hashlib import sha1
from functools import wraps


class Auth:

    def __init__(self, con: sqlite3.Connection, cookie_path: str):
        self. con = con
        self.cookies_path = cookie_path
        self.con.row_factory = self.dict_factory

    @property
    def cur(self):
        return self.con.cursor()

    @property
    def users(self):
        return self.cur.execute("SELECT * FROM users;")

    @property
    def cookies(self):
        file = open(self.cookies_path, encoding="utf-8")
        data = json.load(file)
        file.close()
        return data

    def write_cookies(self, data):
        file = open(self.cookies_path, mode="w")
        json.dump(data, file, indent=4, ensure_ascii=False)
        return True

    @staticmethod
    def encrypt(pwd: str):
        return sha1(pwd.encode("utf-8")).hexdigest()

    @staticmethod
    def random_id():
        return uuid4().hex

    def create_user(self, name, pwd):
        user_id = self.random_id()
        pwd = self.encrypt(pwd)
        is_user = next(filter(lambda user: user["name"] == name, self.users), False)
        if not is_user:
            self.cur.execute("INSERT INTO users VALUES (?,?,?,?);", (user_id, name, pwd, None))
            self.con.commit()
            return True
        return False

    def login(self, name, pwd):
        pwd = self.encrypt(pwd)
        user = next(filter(lambda user: user["name"] == name, self.users), False)
        if user:
            if user["pwd"] == pwd:
                token = secrets.token_hex()
                self.cur.execute("""UPDATE users SET token=? WHERE name=?;""", (token, name))
                self.con.commit()
                self.write_cookies({"id": user["id"], "token": token})
                return True
        return False

    def authorization(self, func):
        @wraps(func)
        def inner(*args):
            user_id = self.cookies["id"]
            user_token = self.cookies["token"]
            user = next(filter(lambda user: user["id"] == user_id, self.users), False)
            if user:
                if user["token"] == user_token:
                    return func(*args)
        return inner

    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d


if __name__ == "__main__":
    pass
