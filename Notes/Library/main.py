import os
import json
import sqlite3
from uuid import uuid4


class Books:
    def __init__(self, path):
        self.con = sqlite3.connect(path)
        self.cursor = self.con.cursor()
        self.con.row_factory = self.dict_factory

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

    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    @staticmethod
    def load_data(path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

            return data


def main():
    CWD = os.getcwd()
    library = Books(f"{CWD}/library.db")
    books = Books.load_data(f"{CWD}/books.json")
    authors = Books.load_data(f"{CWD}/authors.json")
    genres = Books.load_data(f"{CWD}/genres.json")

    sql_create_tables = {
        "table_books": """
                CREATE TABLE IF NOT EXISTS books (
                    id text PRIMARY KEY,
                    title text NOT NULL,
                    author text NOT NULL,
                    genre text NOT NULL,
                    FOREIGN KEY (author)
                        REFERENCES authors (id),
                    FOREIGN KEY (genre)
                        REFERENCES genre (id)
                    );
                """,
        "table_authors": """
                CREATE TABLE IF NOT EXISTS authors (
                    id text PRIMARY KEY,
                    author text NOT NULL
                    );
                """,
        "table_genres": """
                CREATE TABLE IF NOT EXISTS genres (
                    id text PRIMARY KEY,
                    genre text NOT NULL
                    );
                """,
    }

    library.create_table(sql_create_tables["table_books"])
    library.create_table(sql_create_tables["table_authors"])
    library.create_table(sql_create_tables["table_genres"])

    sql_insert_into_tables = {
        "table_books": f"""
                    INSERT INTO books VALUES (?,?,?,?)
                    """,
        "table_authors": """
                    INSERT INTO authors VALUES (?,?)
                    """,
        "table_genres": """
                    INSERT INTO genres VALUES(?,?)
                    """
    }

    for items in books:
        data = {"id": uuid4().hex,
                "title": items["title"],
                "author": items["author"],
                "genre": items["genre"]
                }

        library.insert_into_table(sql_insert_into_tables["table_books"], tuple(data.values()))

    for items in authors:
        data = {"id": uuid4().hex,
                "author": items["author"]
                }

    library.insert_into_table(sql_insert_into_tables["table_authors"], tuple(data.values()))

    for items in genres:
        data = {"id": uuid4().hex,
                "genre": items["genre"]
                }

    library.insert_into_table(sql_insert_into_tables["table_genres"], tuple(data.values()))

    # handlers.select_all("books")
    # handlers.select_item("books", "author", "Isaac Asimov")
    # handlers.select_by_item("books", "author", "Asi")



if __name__ == "__main__":
    main()
