import json

with open("sample-data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Проверяем что в JSON есть список 'imdata'
if not isinstance(data, dict) or "imdata" not in data or not isinstance(data["imdata"], list):
    print("Error: imdata")
    exit(1)

data = data["imdata"]

print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<10}")
print("-" * 90)


for item in data:
    # Проверяем, что у элемента есть 'l1PhysIf' с 'attributes'
    if "l1PhysIf" in item and "attributes" in item["l1PhysIf"]:
        attributes = item["l1PhysIf"]["attributes"]

        dn = attributes.get("dn", "")
        description = attributes.get("descr", "")
        speed = attributes.get("speed", "inherit")
        mtu = attributes.get("mtu", "")

        print(f"{dn:<50} {description:<20} {speed:<10} {mtu:<10}")
    else:
        print("error")