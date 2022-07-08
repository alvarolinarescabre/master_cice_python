import os
from requests import get
from concurrent.futures import ThreadPoolExecutor


def countries():
    url = "https://restcountries.com/v3.1/all"
    return tuple(map(lambda country: country["name"]["common"], get(url).json()))


def download_flag(country):
    CWD = os.getcwd()
    path = f"{CWD}/flags"
    url = "https://restcountries.com/v3.1/name"

    if not os.path.exists(f"{CWD}/flags"):
        os.makedirs(f"{CWD}/flags")
    else:
        data = get(f"{url}/{country}").json()[0]
        flag = data["flags"]["png"]

        with open(f"{path}/{flag[-6:]}", "wb") as file:
            file.write(get(flag).content)


if __name__ == "__main__":
    with ThreadPoolExecutor() as executor:
        executor.map(download_flag, countries())
