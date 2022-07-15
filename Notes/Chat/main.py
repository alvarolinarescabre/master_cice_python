import os
import sqlite3
import datetime as dt
from uuid import uuid4
from hashlib import sha256
from auth import Auth


class Chat:
    def __init__(self, path):
        self.con = sqlite3.connect(path)
        self.cur = self.con.cursor()
        self.con.row_factory = self.dict_factory

    def create_table(self, sql):
        self.cur.execute(sql)

    def select_all(self, table):
        data = self.cur.execute(f"""SELECT * FROM {table}""")

        for k, v in enumerate(data):
            print("-------------------------------------------")
            print(f"\t{k}: {v}", end="\n")

        print("-------------------------------------------")

    def select_by_item(self, table, item, value):
        data = self.cur.execute(f"""SELECT * FROM {table} WHERE {item} LIKE '%{value}%'""")

        for item in data:
            print("-------------------------------------------")
            print(f"\tTítulo: {item[1]}")
            print(f"\tAutor: {item[2]}")
            print(f"\tGénero: {item[3]}")

        print("-------------------------------------------")

    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d


def main():
    CWD = os.getcwd()
    chat = Chat(f"{CWD}/chat.db")
    user = Auth(chat.con, chat)
    now = dt.datetime.now().isoformat()

    sql_create_tables = {
        "table_users": """
                CREATE TABLE IF NOT EXISTS users (
                    id text PRIMARY KEY,
                    name text NOT NULL,
                    pwd text NOT NULL,
                    token text
                    );
                """,
        "table_msgs": """
                CREATE TABLE IF NOT EXISTS msgs (
                    id text PRIMARY KEY,
                    sender text NOT NULL,
                    receiver text NOT NULL,
                    subject text NOT NULL,
                    txt text NOT NULL,
                    datetime datetime NOT NULL,
                    is_read bool NOT NULL,
                    parent_id text NOT NULL,
                    FOREIGN KEY (sender)
                        REFERENCES users (id),
                    FOREIGN KEY (receiver)
                        REFERENCES users (id)
                    );
                """,
    }

    chat.create_table(sql_create_tables["table_users"])
    chat.create_table(sql_create_tables["table_msgs"])

    user.create_user("chamo", "Abc123")
    user.create_user("chamo", "Abc123")

    chat.select_all("users")
    # chat.select_all("msgs")


if __name__ == "__main__":
    main()
