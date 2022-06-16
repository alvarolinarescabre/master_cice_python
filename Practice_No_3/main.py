from os import system
import requests as req

system("clear")

base_url = "https://restcountries.com/v3.1"


def get_data(path):
    res = req.get(f"{base_url}/{path}")

    if res.status_code == 200:
        if path == "all/":
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
        temp_names.append(country['name']['common'])

    temp_names.sort()

    for k, v in enumerate(temp_names):
        countries[k + 1] = v

    return countries


def get_country_info(option):
    country = get_and_order_all_countries_by_names()[option]
    result = {}
    data = get_data(f"name/{country}")

    if data:
        result["Nombre Oficial"] = data["translations"]["spa"]["official"]
        result["Nombre Común"] = data["translations"]["spa"]["common"]
        result["Capital"] = data["capital"]
        result["Superficie"] = data["area"]
        result["Idioma(s)"] = data["languages"].values()

        return result


def submenu_all_countries(countries):
    for k, v in countries.items():
        print(f"{k}: {v}")
        if k % 24 == 0 and k:
            input("-- more --")


def submenu_search_country():
    try:
        submenu_all_countries(get_and_order_all_countries_by_names())
        option = int(input("Escriba el número del país a buscar: "))
    except (ValueError, KeyError):
        print("Debe seleccionar una opción correcta")
        menu()
    else:
        return option


def menu():
    option = None

    while option != "q":
        while True:
            menu_string = '''
                1.- Search Continent
                2.- Search Country
                3.- Search Capital
                4.- Download Country Flag's
                5.- Games :D
                q.- Exit
            '''

            print(menu_string.center(500))
            option = input(": ")
            system("clear")

            if option == "1":
                print("Selected Option No. 1")
                break
            elif option == "2":
                country = submenu_search_country()
                if country in get_and_order_all_countries_by_names():
                    format_data(get_country_info(country))
                else:
                    print("¡Debe seleccionar un país dentro de la lista!")
                break
            elif option == "3":
                print("Selected Option No. 3")
                break
            elif option == "4":
                print("Selected Option No. 4")
                break
            elif option == "5":
                print("Selected Option No. 5")
                break
            elif option == "q":
                break
            else:
                print("¡Debe seleccionar una opción correcta!")


if __name__ == "__main__":
    print('''
    ##############################################################
    #                         COUNTRIES                          #
    ##############################################################
    '''.center(300))
    menu()
