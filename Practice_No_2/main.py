import requests as req

url = "https://datos.comunidad.madrid/catalogo/dataset/032474a0-bf11-4465-bb92-392052962866/resource/301aed82-339b-4005-ab20-06db41ee7017/download/municipio_comunidad_madrid.json"

res = req.get(url).json()
data = res["data"]


def list_top_10(key):
    return sorted(data, key=lambda value: value[key], reverse=True)[0:10]

def get_by_mun_ine(mun_ine):
    return list(filter(lambda mun: mun["municipio_codigo_ine"] == mun_ine, data))


def get_bigger_than(sup):
    return list(filter(lambda mun: mun["superficie_km2"] >= sup, data))


def get_total_sup():
    total_sup = []
    for mun in data:
        total_sup.append(mun["superficie_km2"])

    return sum(total_sup)


def get_total_density():
    return sum([mun["densidad_por_km2"] for mun in data])


def get_population():
    return sum(map(lambda mun: mun["superficie_km2"] * mun["densidad_por_km2"], data))


def get_mean():
    return get_population() / len(data)


def benford():
    result = {str(k):0 for k in range(1,10)}
    for mun in data:
        density = str(mun["densidad_por_km2"])
        result[density[0]] += 100/len(data)
    return result


# Municipios de la comunidad de Madrid

print("----------------------------------")
print("Obtener municipio por código INE")
print(get_by_mun_ine("280035"))
print("----------------------------------")

print("----------------------------------")
print("Obtener el municipio más grande")
print(get_bigger_than(500))
print("----------------------------------")

print("----------------------------------")
print("Obtener superficie total")
print(get_total_sup())
print("----------------------------------")


print("----------------------------------")
print("Obtener densidad total")
print(get_total_density())
print("----------------------------------")

print("----------------------------------")
print("Obtener la población de Madrid")
print(get_population())
print("----------------------------------")

print("----------------------------------")
print("Obtener la población media de los municipios")
print(get_mean())
print("----------------------------------")

print("----------------------------------")
print("Comprobar la ley de Benford")
print(benford())
print("----------------------------------")

print("----------------------------------")
print("Imprimir Top 10 de los municipios por superficie")
for k, v in enumerate(list_top_10("superficie_km2")):
    print(f"{k + 1}: {v}")
print("----------------------------------")
