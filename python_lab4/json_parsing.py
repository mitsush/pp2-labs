import json


with open("sample-data.json") as file:
    data = json.load(file)

print("Interface Status")
print(
    "================================================================================"
)
print(
    "DN                                                 Description           Speed    MTU"
)
print(
    "-------------------------------------------------- --------------------  ------  ------"
)

for elem in data["imdata"]:
    inter = elem["l1PhysIf"]["attributes"]
    print(
        f'{inter["dn"]:<50} {inter["descr"]:<20} {inter["speed"]:<6}   {inter["mtu"]:<7}'
    )
