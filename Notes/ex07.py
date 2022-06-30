from functools import wraps
from datetime import datetime as dt
from os import path

PWD = path.dirname(path.realpath(__file__))


def outter(func):
    def inner(*args):
        print("Hola soy un decorador...")
        return func(*args)
    return inner


@outter
def hello(name="World"):
    print(f"Hola {name}!!!")


@outter
def add(*args):
    return sum(args)


hello("Chamo")
print(add(1, 2, 3, 4))


def deco(func):
    @wraps(func)
    def show():
        print(f"La función '{func.__name__}' ha sido ejecutada")
        return func()
    return show


@deco
def nueva():
    return "Desde la función..."


print(nueva.__name__)


def timestamp(func):
    @wraps(func)
    def now():
        print(f"{dt.now()} | la función {func.__name__} ha generado un registro")
        return func()
    return now


def logs(func):
    @wraps(func)
    def write_logs(*args):
        with open(f"{PWD}/my.log", "a", encoding="utf-8") as file:
            file.write(f"{dt.now()} | la función {func.__name__} ha generado un registro")
            file.write("\n")
        return func(*args)
    return write_logs


@logs
def show_name(name):
    return f"This is my name: {name}"


names = ["Chamo", "Karla", "Chinchilla", "Boinga", "Chiquitina", "Piquito"]

for name in names:
    print(show_name(name))
