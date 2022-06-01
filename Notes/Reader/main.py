with open("test.txt", "w") as f:
    f.write("hola piquito!!!!")
    f.close()

with open("test.txt", "r") as f:
    data =f.readlines()

    for line in data:
        print(line.capitalize(), end="")

    f.close()


