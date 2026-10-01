prices= {"price_of_lemons":-1,
         "price_of_sugar": -0.5,
         "price_of_ice": -0.5,
         "price_of_cups":-1}




def tracking(value, modifier):
    value += modifier
    return value

def shop(inventory):
    #p_ice, p_cups, p_sugar
    whichProduct= input("Which product do you want to buy?\n1.Lemons\n2.Sugar\n3.Ice\n4.Cups\n5.Exit shop\n")
    if whichProduct == "1" or whichProduct.lower()=="lemons":
        lemonsBought= int(input("How many lemons do you want to buy?"))
        inventory["cash"] = tracking(inventory["cash"],prices["price_of_lemons"]*lemonsBought) 
        inventory["p_lemons"] = tracking(inventory["p_lemons"],lemonsBought)
        print("You bought {lemonsBought} lemons!")
        print(f"Cash: {inventory['cash']}\nLemons:{inventory['p_lemons']}\nSugar:{inventory['p_sugar']}\nIce:{inventory['p_ice']}\nCups:{inventory['p_ice']} " )
        return
    elif whichProduct== "2" or whichProduct.lower()=="sugar":
        sugarBought= int(input("How much sugar do you want to buy?"))
        inventory["cash"] = tracking(inventory["cash"], prices["price_of_sugar"]*sugarBought)
        inventory["p_sugar"] = tracking(inventory["p_sugar"],sugarBought)
        print("You bought{sugarBought}sugar!")
        print(f"Cash: {inventory['cash']}\nLemons:{inventory['p_lemons']}\nSugar:{inventory['p_sugar']}\nIce:{inventory['p_ice']}\nCups:{inventory['p_cups']}" )
        return
    elif whichProduct == "3" or whichProduct.lower()=="ice":
        iceBought= int(input("How much ice would you like to buy?"))
        inventory["cash"]= tracking(inventory["cash"],prices["price_of_ice"]*iceBought)
        inventory["p_ice"] = tracking(inventory["p_ice"],iceBought)
        print("You bought {iceBought} ice!")
        print(f"Cash: {inventory['cash']}\nLemons:{inventory['p_lemons']}\nSugar:{inventory['p_sugar']}\nIce:{inventory['p_ice']}\nCups:{inventory['p_cups']}" )
        return
    elif whichProduct == "4" or whichProduct.lower()=="cups":
        cupsBought= int(input("How many cups would you like?"))
        inventory["cash"] = tracking(inventory["cash"],prices["price_of_cups"]*cupsBought)
        inventory["p_cups"] = tracking(inventory["p_cups"],cupsBought)
        print("You have bought {cupsBought} cups!")
        print(f"Cash: {inventory['cash']}\nLemons:{inventory['p_lemons']}\nSugar:{inventory['p_sugar']}\nIce:{inventory['p_ice']}\nCups:{inventory['p_cups']}" )
        return
    else:
        return 0
    
def see_inven(inventory):
    print(f"Cash: {inventory['cash']}\nLemons:{inventory['p_lemons']}\nSugar:{inventory['p_sugar']}\nIce: {inventory['p_ice']}\nCups: {inventory['p_cups']}")

   
 



