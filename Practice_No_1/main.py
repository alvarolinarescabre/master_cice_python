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


def add_book():
    book_author = input(f"Autor del Libro? : ")
    book_title = input(f"Título del Libro? : ")
    book_genre_select = int(input(f"Seleccione un Género: {[genre for genre in enumerate(genres)]}: "))

    if book_genre_select < len(genres):
        print(f"Se ha agregado el libro {book_title} del autor  {book_author} del género {genres[book_genre_select]}")
        get_books_id = [book["id"] for book in DB if book["genre"] in genres[book_genre_select]]

        if get_books_id:
            book_id = get_books_id[-1].split("_")
            new_book_id = f"{book_id[0]}_{int(book_id[1]) + 1}"
        else:
            new_book_id = f"{genres[-1][0:2].lower()}_1"
        new_book = {"id": new_book_id, "title": book_title, "author": book_author, "genre": genres[book_genre_select]}
        DB.append(new_book)
        print(DB[-1])
    elif not book_genre_select:
        print(f"¡No ha seleccionado un género válido!")
    else:
        print(f"¡El género NO exíste!")


def add_genre():
    added_genre = input(f"Escriba el tipo de género a agregar : ")

    if added_genre.isalpha():
        genres.append(added_genre)
        print(f"¡Género {added_genre} agregado!")
    else:
        print(f"¡El género NO es correcto!")


def update_book():
    book_id = input("Escriba el código del libro a actualizar: ")

    for book in DB:
        if book_id == book.get('id'):
            option = input("¿Qué desea actualizar ['titulo, 'autor', genero', 'todo']? :")

            if option == "titulo":
                titulo = input("Escriba el título nuevo: ")
                book.update({"title": titulo})
            if option == "autor":
                autor = input("Escriba el autor nuevo: ")
                book.update({"author": autor})
            if option == "genero":
                genero = input("Escriba el género nuevo: ")
                book.update({"genre": genero})
            if option == "todo":
                titulo = input("Escriba el título nuevo: ")
                autor = input("Escriba el autor nuevo: ")
                genero = input("Escriba el género nuevo: ")

                book.update({"title": titulo})
                book.update({"author": autor})
                book.update({"genre": genero})
            else:
                print("¡Debe selecionar un código existente!")

    if book_id:
        print( f"!El libro con el ID: {book_id} ha sido actualizado con éxito¡")


def delete_book():
    book_id = input("Escriba el código del libro a eliminar: ")

    if book_id:
        option = input("¿Está seguro que desea eliminar el libro seleccionado? (S/N): ")

        for key, book in enumerate(DB):
            if book_id.lower() == book.get('id').lower():
                print("-------------------------------")
                print(f"Código: {book.get('id')}")
                print(f"Título: {book.get('title')}")
                print(f"Autor: {book.get('author')}")
                print(f"Género: {book.get('genre')}")
                print("-------------------------------")
                break

        if option == "S" or option == "s" or option == "Si" or option == "si":
            del DB[key]
            print("!El libro ha sido eliminado¡")
        elif option == "N" or option == "n" or option == "No" or option == "no":
            exit(0)
        else:
            print("!Debe seleccionar una opción válida (S/N)¡")
    else:
        print("!Debe seleecionar un código de libro existente¡")


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
        genre_position = int(input(f"Seleccione un género a consultar: {({key[0] + 1:genre for key, genre in zip(enumerate(genres), genres)})}: "))
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
