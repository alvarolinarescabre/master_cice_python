import json
import secrets
from uuid import uuid4
from hashlib import sha1
from functools import wraps
from Notes.Chat.handlers.db import DB


class Auth:

    def __init__(self, cookie_path: str):
        self. db = DB()
        self.cookies_path = cookie_path

    @property
    def users(self):
        sql = f"""SELECT * FROM users;"""
        return self.db.query(sql)

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
            sql = f"""INSERT INTO users VALUES ('{user_id}', '{name}', '{pwd}', '{None}')"""
            self.db.query(sql)
            self.db.con.commit()
            return True
        return False

    def login(self, name, pwd):
        pwd = self.encrypt(pwd)
        user = next(filter(lambda user: user["name"] == name, self.users), False)
        if user:
            if user["pwd"] == pwd:
                token = secrets.token_hex()
                sql = f"""UPDATE users SET token='{token}' WHERE name='{name}';"""
                self.db.query(sql)
                self.db.con.commit()
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
