import json
from os import getcwd
from uuid import uuid4
from hashlib import sha1


CWD = getcwd()
file_path = f"{CWD}/users.json"


def read():
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data


def write(data):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    return True


def create_user(name, pwd):
    users = read()
    user = get_user_by_name(name)

    if user:
        print(f"¡El usuario {name} ya existe!")
        return False
    else:
        pwd = sha1(pwd.encode()).hexdigest()
        user = {
            "id": uuid4().hex,
            "username": name,
            "password": pwd
        }
        users["data"].append(user)
        write(users)

        print(f"¡El usuario {name} ha sido creado!")


def get_user_by_name(name):
    return next(filter(lambda user: user["username"] == name, read()["data"]), False)


def print_username(name):
    user = get_user_by_name(name)

    if user:
        print(f"username: {user['username']}")
    else:
        print(f"¡El usuario {name} no existe!")


def is_authenticated(name, pwd):
    user = get_user_by_name(name)

    if user:
        if user["password"] == sha1(pwd.encode()).hexdigest():
            return True
        else:
            print(f"¡El clave del usuario {name} no es correcta!")
            return False
    else:
        print(f"¡El usuario {name} no existe!")
        return False


if __name__ == "__main__":
    create_user("admin", "admin")
