from tracking import shop
from customer import production
import random
from time import sleep

inventory = {
    "p_sugar": 0,
    "p_lemons" : 0,
    "p_ice" : 0,
    "p_cups" : 0,
    "cash":100}

recipe = {
    "r_sugar":0,
    "r_lemons":0,
    "r_ice":0,
    "price": 0
}

shop(inventory)

while True:
    if shop(inventory) == 0:
        break

        
from recipe_pricing_messer import set_recipe

print(f"In your recipe you have:\n{recipe['r_lemons']} lemons,\n{recipe['r_sugar']} sugar,\n{recipe['r_ice']} ice cubes")

print(f"Cash: {inventory['cash']}\nIce: {inventory['p_ice']}\nLemons:{inventory['p_lemons']}\nSugar:{inventory['p_sugar']}\nCups: {inventory['p_cups']}")

production(recipe, inventory)
<<<<<<< HEAD
=======
print(inventory)

for _ in range(random.randint(0,20)):
    production(recipe, inventory)
>>>>>>> 2c6df5224c780d9a3fac135fdb7adce97f5784f6
    # sleep(random.random()*2)

print(f"Cash: {inventory['cash']}\nIce: {inventory['p_ice']}\nLemons:{inventory['p_lemons']}\nSugar:{inventory['p_sugar']}\nCups: {inventory['p_cups']}")

