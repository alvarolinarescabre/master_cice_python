import os
from Notes.Chat.handlers.db import DB
from Notes.Chat.handlers.auth import Auth


def main():
    CWD = os.getcwd()
    cookies = f"{CWD}/cookies.json"
    db = DB()
    user = Auth(cookies)

    db.create_tables()

    user.create_user("chamo", "Abc123")
    user.create_user("chamo", "Abc123")

    db.select_all("users")
    db.select_all("msgs")


if __name__ == "__main__":
    main()
