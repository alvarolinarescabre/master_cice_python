import platform
from os import path
from os import system
from os import makedirs
from random import randint
from random import sample
import requests as req


PWD = path.dirname(path.realpath(__file__))


def clear_screen():
    if platform.system() == "Windows":
        system("cls")
    else:
        system("clear")


def get_data(path, flag=None):
    if flag:
        return req.get(path).content
    else:
        res = req.get(f"https://restcountries.com/v3.1/{path}")

        if res.status_code == 200:
            if path == "all/" or "region/" in path:
                return res.json()
            else:
                return res.json()[0]
        else:
            print("¡No exíste!")


def format_data(data):
    if data:
        for k, v in data.items():
            print(f"{k}: {v}")


def get_and_order_all_countries_by_names():
    temp_names = []
    countries = {}

    for country in get_data(f"all/"):
        temp_names.append(country["name"]["common"])

    temp_names.sort()

    for k, v in enumerate(temp_names):
        countries[k] = v

    return countries


def get_country_info(country, flag=None):
    result = {}
    data = get_data(f"name/{country}")

    if data:
        result["official"] = data["translations"]["spa"]["official"]
        result["common"] = data["translations"]["spa"]["common"]
        result["capital"] = data["capital"][0]
        result["area"] = data["area"]
        result["population"] = data["population"]
        result["languages"] = tuple(data["languages"].values())
        result["tld"] = data["tld"][0]
        result["car"] = "Izquierda" if data["car"]["side"] == "left" else "Derecha"
        result["fifa"] = "Sí" if "fifa" in data else "No"

        if flag:
            format_data(result)

            option = input("¿Desea obtener la bandera del país (S/N)?")

            if not path.exists(f"{PWD}/flags"):
                makedirs(f"{PWD}/flags")

            if option.lower() == "s":
                with open(f"{PWD}/flags/{data['flags']['png'][-6:]}", "wb") as file:
                    file.write(get_data(data['flags']['png'], flag=True))
        else:
            return result


def create_questions_and_answers(random_countries):
    select_country = random_countries[randint(0, 4)]
    country_name = select_country["name"]["common"]
    country = get_country_info(country_name, flag=False)
    qa = {
        1: {"q": "Entre estos países, ¿Cuál es el más poblado?",
            "a": list(filter(lambda c: c["population"] >= country["population"], random_countries))
            },
        2: {"q": "Entre estos países, ¿Cuál es el menos poblado?",
            "a": list(filter(lambda c: c["population"] <= country["population"], random_countries))
            },
        3: {"q": "Entre estos países, ¿Cúal es el más grande?",
            "a": list(filter(lambda c: c["area"] >= country["area"], random_countries))
            },
        4: {"q": "Entre estos países, ¿Cúal es el más pequeño?",
            "a": list(filter(lambda c: c["area"] <= country["area"], random_countries))
            },
        5: {"q": f"¿De cuál país es la capital de {country['capital']}?",
            "a": list(filter(lambda c: c["capital"][0] == country["capital"], random_countries))
            },
        6: {"q": f"¿De que país pertenece este domínio de Internet: {country['tld']}?",
            "a": list(filter(lambda c: c["tld"][0] == country["tld"], random_countries))
            },
        7: {"q": f"¿En cuál sentido se conduce en {country_name}?",
            "a": country['car']
            },
        8: {"q": f"El país {country_name}, ¿Es miembro de la FIFA?",
            "a": country['fifa']
            },
    }

    return qa


def list_questions_countries(random_countries):
    for k, v in enumerate(random_countries):
        print(f"{k}.- {v['name']['common']}", end="\n")


def game(random_countries):
    points = 0
    qa = create_questions_and_answers(random_countries)

    for k, v in qa.items():
        if k == 1 or k == 2:
            print(v["q"])
            list_questions_countries(random_countries)
            option = int(input(": "))

            if v["a"][0]["population"] == get_country_info(random_countries[option]["name"]["common"], flag=False)["population"]:
                print("¡Respuesta Correcta!")
                points += 1
            else:
                print(f"¡Respuesta Incorrecta, Respuesta: {v['a'][0]['name']['common']}")
        elif k == 3 or k == 4:
            print(v["q"])
            list_questions_countries(random_countries)
            option = int(input(": "))

            if v["a"][0]["area"] == get_country_info(random_countries[option]["name"]["common"], flag=False)["area"]:
                print("¡Respuesta Correcta!")
                points += 1
            else:
                print(f"¡Respuesta Incorrecta, Respuesta: {v['a'][0]['name']['common']}")
        elif k == 5:
            print(v["q"])
            list_questions_countries(random_countries)
            option = int(input(": "))

            if v["a"][0]["capital"][0] == get_country_info(random_countries[option]["name"]["common"], flag=False)['capital']:
                print("¡Respuesta Correcta!")
                points += 1
            else:
                print(f"¡Respuesta Incorrecta, Respuesta: {v['a'][0]['name']['common']}")
        elif k == 6:
            print(v["q"])
            list_questions_countries(random_countries)
            option = int(input(": "))

            if v["a"][0]["tld"][0] == get_country_info(random_countries[option]["name"]["common"], flag=False)['tld']:
                print("¡Respuesta Correcta!")
                points += 1
            else:
                print(f"¡Respuesta Incorrecta, Respuesta: {v['a'][0]['name']['common']}")

        elif k == 7:
            print(v["q"])
            print('''
            0.- Derecha 
            1.- Izquierda
            ''')
            option = int(input(": "))

            if option == 0:
                drive = "rigth"
            else:
                drive = "left"

            if v["a"][0] == drive:
                print("¡Respuesta Correcta!")
                points += 1
            else:
                print(f"¡Respuesta Incorrecta, Respuesta: {v['a'][0]}")
        elif k == 8:
            print(v["q"])
            print('''
            0.- Sí 
            1.- No
            ''')
            option = int(input(": "))

            if option == 0:
                fifa = True
            else:
                fifa = False

            if v["a"][0] == fifa:
                print("¡Respuesta Correcta!")
                points += 1
            else:
                print(f"¡Respuesta Incorrecta, Respuesta: {v['a'][0]}")

    print(f"Puntaje final {points}/8")


def submenu_regions():
    try:
        print('''
               0.- Africa
               1.- América
               2.- Asía
               3.- Europa
               4.- Oceanía
           ''')
        option = int(input("Seleccione una región de la lista: "))
    except (ValueError, KeyError):
        print("Debe seleccionar una opción correcta")
        exit(0)
    else:
        selected_regions = {
            0: "africa",
            1: "america",
            2: "asia",
            3: "europe",
            4: "oceania",
        }

        if option in selected_regions.keys():
            countries = get_data(f"region/{selected_regions[option]}")

            return sample(countries, k=5)


def submenu_all_countries(countries):
    for k, v in countries.items():
        print(f"{k}: {v}")
        if k % 24 == 0 and k:
            input("-- más --")


def submenu_search_country():
    try:
        submenu_all_countries(get_and_order_all_countries_by_names())
        option = int(input("Escriba el número del país a buscar: "))
    except (ValueError, KeyError):
        print("Debe seleccionar una opción correcta")
        exit(0)
    else:
        return option



