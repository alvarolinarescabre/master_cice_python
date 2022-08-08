import os
import sqlite3


class DB:
    CWD = os.getcwd()
    path = f"{CWD}/chat.db"

    def __init__(self):
        self.con = sqlite3.connect(DB.path)
        self.con.row_factory = self.dict_factory
        self.cur = self.con.cursor()

    def query(self, sql):
        return self.cur.execute(sql)

    def create_tables(self):
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

        self.query(sql_create_tables["table_users"])
        self.query(sql_create_tables["table_msgs"])

    def select_all(self, table):
        data = self.query(f"""SELECT * FROM {table}""")

        for k, v in enumerate(data):
            print("-------------------------------------------")
            print(f"\t{k}: {v}", end="\n")

        print("-------------------------------------------")

    def select_by_item(self, table, item, value):
        data = self.query(f"""SELECT * FROM {table} WHERE {item} LIKE '%{value}%'""")

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


if __name__ == "__main__":
    pass
