import os
from utils import *
from auth import Auth
from logs import create_logs

CWD = os.getcwd()
file_path = f"{CWD}/users.json"
cookies_path = f"{CWD}/cookies.json"

admin = Auth(file_path, cookies_path)


@create_logs
@admin.login
def administration():
    option = None

    if True:
        while option != "r":
            while True:
                menu_string = '''
                        0.- Crear usuario
                        1.- Buscar usuario
                        r.- Regresar
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
                elif option == "r":
                    break
                else:
                    print("¡Debe seleccionar una opción correcta!")


@create_logs
@admin.login
def user_login():
    option = None

    while option != "s":
        while True:
            menu_string = '''
                0.- Buscar país
                1.- Juguemos :D
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
                    1.- Acceder a la Aplicación
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
                menu_string = '''
                                    0.- Cómo Usuario
                                    1.- Cómo Administrador
                                    r.- Regresar
                                '''

                print(menu_string.center(500))
                option = input(": ")

                if option == "0":
                    user_login()
                elif option == "1":
                    administration()
                elif option == "r":
                    break
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