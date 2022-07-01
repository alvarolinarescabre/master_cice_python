import utils
import auth


def main():
    option = None

    while option != "s":
        while True:
            menu_string = '''
                0.- Buscar país
                1.- Jugar :D
                s.- Salir
            '''

            print(menu_string.center(500))
            option = input(": ")

            utils.clear_screen()

            if option == "0":
                option = utils.submenu_search_country()
                if option in utils.get_and_order_all_countries_by_names():
                    utils.get_country_info(utils.get_and_order_all_countries_by_names()[option], flag=True)
                else:
                    print("¡Debe seleccionar un país dentro de la lista!")
                break
            elif option == "1":
                random_countries = utils.submenu_regions()
                if random_countries:
                    utils.game(random_countries)
                else:
                    print("¡Debe seleccionar una región dentro de la lista!")
                break
            elif option == "s":
                break
            else:
                print("¡Debe seleccionar una opción correcta!")


if __name__ == "__main__":
    print('''
    ##############################################################
    #                           PAÍSES                           #
    ##############################################################
    '''.center(300))
    main()