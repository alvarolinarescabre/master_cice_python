import csv

with open("test.csv", "r") as f:
    data = f.read()
    print(data)
    f.close()


print("----------------------")

with open("test.csv", "r") as f:
    data = csv.DictReader(f)
    headers = data.fieldnames

    for head in headers:
        print(head, sep=",", end=" ")

    print("\n", end="")

    for item in data:
        print(f'{item["id"]} {item["marca"]} {item["rodado"]} {item["precio"]}')

    f.close()


