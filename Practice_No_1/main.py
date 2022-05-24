DB = [{
    "id": "cf_1",
    "title": "El hombre bicentenario",
    "author": "Isaac Asimov",
    "genre": "Ciencia ficción"
},
{
    "id": "ne_1",
    "title": "Lobo de mar",
    "author": "Jack London",
    "genre": "Narrativa extranjera"
},
{
    "id": "np_1",
    "title": "El legado de los huesos",
    "author": "Dolores Redondo",
    "genre": "Narrativa policíaca"
},
{
    "id": "dc_1",
    "title": "El error de Descartes",
    "author": "Antonio Damasio",
    "genre": "Divulgación científica"
},
{
    "id": "dc_2",
    "title": "El ingenio de los pájaros",
    "author": "Jennifer Ackerman",
    "genre": "Divulgación científica"
},
{
    "id": "ne_2",
    "title": "El corazón de las tinieblas",
    "author": "Joseph Conrad",
    "genre": "Narrativa extranjera"
},
{
    "id": "cf_2",
    "title": "Metro 2033",
    "author": "Dmitri Glujovski",
    "genre": "Ciencia ficción"
},
{
    "id": "ne_3",
    "title": "Sidharta",
    "author": "Hermann Hesse",
    "genre": "Narrativa extranjera"
},
{
    "id": "ne_4",
    "title": "Andres Trapiello",
    "author": "Las armas y las letras",
    "genre": "Narrativa extranjera"
},
{
    "id": "aa_1",
    "title": "El poder del ahora",
    "author": "Ekhart Tolle",
    "genre": "Autoayuda"
},
]

genres = ["Narrativa extranjera", "Divulgación científica", "Narrativa policíaca", "Ciencia ficción", "Autoayuda"]


def get_book_by_id(book_id):
    for book in DB:
        if book_id == book.get("id"):
            return book


def add_book():
    get_author = input(f"Autor del Libro? : ")
    book_author = get_author if get_author.isalnum() else print(f"¡Debe escribir un autor!")

    get_title = input(f"Título del Libro? : ")
    book_title = get_title if get_title.isalnum() else print(f"¡Debe escribir un título!")

    get_gener= input(f"Seleccione un Género: {({key + 1:gener for key, gener in enumerate(genres)})}: ")
    book_gener = get_gener if get_gener else print("¡Debe seleccionar un género!")

    if book_gener and book_author and book_title:
        book_gener = int(book_gener) - 1
        if book_gener and book_gener < len(genres):
            get_books_id = [book["id"] for book in DB if book["genre"] in genres[book_gener]]

            if get_books_id:
                book_id = get_books_id[-1].split("_")
                new_book_id = f"{book_id[0]}_{int(book_id[1]) + 1}"
            else:
                new_book_id = f"{genres[-1][0:2].lower()}_1"
            new_book = {"id": new_book_id, "title": book_title, "author": book_author, "genre": genres[book_gener]}
            DB.append(new_book)
            print(f"Se ha agregado el libro {book_title} del autor {book_author} del género {genres[book_gener]}")


def add_genre():
    added_genre = input(f"Escriba el tipo de género a agregar : ")

    if added_genre.isalpha():
        genres.append(added_genre)
        print(f"¡Género {added_genre} agregado!")
    else:
        print(f"¡El género NO es correcto!")


def update_book():
    update_success = None
    book_id = input("Escriba el código del libro a actualizar: ")
    book = get_book_by_id(book_id)

    if book_id.lower() == book.get("id").lower():
        option = int(input("¿Qué desea actualizar [1: título, 2: autor, 3: género, 4: todo]? :"))

        if option == 1:
            print(f"El título actual es: {book.get('title')}")
            get_title = input("Escriba el título nuevo: ")
            book_title = True if get_title != '' else False
            book.update({"title": get_title}) if book_title else print("¡Debe escribir un título!")
            update_success = True if book_title else None
        elif option == 2:
            print(f"El autor actual es: {book.get('author')}")
            get_author = input("Escriba el autor nuevo: ")
            book_author = True if get_author != '' else False
            book.update({"author": get_author}) if book_author else print("¡Debe escribir un autor!")
            update_success = True if book_author else None
        elif option == 3:
            print(f"El género actual es: {book.get('genre')}")
            get_gener = int(input(f"Seleccione el nuevo género {({key + 1:gener for key, gener in enumerate(genres)})}: "))
            book.update({"genre": genres[get_gener - 1]}) if get_gener else print("¡Debe seleccionar un género!")
            update_success = True if get_gener else None
        elif option == 4:
            print("El libro a actualizar es:")
            print(f"Título: {book.get('title')}")
            print(f"Autor: {book.get('author')}")
            print(f"Género: {book.get('genre')}")

            option = input("¿Desea actualizar este libro (S/N)?: ")

            if option == "S" or option == "s" or option == "Si" or option == "si":

                title = input("Escriba el título nuevo: ")
                author = input("Escriba el autor nuevo: ")
                gener = int(input(f"Seleccione el nuevo género {({key + 1:gener for key, gener in enumerate(genres)})}: "))

                book_title = True if title != '' else False
                book.update({"title": title}) if book_title else print("¡Debe escribir un título!")
                book_author = True if author != '' else False
                book.update({"author": author}) if book_author else print("¡Debe escribir un autor!")
                book.update({"genre": genres[gener - 1]}) if gener else print("¡Debe seleccionar un género!")

                update_success = True if book_title and book_author and gener else None

            elif option == "N" or option == "n" or option == "No" or option == "no":
                return
    else:
        print("¡Debe selecionar un código existente!")

    if update_success:
        print(f"!El libro con el ID: {book_id} ha sido actualizado con éxito¡")


