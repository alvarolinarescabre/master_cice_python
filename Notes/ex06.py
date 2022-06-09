import functools

a = [0,1,2,3,4,5,6,7,8,9]
b = list(filter(lambda num: num % 2 == 0, a))
print(b)

double_word = lambda word: word.upper() * 2
pow_numbers = lambda num_a, num_b: num_a ** num_b


print(double_word("hola"))
print(pow_numbers(2, 8))


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
    "title": "Las armas y las letras",
    "author": "Andres Trapiello",
    "genre": "Narrativa extranjera"
},
{
    "id": "aa_1",
    "title": "El poder del ahora",
    "author": "Ekhart Tolle",
    "genre": "Autoayuda"
},
]

list(map(lambda book: book.update({"title": book["title"].title()}), DB))
print(DB[0])


num = [6,2,1,3,4]
result = functools.reduce(lambda num_a, num_b: num_a + num_b, num)
print(result)

values = [1,2,3,4,5,6,7,8,9]

def b(num):
    return num % 2 == 0

result = list(filter(b,values))
print(result)