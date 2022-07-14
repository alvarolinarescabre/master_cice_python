import os
import sqlite3
import datetime as dt
from uuid import uuid4
from hashlib import sha256


class Chat:
    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()

    def create_table(self, sql):
        self.cursor.execute(sql)

    def insert_into_table(self, sql, data):
        self.cursor.execute(sql, data)

    def select_all(self, table):
        data = self.cursor.execute(f"""SELECT * FROM {table}""")

        for item in data:
            print("-------------------------------------------")
            print(f"\tTítulo: {item[1]}")
            print(f"\tAutor: {item[2]}")
            print(f"\tGénero: {item[3]}")

        print("-------------------------------------------")

    def select_by_item(self, table, item, value):
        data = self.cursor.execute(f"""SELECT * FROM {table} WHERE {item} LIKE '%{value}%'""")

        for item in data:
            print("-------------------------------------------")
            print(f"\tTítulo: {item[1]}")
            print(f"\tAutor: {item[2]}")
            print(f"\tGénero: {item[3]}")

        print("-------------------------------------------")

    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d


def main():
    CWD = os.getcwd()
    chat = Chat(f"{CWD}/chat.db")
    chat.conn.row_factory = chat.dict_factory
    now = dt.datetime.now().isoformat()

    sql_create_tables = {
        "table_users": """
                CREATE TABLE IF NOT EXISTS users (
                    id text PRIMARY KEY,
                    name text NOT NULL,
                    pwd text NOT NULL
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

    sql_insert_into_tables = {
        "table_users": f"""
                    INSERT INTO users VALUES (?,?,?)
                    """,
        "table_msgs": """
                    INSERT INTO msgs VALUES (?,?,?,?,?,?,?,?)
                    """
    }

    user = {"id": uuid4().hex,
            "name": "Chamo",
            "pwd": sha256("Abc123***".encode('utf-8')).hexdigest(),
            }
    chat.insert_into_table(sql_insert_into_tables["table_users"], tuple(user.values()))

    # msg = {"id": uuid4().hex,
    #         "title": "Chamo",
    #         "author": "Linares",
    #         }
    #
    # chat.insert_into_table(sql_insert_into_tables["table_users"], tuple(user.values()))

    # chat.select_all("books")
    # chat.select_item("books", "author", "Isaac Asimov")
    # chat.select_by_item("books", "author", "Asi")


if __name__ == "__main__":
    main()
