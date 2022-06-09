import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir_path}/test.txt", "w") as f:
    f.write("hola piquito!!!!")


with open(f"{dir_path}/test.txt", "r") as f:
    data = f.readlines()
    for line in data:
        print(line.capitalize(), end="")



