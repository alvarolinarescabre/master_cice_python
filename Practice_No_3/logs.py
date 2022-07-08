import os
from functools import wraps
from datetime import datetime

CWD = os.getcwd()


def create_logs(func):
    @wraps(func)
    def inner():
        if not os.path.exists(f"{CWD}/logs"):
            os.makedirs(f"{CWD}/logs")
        else:
            date_format = datetime.now().strftime("%Y-%m-%d")
            time_format = datetime.now().strftime("%H:%M:%S")
            with open(f"{CWD}/logs/{date_format}.log", "w") as file:
                file.write(f"{date_format} {time_format} | {func.__name__}")

        return func()

    return inner


if __name__ == "__main__":
    pass
