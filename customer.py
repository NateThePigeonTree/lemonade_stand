from customer_class import Customer
import random

def production(recipe, inventory, new_customer = Customer()):
# Write what you are trying to do as a comment
# Get customer attributes and compare the attributes to the recipe
<<<<<<< HEAD
    for _ in range(random.randint(0,20)):
        random_customer = new_customer.get_customer_attributes() 
        # Compare each aspect of "val" [sweetness, ice, price] to your recipe.
        # Decide if it will return a true/false for if they bought from you.
        #`if _they_bought:
        #       Do the thing`   
        cold = recipe["r_ice"]
        sweet = recipe["r_sugar"] - recipe["r_lemons"]
        l_price = recipe["price"]
        if random_customer["sweetness"] - sweet <= 1:
            print("THIS IS TOO SOUR!")
        
        elif random_customer["ice"] <= cold:
            print("THIS IS TOO COLD!")

        elif random_customer["price"] <= l_price:
            print("YOU'RE TOO MONEY LOVING TO BE A GOOD LEMONADE STAND!")
        else:
            inventory["p_lemons"] -= recipe["r_lemons"]
            inventory["p_ice"] -= recipe["r_ice"]
            inventory["p_sugar"] -= recipe["r_sugar"]
            inventory["money"] += recipe["price"]

            
=======
    random_customer = new_customer.get_customer_attributes() 
    # Compare each aspect of "val" [sweetness, ice, price] to your recipe.
    # Decide if it will return a true/false for if they bought from you.
    #`if _they_bought:
    #       Do the thing`   
    cold = recipe["r_ice"]
    sweet = recipe["r_sugar"] - recipe["r_lemons"]
    l_price = recipe["price"]
    if random_customer["sweetness"] - sweet >= 1:
        print("THIS IS TOO SOUR!")
    
    elif random_customer["ice"] <= cold:
        print("THIS IS TOO COLD!")

    elif random_customer["price"] >= l_price:
        print("YOU'RE TOO MONEY LOVING TO BE A GOOD LEMONADE STAND!")
    else:
        inventory["p_lemons"] -= recipe["r_lemons"]

        inventory["p_ice"] -= recipe["r_ice"]
        inventory["p_sugar"] -= recipe["r_sugar"]
        inventory["money"] += recipe["price"]

>>>>>>> 2c6df5224c780d9a3fac135fdb7adce97f5784f6
        