def delete_book():
    book_id = input("Escriba el código del libro a eliminar: ")
    book = get_book_by_id(book_id)

    if book_id.lower() == book.get("id").lower():
        print("-------------------------------")
        print(f"Código: {book.get('id')}")
        print(f"Título: {book.get('title')}")
        print(f"Autor: {book.get('author')}")
        print(f"Género: {book.get('genre')}")
        print("-------------------------------")

        option = input("¿Está seguro que desea eliminar el libro seleccionado? (S/N): ")

        if option == "S" or option == "s" or option == "Si" or option == "si":
            print(f"!El libro \"{book.get('title')}\" ha sido eliminado¡")
            DB.remove(book)
        elif option == "N" or option == "n" or option == "No" or option == "no":
            return
    else:
        print("¡Debe seleccionar un código de libro existente!")


def search_by():
    search_type = None
    key = None

    option = int(input("¿Cómo desea realizar la busqueda (1: Por ID, 2: Por Autor, 3: Por Título, 4: Por Género)?: "))

    if option == 1:
        search_type = input("Escriba el ID del libro a buscar: ")
        key = "id"
    elif option == 2:
        search_type = input("Escriba el nombre del autor a buscar: ")
        key = "author"
    elif option == 3:
        search_type = input("Escriba el título del libro a buscar: ")
        key = "title"
    elif option == 4:
        genre_position = int(input(f"Seleccione un género a consultar: {({key + 1:gener for key, gener in enumerate(genres)})}: "))
        search_type = genres[genre_position - 1] if genre_position <= len(genres) else print("¡Género no existe!")
        key = "genre"
    else:
        print("¡Debe seleecionar una opción válida!")

    if search_type and key:
        for book in DB:
            if search_type.lower() in book.get(key).lower():
                print("-------------------------------")
                print(f"Código: {book.get('id')}")
                print(f"Título: {book.get('title')}")
                print(f"Autor: {book.get('author')}")
                print(f"Género: {book.get('genre')}")
                print("-------------------------------")

                input("\n Siguiente Libro \n")

        if search_type.lower() not in [book[key] for book in DB]:
            if key == "id":
                print("¡El ID del libro no exíste!")
            elif key == "author":
                print("¡No hay libro del autor por el momento!")
            elif key == "title":
                print("¡No está disponible el título por el momento!")


def list_all_books(list_all=True):
    book_list = input(f"Listar los libros (S/N): ")

    if book_list == "S" or book_list == "s" or book_list == "Si" or book_list == "si":
        print("-------------------------------")
        for book in DB:
            print(f"Código: {book.get('id')}")
            print(f"Título: {book.get('title')}")
            print(f"Autor: {book.get('author')}")
            print(f"Género: {book.get('genre')}")
            print("-------------------------------")

        if not list_all:
            book_id = input("Ingresé el código del libro a seleccionar: ")

            if book_id not in [books.get('id') for books in DB]:
                print(f"¡El código {book_id} NO exíste¡")
            else:
                return book_id

    elif book_list == "N" or book_list == "n" or book_list == "No" or book_list == "no":
        exit(0)
    else:
        print("!Debe seleccionar una opción válida (S/N)¡")


def menu():
    option = None

    while option != "q":
        menu_string = ('''
        1 -- Agregar Libro
        2 -- Agregar un nuevo Género
        3 -- Actualizar Libro
        4 -- Eliminar Libro
        5 -- Buscar Libro
        6 -- Listar todos los libros
        q -- Exit
        ''')

        option = input(f"{menu_string}: ")

        while True:
            if option == "1":
                add_book()
                break
            elif option == "2":
                add_genre()
                break
            elif option == "3":
                update_book()
                break
            elif option == "4":
                delete_book()
                break
            elif option == "5":
                search_by()
                break
            elif option == "6":
                list_all_books()
                break
            elif option == "q":
                break
            else:
                print("Please select a correct option from menu...")
                break


if __name__ == "__main__":
    print("###################################################")
    print("############ Bienvenidos a Bookstore ##############")
    print("###################################################")

    menu()