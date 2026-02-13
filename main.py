from tracking import shop
inventory = {
    "p_sugar": 0,
    "p_lemons" : 0,
    "p_ice" : 0,
    "p_cups" : 0,
    "cash":100}

recipe = {
    "r_sugar":0,
    "r_lemons":0,
    "r_ice":0
}

shop(inventory)

while True:
    if shop(inventory) == 0:
        break
print(f"Cash:{inventory['cash']}\nIce:{inventory['p_ice']}\nLemons:{inventory['p_lemons']}\nSugar:{inventory['p_sugar']}\nCups:{inventory['p_cups']}")

