from tracking import recipe

def set_recipe():
        recipe["r_lemons"]=int(input("How many lemons would you like (ex.1/2/3):"))
        recipe["r_sugar"]=int(input("How much sugar would you like (ex.1/2/3):"))
        recipe["r_ice"]=int(input("How much ice would you like (ex.1/2/3):"))
        
set_recipe()
print(f"In your recipe you have:\n{recipe['r_lemons']} lemons,")






