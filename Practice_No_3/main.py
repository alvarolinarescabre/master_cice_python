import os
from utils import *
from auth import Auth

CWD = os.getcwd()
file_path = f"{CWD}/users.json"
cookies_path = f"{CWD}/cookies.json"

admin = Auth(file_path, cookies_path)


@admin.login
def administration():
    option = None

    if True:
        while option != "s":
            while True:
                menu_string = '''
                        0.- Crear usuario
                        1.- Buscar usuario
                        s.- Salir
                    '''

                print(menu_string.center(500))
                option = input(": ")

                clear_screen()

                if option == "0":
                    username = input("Usuario: ")
                    password = input("Clave: ")
                    admin.set_user(username, password)
                    break
                elif option == "1":
                    username = input("Usuario:")
                    admin.show_user_info(username)
                    break
                elif option == "s":
                    break
                else:
                    print("¡Debe seleccionar una opción correcta!")


@admin.login
def user_login():
    option = None

    while option != "s":
        while True:
            menu_string = '''
                0.- Buscar país
                1.- Juguemos :D
                2.- Administración
                s.- Salir
            '''

            print(menu_string.center(500))
            option = input(": ")

            clear_screen()

            if option == "0":
                option = submenu_search_country()
                if option in get_and_order_all_countries_by_names():
                    get_country_info(get_and_order_all_countries_by_names()[option], flag=True)
                else:
                    print("¡Debe seleccionar un país dentro de la lista!")
                break
            elif option == "1":
                random_countries = submenu_regions()
                if random_countries:
                    game(random_countries)
                else:
                    print("¡Debe seleccionar una región dentro de la lista!")
                break
            elif option == "2":
                administration()
                break
            elif option == "s":
                break
            else:
                print("¡Debe seleccionar una opción correcta!")


def anonymous():
    option = None

    while option != "s":
        while True:
            menu_string = '''
                    0.- Buscar país
                    1.- Acceder al Juego
                    s.- Salir
                '''

            print(menu_string.center(500))
            option = input(": ")

            clear_screen()

            if option == "0":
                option = submenu_search_country()
                if option in get_and_order_all_countries_by_names():
                    get_country_info(get_and_order_all_countries_by_names()[option], flag=True)
                else:
                    print("¡Debe seleccionar un país dentro de la lista!")
                break
            elif option == "1":
                user_login()
                break
            elif option == "s":
                break
            else:
                print("¡Debe seleccionar una opción correcta!")


def main():
    anonymous()


if __name__ == "__main__":
    print('''
    ##############################################################
    #                           PAÍSES                           #
    ##############################################################
    '''.center(300))
    main()