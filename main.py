from tracking import shop,see_inven
from customer import production
import random
from time import sleep
from recipe_pricing_messer import set_recipe
from intro_messer import intro

    
def diff():
    difficult = input("What difficulty do you want to play? 1.Easy/ 2.Medium/ 3.Hard/ 4.Impossible \n")
    if difficult.lower() == "easy" or difficult == "1":
        return 175
    elif difficult.lower() == "medium" or difficult == "2":
        return 150
    elif difficult.lower() == "hard" or difficult == "3":
        return 115
    elif difficult.lower() == "impossible" or difficult == "4":  
        return 100
    

inventory = {
        "p_sugar": 0,
        "p_lemons" : 0,
        "p_ice" : 0,
        "p_cups" : 0,
        "cash":diff()}

recipe = {
    "r_sugar":0,
    "r_lemons":0,
    "r_ice":0,
    "price": 0
}
days = 0


def day():
    global days
    choice = input("Which thing do you want to do?\n1.Shop\n2.See inventory\n3.Set recipe\n4.Start Day\n")

    # IF choice = 1 OR choice = "words" THEN {
    #       DO THING
    #} ELSE IF choice = 2 THEN {
    #       DO THING 2}

    if choice == "1" or choice =="shop" :
        print("~~~~~~~~~~SHOP~~~~~~~~~~")
        while shop(inventory) != 0:
            if inventory['cash'] <= 0:
                print("Out of money:(")
                break
    elif choice == "2" or choice.lower() ==  "see inventory":
        print("~~~~~~~~~~INVENTORY~~~~~~~~~~")
        see_inven(inventory)
    elif choice == "3" or choice.lower() == "set recipe":
        print("~~~~~~~~~~RECIPE~~~~~~~~~~")
        set_recipe(recipe)
        print(f"In your recipe you have:\n{recipe['r_lemons']} lemons,\n{recipe['r_sugar']} sugar,\n{recipe['r_ice']} ice cubes")
    elif choice == "4" or choice.lower() == "start day":
        print("~~~~~~~~~~WERE OPEN FOR BUISNESS~~~~~~~~~~")
        for _ in range(random.randint(30,60)):
            production(recipe, inventory)
            sleep(random.random()*2)
            if inventory["p_lemons"] <= 0 or inventory["p_ice"] <= 0 or inventory["p_sugar"] <= 0 or inventory["p_cups"] <= 0:
                print("Need more supplies :(")
                break
        
        
        days += 1
        print(f"End of day {days}")
        print(f"Cash: {inventory['cash']}\nLemons:{inventory['p_lemons']}\nIce: {inventory['p_ice']}\nSugar: {inventory['p_sugar']}\nCups: {inventory['p_cups']}")

        
    else:
        return 0

name = input("Hi, What is your name\n")
intro(name)

while True:
    day()
    if inventory['cash'] <= 0:
            print("YOU LOSE BRO:(")
            break
    if days == 7:
        if inventory['cash']>= 200:
            print("YOU WIN")
            print("YAAAAAAAY!!!!!!!!")
            break
        elif inventory['cash'] <= 200:
            print("YOU DID NOT MAKE ENOUGH MONEY, AND YOUR FRIEND IS SAD AND HE STILL HASN'T FORGAVE YOU YET") 
            break  