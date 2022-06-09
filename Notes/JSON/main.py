import os
import json

dir_path = os.path.dirname(os.path.realpath(__file__))

Jsonize String
with open(f"{dir_path}/data.json", encoding="utf-8") as f:
    data = f.read()
    j = json.loads(data)
    print(j["data"][0]["a"])


# Jsonize File
with open(f"{dir_path}/data.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    data["data"][0]["a"] = False

with open(f"{dir_path}/data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)
