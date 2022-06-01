import random as rdm


def menu():
    while True:
        options = ["Jugar", "Salir"]
        select = int(input(f"Seleccione una opción {({k:v for k,v in enumerate(options)})}: "))

        while select <= 1:
            if select == 0:
                game()
                break
            elif select > 0:
                exit(0)


def game():
    options = ["Piedra", "Papel", "Tijera"]
    select = int(input(f"A jugar {({k:v for k,v in enumerate(options)})}: "))

    if select > len(options) or select == "":
        print("!Seleccione una opción válida!")
    else:
        random_select = rdm.choices(options)

        if options[select] == random_select[0]:
            print(f"Haz empatado con {options[select]} contra {random_select[0]}")
        elif options[select] == "Piedra" and random_select[0] == "Papel" or \
                options[select] == "Papel" and random_select[0] == "Tijera":
            print(f"Haz perdido con {options[select]} contra {random_select[0]}")
        else:
            print(f"Haz ganado con {options[select]} contra {random_select[0]}")


if __name__ == "__main__":
    menu()
