from customer_class import Customer
import random

def production(recipe, inventory):
# Write what you are trying to do as a comment
# Get customer attributes and compare the attributes to the recipe

    for _ in range(random.randint(0,20)):
        new_customer = Customer()
        random_customer = new_customer.get_customer_attributes() 
        # Compare each aspect of "val" [sweetness, ice, price] to your recipe.
        # Decide if it will return a true/false for if they bought from you.
        #`if _they_bought:
        #       Do the thing`   
        cold = recipe["r_ice"]
        sweet = recipe["r_sugar"] - recipe["r_lemons"]
        l_price = recipe["price"]
        # print(f"DEBUG:\nSweet: {random_customer["sweetness"] - sweet}, Cold: {random_customer["ice"]} : {cold}, Price: {random_customer["price"]} : {l_price}")
        if random_customer["sweetness"] - sweet <= 1:
            print("THIS IS TOO SOUR!")
            
        elif random_customer["ice"] <= cold:
            print("THIS IS TOO COLD!")

        elif random_customer["price"] <= l_price:
            print("YOU'RE TOO MONEY LOVING TO BE A GOOD LEMONADE STAND!")
        else:
            print("This is good lemonade!")
            inventory["p_lemons"] -= recipe["r_lemons"]
            inventory["p_ice"] -= recipe["r_ice"]
            inventory["p_sugar"] -= recipe["r_sugar"]
            inventory["p_cups"] -= 1
            inventory["cash"] += recipe["price"]
            if inventory["p_lemons"] == 0 or inventory["p_ice"] == 0 or inventory["p_sugar"] == 0 or inventory["p_cups"] == 0:
                print("Your inventory is empty :(")
                return 0
            # print("DEBUG: LEMONADE BOUGHT")

            

     
    # Compare each aspect of "val" [sweetness, ice, price] to your recipe.
    # Decide if it will return a true/false for if they bought from you.
    #`if _they_bought:
    #       Do the thing`   



        

