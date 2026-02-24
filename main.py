from tracking import shop
from customer import production
import random
from time import sleep
from recipe_pricing_messer import set_recipe
from intro_messer import intro
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
name = input("Hi, What is your name")
intro(name)

choice = input("Which thing do you want to do?\n1.Shop\n2.See inventory\n3.Set recipe\n4.Start Day")

# IF choice = 1 OR choice = "words" THEN {
#       DO THING
#} ELSE IF choice = 2 THEN {
#       DO THING 2}

while True:
    if shop(inventory) == 0:
        break

        

set_recipe(recipe)
print(f"In your recipe you have:\n{recipe['r_lemons']} lemons,\n{recipe['r_sugar']} sugar,\n{recipe['r_ice']} ice cubes")

print(f"Cash: {inventory['cash']}\nIce: {inventory['p_ice']}\nLemons:{inventory['p_lemons']}\nSugar:{inventory['p_sugar']}\nCups: {inventory['p_cups']}")


for _ in range(random.randint(0,20)):
    production(recipe, inventory)
    #sleep(random.random()*2)

print(f"Cash: {inventory['cash']}\nIce: {inventory['p_ice']}\nLemons:{inventory['p_lemons']}\nSugar:{inventory['p_sugar']}\nCups: {inventory['p_cups']}")

