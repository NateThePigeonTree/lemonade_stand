prices= {"price_of_lemons":-5,
         "price_of_sugar": -3,
         "price_of_ice": -3,
         "price_of_cups":-5}


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


def tracking(value, modifier):
    value += modifier
    return value

def shop():
    global inventory
    global prices
    #p_ice, p_cups, p_sugar
    whichProduct= input("Which product do you want to buy? Lemons/Sugar/Ice/Cups\n")
    if whichProduct.lower()=="lemons":
        inventory["cash"] = tracking(inventory["cash"],prices["price_of_lemons"])
        inventory["p_lemons"] = tracking(inventory["p_lemons"],50)
        print(f"Cash: {inventory['cash']}\nIce: {inventory['p_ice']}\nLemons:{inventory['p_lemons']}\nSugar:{inventory['p_sugar']}\nCups: {inventory['p_cups']}")
        return
    elif whichProduct.lower()=="sugar":
        inventory["cash"] = tracking(inventory["cash"], prices["price_of_sugar"])
        inventory["p_sugar"] = tracking(inventory["p_sugar"],25)
        print(f"Cash: {inventory['cash']}\nIce: {inventory['p_ice']}\nLemons:{inventory['p_lemons']}\nSugar:{inventory['p_sugar']}\nCups: {inventory['p_cups']}")
        return
    elif whichProduct.lower()=="ice":
        inventory["cash"]= tracking(inventory["cash"],prices["price_of_ice"])
        inventory["p_ice"] = tracking(inventory["p_ice"],25)
        print(f"Cash: {inventory['cash']}\nIce: {inventory['p_ice']}\nLemons:{inventory['p_lemons']}\nSugar:{inventory['p_sugar']}\nCups: {inventory['p_cups']}")
        return
    elif whichProduct.lower()=="cups":
        inventory["cash"]== tracking(inventory["cash"],prices["price_of_cups"])
        inventory["p_cups"] = tracking(inventory["cash"],100)
        print(f"Cash: {inventory['cash']}\nIce: {inventory['p_ice']}\nLemons:{inventory['p_lemons']}\nSugar:{inventory['p_sugar']}\nCups: {inventory['p_cups']}")
        return
    else:
        return 0


while True:
    if shop() == 0:
        break
print(f"Cash: {inventory['cash']}\nIce: {inventory['p_ice']}\nLemons:{inventory['p_lemons']}\nSugar:{inventory['p_sugar']}\nCups: {inventory['p_cups']}")

