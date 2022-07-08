import json
import secrets
from os import getcwd
from uuid import uuid4
from hashlib import sha1
from functools import wraps


class Auth:
    
    def __init__(self, file_path, cookies_path):
        self.file_path = file_path
        self.cookies_path = cookies_path
     
    @property          
    def users(self):
        with open(self.file_path, "r", encoding="utf-8") as f:
            users = json.load(f)
    
        return users
    
    @property          
    def cookies(self):
        with open(self.cookies_path, "r", encoding="utf-8") as f:
            cookies = json.load(f)
    
        return cookies
    
    def write(self, file, data):
        with open(file, "w", encoding="utf-8") as f:
            if json.dump(data, f, indent=4, ensure_ascii=False):
                return True
            else:
                return False     

    def set_user(self, username, password):
        user = self.get_user(username)
    
        if user:
            print(f"¡El usuario {username} ya existe!")
            return False
        else:
            password = sha1(password.encode()).hexdigest()
            user = {
                "id": uuid4().hex,
                "username": username,
                "password": password,
                "token": ""
            }
            
            users = self.users.copy()
            users["data"].append(user)
            
            self.write(self.file_path, users)
            print(f"¡El usuario {username} ha sido creado!")
                 
    def update_user(self, data):
        for k, v in enumerate(self.users["data"]):
            if v["username"] == data["username"]:
                users = self.users.copy()
                users["data"].pop(k)
                users["data"].insert(k, data)
                self.write(self.file_path, users)    
            
    def get_user(self, username):
        return next(filter(lambda user: user["username"] == username, self.users["data"]), False)

    def show_user_info(self, username):
        user = self.get_user(username)

        if user:
            print(f"Información del Usuario:")
            for k, v in user.items():
                print(f"{k} -> {v}")

    def validate_user(self, username, password):
        user = self.get_user(username)
    
        if user:
            if user["password"] == sha1(password.encode()).hexdigest():
                if user["token"]:
                    return True
                else:
                    self.set_cookie(username)
            else:
                print(f"¡La clave del usuario {username} no es correcta!")
                return False
        else:
            print(f"¡El usuario {username} no existe!")
            return False   

    def set_cookie(self, username):
        user = self.get_user(username)
        
        token = {"token": secrets.token_hex()}
        user.update(token)
        self.update_user(user)
        
        cookie = {
                        "id": user["id"],
                        "token": token["token"]
                    }
                    
        self.write(self.cookies_path, cookie)

    def login(self, func):
        @wraps(func)
        def inner():
            menu_string = '''
                                ######################
                                #       LOGIN        #
                                ######################
                                '''

            print(menu_string.center(500))
            username = input("Usuario: ")
            password = input("Clave: ")

            if self.validate_user(username, password):
                self.set_cookie(username)
                print(f"¡Bienvenido nuevamente {username}!")
                return func()

        return inner


if __name__ == "__main__":
    CWD = getcwd()
    file_path = f"{CWD}/users.json"
    cookies_path = f"{CWD}/cookies.json"

    user = Auth(file_path, cookies_path)
    user.set_user("admin", "admin")
